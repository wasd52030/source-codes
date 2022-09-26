# 暑假在大雅ㄉ科技廠輪班，最近工作少到已經閒到開始研究powershell scriptㄌ
# 上班時突然冒出用powershell寫QuickSort這個餿主意，於是下班就試著寫看看
# 沒想到真的能寫得出來，酷欸
# 不知道bash能不能那麼猛

function QuickSort([array]$arr) {
    if ($arr.Length -lt 2) {
        return $arr
    }

    $key = $arr[0]
    $arr = $arr[1..$arr.Length]
    $left = $arr | Where-Object { $_ -le $key } # Where-Object -> 類似其他語言的filter
    $right = $arr | Where-Object { $_ -gt $key } 

    return @(QuickSort($left)) + @($key) + @(QuickSort($right)) | Where-Object { $_ -ne $null }
}


function ArrayPrint ([array]$arr) {
    for ($i = 0; $i -lt $arr.Length; $i++) {
        if ($i -ne $arr.Length - 1) {
            Write-Host ("{0} " -f $arr[$i]) -NoNewline # Write-Host 預設換行，不換行需加 -NoNewline argument
        }
        else {
            Write-Host ("{0}" -f $arr[$i])
        }
    }
}


function getRandomArray($min, $max, $len) {
    $res = @()
    for ($i = 0; $i -lt $len; $i++) {
        $res += @(Get-Random -Minimum $min -Maximum $max)
    }
    return $res
}


function main {
    Write-Host "Before Sort"
    # Powershell函數多參數的坑: https://blog.darkthread.net/blog/ps-func-param-syntax/
    $a = getRandomArray 0 1000 1000
    ArrayPrint($a)

    Write-Host "After Sort"
    ArrayPrint(QuickSort $a)
}

main

