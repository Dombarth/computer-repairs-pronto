# Fix mobile menu issues across all HTML files
# 1. Replace favicon.svg with proper logo (prontositelogo.png)
# 2. Replace multiplication sign character with SVG X icon

$closeSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>'
$closeButtonNew = '<button class="mobile-menu-close" id="menuClose" aria-label="Close menu">' + $closeSvg + '</button>'

$fixedCount = 0

# Get all HTML files
$htmlFiles = Get-ChildItem -Path "." -Filter "*.html" -Recurse | Where-Object { $_.DirectoryName -notlike "*\.git*" }

foreach ($file in $htmlFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    # Calculate logo path based on directory depth
    $relativePath = $file.DirectoryName.Replace((Get-Location).Path, "").TrimStart("\")
    $depth = if ($relativePath -eq "") { 0 } else { ($relativePath -split "\\").Count }
    
    switch ($depth) {
        0 { $logoPath = "assets/images/prontositelogo.png" }
        1 { $logoPath = "../assets/images/prontositelogo.png" }
        2 { $logoPath = "../../assets/images/prontositelogo.png" }
        default { $logoPath = "assets/images/prontositelogo.png" }
    }
    
    # Fix 1: Replace favicon.svg logo with proper logo path
    $content = $content -replace '<img src="[^"]*favicon\.svg" alt="Computer Repairs Pronto" class="logo-img">', "<img src=`"$logoPath`" alt=`"Computer Repairs Pronto`" class=`"logo-img`">"
    
    # Fix 2: Replace close button with SVG icon
    # Handle the multiplication sign character
    $content = $content -replace '<button class="mobile-menu-close" id="menuClose">[^<]{1,5}</button>', $closeButtonNew
    
    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        Write-Host "Fixed: $($file.FullName)"
        $fixedCount++
    } else {
        Write-Host "No changes needed: $($file.FullName)"
    }
}

Write-Host "`nTotal files fixed: $fixedCount"
