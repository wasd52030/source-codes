# 暑假在大雅ㄉ科技廠輪班，最近工作少到已經閒到開始研究powershell scriptㄌ
# 上班時突然冒出用powershell寫QuickSort這個餿主意，於是下班就試著寫看看
# 沒想到還真的能成功，酷欸
# 不知道bash能不能那麼猛

function QuickSort {
    param (
        [array]$arr
    )

    if ($arr.Length -lt 2) {
        return $arr
    }

    $key = $arr[0]
    $arr = $arr[1..$arr.Length]
    $left = $arr | Where-Object { $_ -lt $key } # Where-Object -> 類似其他語言的filter
    $right = $arr | Where-Object { $_ -gt $key } 

    return @(QuickSort($left)) + @($key) + @(QuickSort($right)) | Where-Object { $_ -ne $null }
}


function ArrayPrint {
    param (
        [array]$arr
    )

    for ($i = 0; $i -lt $arr.Length; $i++) {
        if ($i -ne $arr.Length - 1) {
            Write-Host ("{0} " -f $arr[$i]) -NoNewline # Write-Host 預設換行，不換行需加 -NoNewline argument
        }
        else {
            Write-Host ("{0}" -f $arr[$i])
        }
    }
}


function main {
    Write-Host "Before Sort"
    $a = 1..100 | Sort-Object { Get-Random }
    ArrayPrint($a)

    Write-Host "After Sort"
    $b = QuickSort($a)
    ArrayPrint($b)
}

main

