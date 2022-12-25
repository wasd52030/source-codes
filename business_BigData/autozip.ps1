function main {

    $excludes = @("*.md")

    if (!(Test-Path './HW_Compressed')) {
        mkdir './HW_Compressed'
    }

    $a = Get-ChildItem -Directory | Sort-Object CreationTime | Where-Object { $_.BaseName -ne "HW_Compressed" }
    for ($i = 0; $i -lt $a.Count; $i++) {
        # 平常的作業皆以教授出作業當天日期(YYYYMMDD)命名，以便跟期中期末區隔
        if ($a[$i].BaseName -as [int]) {
            if ($i -lt 10) {
                Get-ChildItem $a[$i].BaseName -Exclude $excludes | Compress-Archive -Force -DestinationPath "./HW_Compressed/hw0$($i+1).zip"
            }
            else {
                Get-ChildItem $a[$i].BaseName -Exclude $excludes | Compress-Archive -Force -DestinationPath "./HW_Compressed/hw$($i+1).zip" 
            }
        }
        else {
            if ($i -lt 10) {
                Get-ChildItem $a[$i].BaseName -Exclude $excludes | Compress-Archive -Force -DestinationPath "./HW_Compressed/hw0$($i+1)_$($a[$i].BaseName).zip"
            }
            else {
                Get-ChildItem $a[$i].BaseName -Exclude $excludes | Compress-Archive -Force -DestinationPath "./HW_Compressed/hw$($i+1)_$($a[$i].BaseName).zip" 
            }
        }
        
    }

    Write-Host "完成！"
    Pause
}

main