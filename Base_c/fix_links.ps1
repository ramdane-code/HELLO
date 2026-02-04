#!/usr/bin/env pwsh
Set-StrictMode -Version Latest
$P = Get-Location
$base = (Resolve-Path $PSScriptRoot).Path
$report = Join-Path $PSScriptRoot 'link_fix_report.json'
$changes = @()
$files = Get-ChildItem -Path $PSScriptRoot -Recurse -File -Include *.md,*.mdx,*.markdown
foreach ($f in $files) {
  try {
    $orig = Get-Content -Raw -LiteralPath $f.FullName -ErrorAction Stop
  } catch { continue }
  $new = $orig

  # 1) fix .md.md -> .md
  $new = $new -replace '\.md\.md','\.md'

  # 2) remove absolute base path occurrences
  $escaped = [regex]::Escape($base)
  $new = $new -replace $escaped, ''

  # 3) normalize backslashes inside markdown links and wikilinks
  $new = [regex]::Replace($new, '\(([^)]+)\)', { param($m) '(' + ($m.Groups[1].Value -replace '\\','/') + ')' })
  $new = [regex]::Replace($new, '\[\[([^\]]+)\]\]', { param($m) '[[' + ($m.Groups[1].Value -replace '\\','/') + ']]' })

  if ($new -ne $orig) {
    # backup original
    $bak = $f.FullName + '.bak'
    if (-not (Test-Path $bak)) { Set-Content -LiteralPath $bak -Value $orig -Encoding UTF8 }
    Set-Content -LiteralPath $f.FullName -Value $new -Encoding UTF8
    $changes += [PSCustomObject]@{ file = $f.FullName; changed = $true }
  }
}
$changes | ConvertTo-Json -Depth 4 | Out-File -Encoding UTF8 $report
Write-Output "Wrote $report (items: $($changes.Count))"
