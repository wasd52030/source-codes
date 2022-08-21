# 暑假在大雅ㄉ科技廠輪班，最近工作少到已經閒到開始研究powershell scriptㄌ
# 上班時突然冒出用powershell寫QuickSort這個餿主意，於是下班就試著寫看看
# 沒想到還真的能成功，酷欸
# 不知道bash能不能那麼猛

function QuickSort {
    param (
        [Int64[]]$arr
    )

    if ($arr.Length -lt 2) {
        return $arr
    }

    $key = $arr[0]
    $left = @()
    $right = @()
    $res = @()

    for ($i = 1; $i -lt $arr.Length; $i++) {
        if ($arr[$i] -le $key) {
            $left += $arr[$i]
        }
        else {
            $right += $arr[$i]
        }
    }

    $res += QuickSort($left)
    $res += $key
    $res += QuickSort($right)

    return $res
}

Write-Host "Before Sort"
$a = 1..1000 | Sort-Object { Get-Random }
foreach ($i in $a) { Write-Host "$i " -NoNewline } # Write-Host 預設換行，不換行需加 -NoNewline argument

Write-Host "`n" # powershell的escape char以「`」開頭

Write-Host "After Sort"
$b=QuickSort($a)
foreach ($i in $b) { Write-Host "$i " -NoNewline }
