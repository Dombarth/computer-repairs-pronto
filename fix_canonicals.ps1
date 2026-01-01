$BaseUrl = "https://www.computerrepairspronto.com.au"

function Get-CanonicalUrl {
    param([string]$FilePath)
    $FilePath = $FilePath -replace '\\', '/'
    $FilePath = $FilePath -replace '^\.\/', ''
    if ($FilePath -eq "index.html") { return "$BaseUrl/" }
    elseif ($FilePath -match '/index\.html$') {
        $folder = $FilePath -replace '/index\.html$', ''
        return "$BaseUrl/$folder/"
    }
    else {
        $urlPath = $FilePath -replace '\.html$', ''
        return "$BaseUrl/$urlPath"
    }
}

$htmlFiles = Get-ChildItem -Path . -Filter "*.html" -Recurse | Where-Object { 
    $_.FullName -notmatch '\\\.git\\' -and $_.FullName -notmatch '\\assets\\' -and $_.FullName -notmatch '\\sydney-areas\\'
}

$fixedCount = 0
foreach ($file in $htmlFiles) {
    $relativePath = $file.FullName.Replace((Get-Location).Path + "\", "").Replace("\", "/")
    $correctCanonical = Get-CanonicalUrl -FilePath $relativePath
    $newCanonicalTag = "<link rel=`"canonical`" href=`"$correctCanonical`">"
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    if ($content -match '<link rel="canonical" href="[^"]*">') {
        $currentCanonical = $Matches[0]
        if ($currentCanonical -ne $newCanonicalTag) {
            $newContent = $content -replace '<link rel="canonical" href="[^"]*">', $newCanonicalTag
            Set-Content -Path $file.FullName -Value $newContent -NoNewline -Encoding UTF8
            Write-Host "Fixed: $relativePath"
            $fixedCount++
        }
    }
}
Write-Host "Fixed $fixedCount HTML files"

$sitemapContent = Get-Content "sitemap.xml" -Raw -Encoding UTF8
$sitemapContent = $sitemapContent -replace '(<loc>[^<]*/)index\.html(</loc>)', '$1$2'
$sitemapContent = $sitemapContent -replace '(<loc>[^<]*)\.html(</loc>)', '$1$2'
Set-Content -Path "sitemap.xml" -Value $sitemapContent -NoNewline -Encoding UTF8
Write-Host "Fixed sitemap.xml"
