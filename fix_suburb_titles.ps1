$suburbs = @{
    "baulkham-hills" = "Baulkham Hills"
    "bella-vista" = "Bella Vista"
    "carlingford" = "Carlingford"
    "castle-hill" = "Castle Hill"
    "cherrybrook" = "Cherrybrook"
    "dural" = "Dural"
    "glenhaven" = "Glenhaven"
    "glenorie" = "Glenorie"
    "kellyville" = "Kellyville"
    "kenthurst" = "Kenthurst"
    "north-rocks" = "North Rocks"
    "northmead" = "Northmead"
    "norwest" = "Norwest"
    "rouse-hill" = "Rouse Hill"
    "west-pennant-hills" = "West Pennant Hills"
    "winston-hills" = "Winston Hills"
}

foreach ($key in $suburbs.Keys) {
    $filePath = "hills-district\$key.html"
    $suburbName = $suburbs[$key]
    $newTitle = "Computer Repair $suburbName`: Same-Day Local Laptop & PC Fix"
    $newH1 = "Computer Repair $suburbName`: Same-Day Local Laptop & PC Fix"
    
    $content = Get-Content $filePath -Raw -Encoding UTF8
    $content = $content -replace '<title>[^<]*</title>', "<title>$newTitle</title>"
    $content = $content -replace '<h1>[^<]*</h1>', "<h1>$newH1</h1>"
    Set-Content -Path $filePath -Value $content -NoNewline -Encoding UTF8
    Write-Host "Updated: $suburbName"
}
Write-Host "All suburb pages updated!"
