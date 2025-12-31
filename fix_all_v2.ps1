# PowerShell script to fix remaining icon issues

# Phone icon SVG
$phoneSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>'

# SVG icons for service cards
$laptopSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>'
$appleSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>'
$pcSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg>'
$shieldSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path><path d="M9 12l2 2 4-4"></path></svg>'
$dataSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>'
$screenSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>'
$upgradeSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>'
$businessSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>'
$workshopSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>'
$networkSvg = '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.55a11 11 0 0 1 14.08 0"></path><path d="M1.42 9a16 16 0 0 1 21.16 0"></path><path d="M8.53 16.11a6 6 0 0 1 6.95 0"></path><line x1="12" y1="20" x2="12.01" y2="20"></line></svg>'

# Mobile menu phone header
$mobilePhoneHeader = @'
            <div class="mobile-menu-phone">
                <a href="tel:0400454859"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg> 0400 454 859</a>
            </div>
'@

# Get all HTML files
$htmlFiles = Get-ChildItem -Path "." -Filter "*.html" -Recurse

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $modified = $false
    
    # Fix empty phone icon in header
    if ($content -match '<span class="header-phone-icon"></span>') {
        $content = $content -replace '<span class="header-phone-icon"></span>', "<span class=`"header-phone-icon`">$phoneSvg</span>"
        $modified = $true
    }
    
    # Fix "PC" text in service icons
    if ($content -match '<div class="service-icon">PC</div>') {
        $content = $content -replace '<div class="service-icon">PC</div>', "<div class=`"service-icon`">$pcSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons based on context - Laptop Repairs
    if ($content -match 'href="laptop-repairs.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="laptop-repairs.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$laptopSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons - Mac Repairs
    if ($content -match 'href="mac-repairs.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="mac-repairs.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$appleSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons - PC Repairs
    if ($content -match 'href="pc-repairs.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="pc-repairs.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$pcSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons - Virus Removal
    if ($content -match 'href="virus-removal.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="virus-removal.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$shieldSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons - Data Recovery
    if ($content -match 'href="data-recovery.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="data-recovery.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$dataSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons - Screen Repairs
    if ($content -match 'href="screen-repairs.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="screen-repairs.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$screenSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons - Upgrades
    if ($content -match 'href="upgrades.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="upgrades.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$upgradeSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons - Business IT Support
    if ($content -match 'href="business-it-support.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="business-it-support.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$businessSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons - Workshop Repairs
    if ($content -match 'href="workshop-repairs.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="workshop-repairs.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$workshopSvg</div>"
        $modified = $true
    }
    
    # Fix empty service icons - Network Setup
    if ($content -match 'href="network-setup.html" class="service-card">\s*<div class="service-icon"></div>') {
        $content = $content -replace '(href="network-setup.html" class="service-card">)\s*<div class="service-icon"></div>', "`$1`n                    <div class=`"service-icon`">$networkSvg</div>"
        $modified = $true
    }
    
    # Add phone number to mobile menu header (after mobile-menu-header close tag if not already there)
    if ($content -match '<div class="mobile-menu-header">' -and $content -notmatch 'mobile-menu-phone') {
        $content = $content -replace '(<button class="mobile-menu-close" id="menuClose">×</button>\s*</div>)', "`$1`n$mobilePhoneHeader"
        $modified = $true
    }
    
    if ($modified) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        Write-Host "Updated: $($file.FullName)"
    }
}

Write-Host "Done!"
