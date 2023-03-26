Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$form = New-Object System.Windows.Forms.Form
$form.Text = '正在前往KNN的路上'
$form.ClientSize = New-Object System.Drawing.Size(400, 300)
[System.Windows.Forms.Application]::EnableVisualStyles() | Out-Null

$rootLayout = New-Object System.Windows.Forms.TableLayoutPanel
$rootLayout.Anchor=[System.Windows.Forms.AnchorStyles]::None
$rootLayout.AutoSize = $true
$rootLayout.Location=New-Object System.Drawing.Point(10,10)
# $rootLayout.CellBorderStyle=[System.Windows.Forms.TableLayoutPanelCellBorderStyle]::Single
$form.Controls.Add($rootLayout)

$btn1 = New-Object System.Windows.Forms.Button
$btn1.name = "btn1"
$btn1.AutoSize = $true
$btn1.Text = "親切問候"
$btn1.Anchor=[System.Windows.Forms.AnchorStyles]::None
$btn1.UseVisualStyleBackColor = $true
$btn1.Add_Click({
        $btn1.Enabled = $false
        Start-ThreadJob -ScriptBlock {
            param($Callback, $progressReporter)

            # Write-Host "Start DLLM"
            $i = 1
            $total = 100
            do {
                Invoke-Command -ScriptBlock $progressReporter -ArgumentList $i, "屌你老母", $i
                Start-Sleep -Milliseconds 100
                $i++
            } while ($i -le $total)
            # Write-Host "End DLLM"

            Invoke-Command -ScriptBlock $Callback -ArgumentList $true
        } -StreamingHost $Host -ArgumentList $TaskEnd, $ReportProgress
    })
$rootLayout.Controls.Add($btn1, 1, 1)


$label1 = New-Object System.Windows.Forms.Label
$label1.AutoSize = $true
$label1.Name = "label1"
$label1.Size = New-Object System.Drawing.Size(50, 20)
$label1.TabIndex = 2
$label1.Anchor=[System.Windows.Forms.AnchorStyles]::None
$label1.Text = "o4o555"
$rootLayout.Controls.Add($label1, 1, 2)

$progressBar1 = New-Object System.Windows.Forms.ProgressBar
$progressBar1.Name = "progressBar1"
$progressBar1.Size = New-Object System.Drawing.Size(250, 29)
$progressBar1.Anchor=[System.Windows.Forms.AnchorStyles]::None
$rootLayout.Controls.Add($progressBar1, 2, 2)

$TaskEnd = {
    param($enable)

    $Form.Invoke(
        {
            $btn1.Enabled = $enable
        }
    )
}
 
$ReportProgress = {
    param($progress, $activity, $status)
    $Form.Invoke({
            $label1.Text = "$activity $status"
            $progressBar1.Value = $progress
        })
        
}

[System.Windows.Forms.Application]::Run($form)

