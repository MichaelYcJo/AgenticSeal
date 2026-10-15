@echo off
rem Windows counterpart to bin/payload-meter: cmd.exe/PowerShell resolve a bare
rem `payload-meter` to this file via PATHEXT, the same way POSIX shells resolve
rem the extensionless sibling. Kept in lockstep with it.
setlocal
set "here=%~dp0"
set "script=%here%..\skills\verify\scripts\payload_meter.py"

set "launch=%here%..\hooks\launch.py"

where /q py
if errorlevel 1 goto usepython
py -3 "%launch%" "%script%" %*
exit /b %errorlevel%

:usepython
python "%launch%" "%script%" %*
exit /b %errorlevel%
