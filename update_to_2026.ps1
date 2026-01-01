# PowerShell Script to Replace 2024 and 2025 with 2026 in all HTML files
# Run this script from the project root directory

$ErrorActionPreference = "Stop"

# Get all HTML files recursively, excluding .git folder
$htmlFiles = Get-ChildItem -Path "." -Filter "*.html" -Recurse | Where-Object { $_.FullName -notlike "*\.git\*" }

$totalFilesChecked = 0
$totalFilesModified = 0
$totalReplacements = 0

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Year Replacement Script - Update to 2026" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

foreach ($file in $htmlFiles) {
    $totalFilesChecked++
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    # Count occurrences before replacement
    $count2024 = ([regex]::Matches($content, "2024")).Count
    $count2025 = ([regex]::Matches($content, "2025")).Count
    
    # Replace 2024 with 2026
    $content = $content -replace "2024", "2026"
    
    # Replace 2025 with 2026
    $content = $content -replace "2025", "2026"
    
    # Only write if changes were made
    if ($content -ne $originalContent) {
        $totalFilesModified++
        $replacements = $count2024 + $count2025
        $totalReplacements += $replacements
        
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        
        Write-Host "Modified: $($file.FullName)" -ForegroundColor Green
        if ($count2024 -gt 0) {
            Write-Host "  - Replaced $count2024 instance(s) of '2024' with '2026'" -ForegroundColor Yellow
        }
        if ($count2025 -gt 0) {
            Write-Host "  - Replaced $count2025 instance(s) of '2025' with '2026'" -ForegroundColor Yellow
        }
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Total HTML files checked: $totalFilesChecked" -ForegroundColor White
Write-Host "Total files modified: $totalFilesModified" -ForegroundColor White
Write-Host "Total replacements made: $totalReplacements" -ForegroundColor White
Write-Host ""

if ($totalFilesModified -eq 0) {
    Write-Host "No instances of 2024 or 2025 found. All files already up to date!" -ForegroundColor Green
} else {
    Write-Host "Done! All years updated to 2026." -ForegroundColor Green
}
