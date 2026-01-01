# Generate sitemap.xml for Computer Repairs Pronto
# Run this script to automatically generate/update the sitemap based on all HTML files

$baseUrl = "https://www.computerrepairspronto.com.au"
$today = Get-Date -Format "yyyy-MM-dd"

# Start XML content
$xml = @"
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"@

# Get all HTML files, excluding hidden folders
$htmlFiles = Get-ChildItem -Path "." -Filter "*.html" -Recurse | Where-Object { $_.FullName -notlike "*\.git*" }

foreach ($file in $htmlFiles) {
    # Get relative path from current directory
    $relativePath = $file.FullName.Replace((Get-Location).Path + "\", "").Replace("\", "/")
    
    # Build the URL
    if ($relativePath -eq "index.html") {
        $url = $baseUrl + "/"
    } else {
        $url = $baseUrl + "/" + $relativePath
    }
    
    # Determine priority based on file location
    $priority = "0.5"
    if ($relativePath -eq "index.html") {
        $priority = "1.0"
    } elseif ($relativePath -like "services/index.html" -or $relativePath -like "hills-district/index.html") {
        $priority = "0.9"
    } elseif ($relativePath -match "^services/[^/]+\.html$" -or $relativePath -eq "contact.html" -or $relativePath -eq "about.html") {
        $priority = "0.8"
    } elseif ($relativePath -match "^hills-district/[^/]+\.html$") {
        $priority = "0.7"
    } elseif ($relativePath -match "^services/[^/]+/[^/]+\.html$") {
        $priority = "0.6"
    }
    
    # Determine change frequency
    $changefreq = "monthly"
    if ($relativePath -eq "index.html") {
        $changefreq = "weekly"
    } elseif ($relativePath -like "services/*" -or $relativePath -like "hills-district/*") {
        $changefreq = "monthly"
    }
    
    # Add URL entry
    $xml += @"

  <url>
    <loc>$url</loc>
    <lastmod>$today</lastmod>
    <changefreq>$changefreq</changefreq>
    <priority>$priority</priority>
  </url>
"@
}

# Close XML
$xml += @"

</urlset>
"@

# Write to file
$xml | Out-File -FilePath "sitemap.xml" -Encoding UTF8

# Count URLs
$urlCount = ($htmlFiles | Measure-Object).Count
Write-Host "Sitemap generated successfully with $urlCount URLs"
Write-Host "File saved: sitemap.xml"
