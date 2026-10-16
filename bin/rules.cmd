@echo off
rem Windows counterpart to bin/rules: cmd.exe/PowerShell resolve a bare
rem `rules` to this file via PATHEXT, the same way POSIX shells resolve the
rem extensionless sibling. Kept in lockstep with it.
setlocal
set "here=%~dp0"
set "script=%here%..\.github\scripts\rules.py"

set "launch=%here%..\hooks\launch.py"

where /q py
if errorlevel 1 goto usepython
py -3 "%launch%" "%script%" %*
exit /b %errorlevel%

:usepython
python "%launch%" "%script%" %*
exit /b %errorlevel%
