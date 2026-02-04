# Verbose link checker for Base_c
$baseFull = Get-Item -LiteralPath (Join-Path (Get-Location) '.')
$report = Join-Path $baseFull.FullName 'link_check_report.json'
$missing = @()
$count = 0
$mdFiles = Get-ChildItem -Path $baseFull.FullName -Recurse -File -Include *.md
Write-Output ("Found {0} markdown files" -f $mdFiles.Count)
foreach ($file in $mdFiles) {
    $count++
    Write-Output ("Checking file {0} ({1}/{2})" -f $file.FullName, $count, $mdFiles.Count)
    try { $text = Get-Content -Raw -LiteralPath $file.FullName -ErrorAction Stop } catch { $text = '' }
    if ($text) {
        $matches = [regex]::Matches($text,'\[\[([^\]]+)\]\]')
        foreach ($m in $matches) {
            $raw = $m.Groups[1].Value
            $target = $raw.Split('|')[0].Trim()
            if ($target -ne '') {
                $t = $target -replace '/','\\'
                if (-not [IO.Path]::IsPathRooted($t)) { $cand = Join-Path $baseFull.FullName $t } else { $cand = $t }
                if (-not [IO.Path]::GetExtension($cand)) { $cand = $cand + '.md' }
                if (-not (Test-Path -LiteralPath $cand)) {
                    Write-Output ("  Missing wikilink: {0} -> {1}" -f $raw, $cand)
                    $missing += [PSCustomObject]@{file=$file.FullName; link=$raw; resolved=$cand; type='wikilink'}
                }
            }
        }
        $matches2 = [regex]::Matches($text,'\[[^\]]*\]\(([^)]+)\)')
        foreach ($m in $matches2) {
            $url = $m.Groups[1].Value.Split('#')[0].Trim()
            if ($url -and $url -notmatch '^[a-zA-Z]+:\/\/') {
                $u = $url -replace '/','\\'
                if ([IO.Path]::IsPathRooted($u)) { $cand = $u } else { $cand = Join-Path (Split-Path $file.FullName -Parent) $u }
                if (-not [IO.Path]::GetExtension($cand)) { $cand = $cand + '.md' }
                if (-not (Test-Path -LiteralPath $cand)) {
                    Write-Output ("  Missing mdlink: {0} -> {1}" -f $url, $cand)
                    $missing += [PSCustomObject]@{file=$file.FullName; link=$url; resolved=$cand; type='mdlink'}
                }
            }
        }
    }
}
$missing | ConvertTo-Json -Depth 6 | Out-File -Encoding UTF8 $report
Write-Output ("Wrote {0} (missing: {1})" -f $report, $missing.Count)
if ($missing.Count -gt 0) { $missing | Select-Object -First 20 | Format-Table -AutoSize } else { Write-Output 'No missing links found.' }
