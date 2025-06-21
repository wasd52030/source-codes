# reference -> https://stackoverflow.com/questions/13974676/why-does-powershell-think-im-trying-to-return-an-object-rather-then-a-datatab
function Get-MSSQL(){
    # 設定連線字串
    $server = "localhost,1401"            # SQL Server 伺服器名稱
    $database = "pubs"   # 資料庫名稱
    $user = "sa"           # SQL 登入帳號
    $password = "!Password"       # SQL 密碼

    # 建立連線字串
    $connectionString = "Server=$server;Database=$database;User ID=$user;Password=$password;Trusted_Connection=False;"

    # 載入 SQLClient
    Add-Type -AssemblyName System.Data

    # 建立 SQL 連線
    $connection = New-Object System.Data.SqlClient.SqlConnection
    $connection.ConnectionString = $connectionString
    

    # 將查詢結果填入 DataTable
    try {
        $connection.Open()

        $query="SELECT * FROM [pubs].[dbo].[employee]"
        $adapter = New-Object System.Data.SqlClient.SqlDataAdapter ($query, $connection)
        $dataTable = New-Object System.Data.DataTable

        $adapter.Fill($dataTable) | Out-Null  # 避免輸出數字行數
    }
    catch {
        Write-Error "發生錯誤：$($_.Exception.Message)"
    }
    finally {
        $connection.Close()
    }

    return , $dataTable
}


$db = Get-MSSQL
$db | Format-Table -AutoSize

# 依據資料庫實際欄位取值
foreach($row in $db.Rows){
    Write-Host $row["emp_id"], $row["fname"], $row["lname"], $row["job_id"], $row["job_lvl"], $row["pub_id"], $row["hire_date"]
}