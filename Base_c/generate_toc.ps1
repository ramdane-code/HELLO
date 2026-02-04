#!/usr/bin/env pwsh
# Génère Base_c/toc_headings.json en extrayant les titres Markdown
Set-StrictMode -Version Latest
$out = Join-Path $PSScriptRoot 'toc_headings.json'
$files = Get-ChildItem -Path $PSScriptRoot -Recurse -File -Include *.md,*.md.md
$rows = @()
foreach ($f in $files) {
  try {
    $matches = Select-String -Path $f.FullName -Pattern '^(#+)\s*(.+)$' -AllMatches -ErrorAction SilentlyContinue
    foreach ($m in $matches.Matches) {
      $rows += [PSCustomObject]@{
        file = (Resolve-Path $f.FullName).Path
        title = $m.Groups[2].Value.Trim()
      }
    }
  } catch {
    # ignorer les fichiers illisibles
  }
}
$rows | ConvertTo-Json -Depth 6 | Out-File -Encoding UTF8 $out
Write-Output "Wrote $out (items: $($rows.Count))"
