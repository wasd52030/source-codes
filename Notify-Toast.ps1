# 利用 $PSVersionTable 檢查
# 版本限制 -> PSVersion>=5 && PSVersion<7

[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
$Template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText04)

$RawXml = [xml] $Template.GetXml()
# ($RawXml.toast.visual.binding.text | Where-Object { $_.id -eq "1" }).AppendChild($RawXml.CreateTextNode("")) > $null
($RawXml.toast.visual.binding.text | Where-Object { $_.id -eq "2" }).AppendChild($RawXml.CreateTextNode("なんで春日影やったの")) > $null
($RawXml.toast.visual.binding.text | Where-Object { $_.id -eq "3" }).AppendChild($RawXml.CreateTextNode("いいご身分ですわね")) > $null

$SerializedXml = New-Object Windows.Data.Xml.Dom.XmlDocument
$SerializedXml.LoadXml($RawXml.OuterXml)

$Toast = [Windows.UI.Notifications.ToastNotification]::new($SerializedXml)

$Toast.Tag = "PowerShell"
$Toast.Group = "PowerShell"
$Toast.ExpirationTime = [DateTimeOffset]::Now.AddMinutes(1)

$Notifier = [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]::CreateToastNotifier("crychic")
$Notifier.Show($Toast);