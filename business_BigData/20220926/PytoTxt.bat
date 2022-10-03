@echo off

@REM 從cmd的輸入建立變數，型態為string
set /p input=請輸入這是第幾回作業:
@REM 把剛才的變數轉成數字型態，方便下面比較
set /a ver=%input%

@REM equ 或==：等於
@REM neq：不等於
@REM lss：小於
@REM leq：小於等於
@REM gtr：大於
@REM geq：大於等於
if %ver% lss 10 (
    @REM type: 功能類似於linux的cat
    type main.py > hw0%ver%.txt
) else (
    type main.py > hw%ver%.txt
)
