function main {

    $excludes = @("*.md")

    if (!(Test-Path './Compressed_for_HW')) {
        mkdir './Compressed_for_HW'
    }

    $a = Get-ChildItem -Directory | Where-Object { $_.BaseName -ne "Compressed_for_HW" }
    for ($i = 0; $i -lt $a.Count; $i++) {
        if ($a[$i].BaseName -as [int]) {
            if ($i -lt 10) {
                Get-ChildItem $a[$i].BaseName -Exclude $excludes | Compress-Archive -Force -DestinationPath "./Compressed_for_HW/hw0$($i+1).zip"
            }
            else {
                Get-ChildItem $a[$i].BaseName -Exclude $excludes | Compress-Archive -Force -DestinationPath "./Compressed_for_HW/hw$($i+1).zip" 
            }
        }else {
            Get-ChildItem $a[$i].BaseName -Exclude $excludes | Compress-Archive -Force -DestinationPath "./Compressed_for_HW/$($a[$i].BaseName).zip" 
        }
    }

    Write-Host "完成！"
    Pause
}

main