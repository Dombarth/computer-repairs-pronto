# Update all HTML files except castle-hill.html
Get-ChildItem -Path . -Filter *.html -Recurse | Where-Object { $_.Name -ne 'castle-hill.html' } | ForEach-Object {
    $content = Get-Content $_.FullName -Raw -Encoding UTF8
    $content = $content -replace 'Workshop in Castle Hill', 'Workshop near Castle Hill'
    $content = $content -replace 'workshop in Castle Hill', 'workshop near Castle Hill'
    $content = $content -replace 'based in Castle Hill', 'based near Castle Hill'
    $content = $content -replace 'repairs in Castle Hill', 'repairs near Castle Hill'
    Set-Content -Path $_.FullName -Value $content -Encoding UTF8 -NoNewline
    Write-Host "Updated: $($_.FullName)"
}

# Update suburb page titles
$suburbs = @{
    'baulkham-hills.html' = 'Baulkham Hills'
    'bella-vista.html' = 'Bella Vista'
    'carlingford.html' = 'Carlingford'
    'cherrybrook.html' = 'Cherrybrook'
    'dural.html' = 'Dural'
    'glenhaven.html' = 'Glenhaven'
    'glenorie.html' = 'Glenorie'
    'kellyville.html' = 'Kellyville'
    'kenthurst.html' = 'Kenthurst'
    'north-rocks.html' = 'North Rocks'
    'northmead.html' = 'Northmead'
    'norwest.html' = 'Norwest'
    'rouse-hill.html' = 'Rouse Hill'
    'west-pennant-hills.html' = 'West Pennant Hills'
    'winston-hills.html' = 'Winston Hills'
}

foreach ($file in $suburbs.Keys) {
    $filepath = "hills-district\$file"
    if (Test-Path $filepath) {
        $content = Get-Content $filepath -Raw -Encoding UTF8
        $suburb = $suburbs[$file]
        $oldTitle = "<title>Computer Repair Help in $suburb | Local Service</title>"
        $newTitle = "<title>Computer Repair Help in $suburb`: Local Workshop Support</title>"
        $content = $content -replace [regex]::Escape($oldTitle), $newTitle
        Set-Content -Path $filepath -Value $content -Encoding UTF8 -NoNewline
        Write-Host "Updated title: $filepath"
    }
}

Write-Host "Done!"
