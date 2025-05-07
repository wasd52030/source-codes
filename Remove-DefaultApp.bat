@echo off
if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%~f0' -ArgumentList 'am_admin'"
    exit /b
)

REM remove appx package
set appxList="3d";"alarms";"bing";"Calendar";"camera";"communicationsapps";"Cortana";"Feedback";"help";"maps";"note";"office";"people";"Phone";"Reality";"skype";"solitaire";"soundrecorder";"started";"Tips";"Wallet";"Weather";"xbox";"zune"
for %%a in (%appxList%) do (
    if %%a=="Cortana" (
        REM 確實移除 Cortana（Microsoft.549981C3F5F10）
        powershell "Get-AppxPackage -AllUsers Microsoft.549981C3F5F10 | Remove-AppxPackage -ErrorAction SilentlyContinue; Write-Host Removed: Cortana"
    ) else (
        powershell "Get-AppxPackage *%%a* | Remove-AppxPackage -ErrorAction SilentlyContinue; Write-Host Removed: %%a"
    )
)

echo .
goto OneDrive

REM remove OneDrive
:OneDrive
taskkill /f /im OneDrive.exe
@rem Detect if OS is 32 or 64 bit
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=32BIT || set OS=64BIT

if %OS%==32BIT GOTO 32BIT
if %OS%==64BIT GOTO 64BIT

:32BIT
echo.
echo This is a 32-bit operating system.
echo Removing OneDrive setup files.

%SystemRoot%\System32\OneDriveSetup.exe /uninstall

:64BIT
echo.
echo This is a 64-bit operating system.
echo Removing OneDrive setup files.

%SystemRoot%\SysWOW64\OneDriveSetup.exe /uninstall

pause
