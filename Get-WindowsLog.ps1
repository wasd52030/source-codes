# 檢查是否已經以 Administrator 身份執行 (Security 需要 Administrator 才能跑)
function Check-Administrator {
    $context = New-Object System.Security.Principal.WindowsPrincipal([System.Security.Principal.WindowsIdentity]::GetCurrent())
    if (-not $context.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)) {
        $scriptPath = $MyInvocation.ScriptName
        $process = New-Object System.Diagnostics.ProcessStartInfo
        $process.FileName = "powershell.exe"
        $process.Arguments = "-File `"$scriptPath`" -type $type"
        $process.Verb = "runas"
        [System.Diagnostics.Process]::Start($process) | Out-Null
        Exit
    }
}


function Get-WindowsLog {
    param (
        [hashtable]$filterHashTable,
        [string]$logType,
        [string]$date
    )

    $taskDisplay = @{
        Name       = "TaskDisplayName";
        Expression = { if ($_.TaskDisplayName) { $_.TaskDisplayName } else { "無" } }
    }

    # reference -> https://learn.microsoft.com/zh-tw/dotnet/api/system.diagnostics.tracing.eventlevel?view=net-8.0#---
    $levelDisplayName = @{
        Name       = "LevelDisplayName";
        Expression = { if ($_.LevelDisplayName) { $_.LevelDisplayName } else { 
                switch ($_.Level) {
                    1 { "錯誤" }
                    2 { "警告" }
                    4 { "資訊" }
                    8 { "成功稽核" }
                }
            } }
    }

    $event = Get-WinEvent -FilterHashtable $filterHashTable | Select-Object -Property Level, $levelDisplayName, TimeCreated, ProviderName, Id, $taskDisplay, Message

    $event | Select-Object -Property * -ExcludeProperty Level  | ConvertTo-Csv -NoTypeInformation | ForEach-Object { ($_ -replace '\"', '') } | Out-File "~\Downloads\$($date)$($logType).csv"
	
    Write-Host "已取得$($logType)紀錄！"
}


Check-Administrator

$types = @('Application', 'Security' , 'System')

$yesterday = (Get-Date).AddDays(-1)
$start = $yesterday.Date
$end = $yesterday.Date.AddHours(23).AddMinutes(59).AddSeconds(59)
$kmtDate = "$($yesterday.Year-1911)$($yesterday.Date.ToString("MMdd"))"

$types | ForEach-Object {
    $filterHashTable = @{ 
        LogName   = $_; 
        StartTime = $start; 
        EndTime   = $end; 
    }
    
    $logNames = @{
        Application = "應用程式"
        Security    = "安全"
        System      = "系統"
    }
    

    Get-WindowsLog -filterHashTable $filterHashTable -logType $logNames[$_] -date $kmtDate
}


Pause