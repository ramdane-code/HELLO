#!/usr/bin/env pwsh
Set-StrictMode -Version Latest
$base = (Resolve-Path $PSScriptRoot).Path
$toc = Join-Path $base 'toc_headings.json'
if (-not (Test-Path $toc)) { Write-Error 'toc_headings.json missing'; exit 2 }
$data = Get-Content $toc | ConvertFrom-Json
$grouped = $data | Group-Object { ([IO.Path]::GetDirectoryName($_.file)).Substring($base.Length+1) -replace '\\','/' }
$out = Join-Path $base 'index_enriched.md'
$lines = @()
$lines += '# Index enrichi — Base_c'
$lines += ''
foreach ($g in $grouped | Sort-Object Name) {
  $section = if ($g.Name) { $g.Name } else { '.' }
  $lines += "## $section"
  $seenFiles = @{}
  foreach ($item in ($g.Group | Sort-Object title)) {
    $file = $item.file
    $rel = $file.Substring($base.Length+1) -replace '\\','/'
    if ($seenFiles.ContainsKey($rel)) { continue }
    $seenFiles[$rel]=1
    $title = $item.title -replace '\n',' '
    if (-not $title) { $title = [IO.Path]::GetFileName($rel) }
    $lines += "- [$title]($rel)"
  }
  $lines += ''
}

$lines | Out-File -Encoding UTF8 $out
Write-Output "Wrote $out"
