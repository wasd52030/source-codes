@echo off
if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%~f0' -ArgumentList 'am_admin'"
    exit /b
)

set appxList=3d;alarms;bing;Calendar;camera;communicationsapps;Feedback;help;maps;note;office;people;Phone;Reality;skype;solitaire;soundrecorder;started;Tips;Wallet;Weather;xbox;zune

set GetAppx=Get-AppxPackage -AllUsers
set filter=Where-Object { $_.Name -like '*%%a*' }
set RemoveAct=ForEach-Object { Remove-AppxPackage -Package $_.PackageFullName -ErrorAction SilentlyContinue;Write-Host Removed: $($_.Name) }
set RemoveCortana="Get-AppxPackage -AllUsers Microsoft.549981C3F5F10 | ForEach-Object { Remove-AppxPackage -Package $_.PackageFullName -ErrorAction SilentlyContinue; Write-Host ('Removed: Cortana (' + $_.Name + ')') }"
REM 確實移除 Cortana（Microsoft.549981C3F5F10）
powershell -Command %RemoveCortana%
REM 移除其他Default Appx
for %%a in (%appxList%) do ( powershell "%GetAppx% | %filter% | %RemoveAct%" )
echo.
goto RemoveOneDrive


:RemoveOneDrive
taskkill /f /im OneDrive.exe
rem Detect if OS is 32 or 64 bit
rem HKLM -> HKEY_LOCAL_MACHINE
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=32BIT || set OS=64BIT

if %OS%==32BIT GOTO 32BIT
if %OS%==64BIT GOTO 64BIT


:32BIT
echo.
echo This is a 32-bit operating system.
echo Removing OneDrive setup files.
%SystemRoot%\System32\OneDriveSetup.exe /uninstall
goto end


:64BIT
echo.
echo This is a 64-bit operating system.
echo Removing OneDrive setup files.
%SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall
goto end


:end
echo.
echo Remove Default App successfully
pause