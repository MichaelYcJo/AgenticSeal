@echo off
rem Windows counterpart to bin/fold-check: cmd.exe/PowerShell resolve a bare
rem `fold-check` to this file via PATHEXT, the same way POSIX shells resolve
rem the extensionless sibling. Kept in lockstep with it.
setlocal
set "here=%~dp0"
set "script=%here%..\skills\settle\scripts\fold_check.py"

set "launch=%here%..\hooks\launch.py"

where /q py
if errorlevel 1 goto usepython
py -3 "%launch%" "%script%" %*
exit /b %errorlevel%

:usepython
python "%launch%" "%script%" %*
exit /b %errorlevel%
