@echo off

@REM �qcmd����J�إ��ܼơA���A��string
set /p input=�п�J�o�O�ĴX�^�@�~:
@REM ���~���ܼ��ন�Ʀr���A�A��K�U�����
set /a ver=%input%

@REM equ ��==�G����
@REM neq�G������
@REM lss�G�p��
@REM leq�G�p�󵥩�
@REM gtr�G�j��
@REM geq�G�j�󵥩�
if %ver% lss 10 (
    @REM type: �\��������linux��cat
    type main.py > hw0%ver%.txt
) else (
    type main.py > hw%ver%.txt
)
