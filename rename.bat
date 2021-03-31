@echo off
setlocal enabledelayedexpansion
set count=10000
for /f "delims=" %%i in ('dir /b *.jpg,*.png,*.bmp,*.jpeg,*.gif') do call:Rename "%%~i"
pause
exit
 
:Rename
set /a count+=1
if /i "%~1"=="!count:~1!%~x1" goto :eof
if exist "!count:~1!%~x1" goto Rename
echo 改名：%1 !count:~1!
ren "%~1" "!count:~1!%~x1"
goto :eof
