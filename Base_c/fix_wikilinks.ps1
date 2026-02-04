#!/usr/bin/env pwsh
Set-StrictMode -Version Latest
$base = (Resolve-Path $PSScriptRoot).Path
$report = Join-Path $base 'link_fix_suggestions.json'
if (-not (Test-Path (Join-Path $base 'link_check_report.json'))) { Write-Error 'link_check_report.json missing'; exit 2 }
$missing = Get-Content (Join-Path $base 'link_check_report.json') | ConvertFrom-Json
# build candidate index
$files = Get-ChildItem -Path $base -Recurse -File -Include *.md | ForEach-Object {
  [PSCustomObject]@{ path=$_.FullName; key=([IO.Path]::GetFileNameWithoutExtension($_.Name) -replace '[^\w]',' ' -replace '\s+',' ' -replace '\s$','').ToLowerInvariant() }
}

$suggestions = @()
foreach ($m in $missing) {
  if ($m.type -ne 'wikilink') { continue }
  $label = $m.link.Split('|')[0].Trim()
  $norm = $label -replace '[^\w]',' ' -replace '\s+',' ' -replace '^\s+|\s+$',''
  $norm = $norm.ToLowerInvariant()
  # exact filename match
  $cand = $files | Where-Object { $_.key -eq $norm } | Select-Object -First 1
  if (-not $cand) {
    # partial match: find file containing most words
    $words = $norm.Split(' ') | Where-Object { $_ -and $_.Length -gt 2 }
    $best=$null; $bestScore=0
    foreach ($f in $files) {
      $score = 0
      foreach ($w in $words) { if ($f.key -like "*${w}*") { $score++ } }
      if ($score -gt $bestScore) { $bestScore=$score; $best=$f }
    }
    if ($bestScore -ge [math]::Max(1, [int]($words.Count/2))) { $cand = $best }
  }
  if ($cand) {
    # propose relative link without extension
    $rel = $cand.path.Substring($base.Length+1) -replace '\\','/'
    $relNoExt = $rel -replace '\.md$',''
    $suggestions += [PSCustomObject]@{ file=$m.file; originalLink=$m.link; suggestion=$relNoExt; confidence='high' }
  } else {
    $suggestions += [PSCustomObject]@{ file=$m.file; originalLink=$m.link; suggestion=$null; confidence='low' }
  }
}

$suggestions | ConvertTo-Json -Depth 6 | Out-File -Encoding UTF8 $report
Write-Output "Wrote $report (items: $($suggestions.Count))"

# Apply high-confidence replacements (create backups directory)
$applied=0
$backupDir = Join-Path $base '.link_fix_backups'
if (-not (Test-Path $backupDir)) { New-Item -ItemType Directory -Path $backupDir | Out-Null }
foreach ($s in $suggestions | Where-Object { $_.confidence -eq 'high' }) {
  $f = $s.file
  $orig = Get-Content -Raw -LiteralPath $f
  $pattern = '\[\[' + [regex]::Escape($s.originalLink) + '(\|[^\]]*)?\]\]'
  $replacement = '[[{0}|{1}]]' -f $s.suggestion, $s.originalLink
  $new = [regex]::Replace($orig, $pattern, $replacement)
  if ($new -ne $orig) {
    $bak = Join-Path $backupDir ((Get-Random) + '_' + (Split-Path $f -Leaf))
    Set-Content -LiteralPath $bak -Value $orig -Encoding UTF8
    Set-Content -LiteralPath $f -Value $new -Encoding UTF8
    $applied++
  }
}
Write-Output "Applied $applied high-confidence replacements (backups in $backupDir)"
