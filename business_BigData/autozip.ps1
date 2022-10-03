function main {
    if (!(Test-Path './Compressed_for_HW')) {
        mkdir './Compressed_for_HW'
    }

    #這裡會以能不能轉int為filter的條件是因為每週作業的資料夾皆以當天日期(YYYYMMDD)為名，剛好可以濾掉存壓縮檔的資料夾Compressed_for_HW
    $a = Get-ChildItem -Directory | Where-Object { $_.BaseName -as [int] }
    for ($i = 0; $i -lt $a.Count; $i++) {
        if ($i -lt 10) {
            zip.exe "./Compressed_for_HW/hw0$($i+1).zip" "$($a[$i].BaseName)/*"
        }
        else {
            zip.exe "./Compressed_for_HW/hw$($i+1).zip" "$($a[$i].BaseName)/*"
        }
    }

    Write-Host "完成！"
}

main