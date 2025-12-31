# Add mobile-menu-phone to all HTML files

$mobilePhoneDiv = @'
            <div class="mobile-menu-phone">
                <a href="tel:0400454859"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg> 0400 454 859</a>
            </div>
'@

$htmlFiles = Get-ChildItem -Path "." -Filter "*.html" -Recurse

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # Skip if already has mobile-menu-phone
    if ($content -match 'mobile-menu-phone') {
        continue
    }
    
    # Find and replace the pattern
    $pattern = '</div>\s*<div class="mobile-menu-content">'
    if ($content -match $pattern) {
        $content = $content -replace $pattern, "</div>`n$mobilePhoneDiv`n            <div class=`"mobile-menu-content`">"
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        Write-Host "Updated: $($file.FullName)"
    }
}

Write-Host "Done!"
