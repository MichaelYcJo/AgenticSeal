@echo off
rem Windows counterpart to bin/iadd: cmd.exe/PowerShell resolve a bare `iadd`
rem to this file via PATHEXT, the same way POSIX shells resolve the
rem extensionless sibling. Kept in lockstep with it.
setlocal
set "here=%~dp0"
set "script=%here%..\skills\implement\scripts\iadd.py"

set "launch=%here%..\lib\launch.py"

where /q py
if errorlevel 1 goto usepython
py -3 "%launch%" "%script%" %*
exit /b %errorlevel%

:usepython
python "%launch%" "%script%" %*
exit /b %errorlevel%
