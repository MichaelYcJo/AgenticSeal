@echo off
rem Windows counterpart to bin/pact-check: cmd.exe/PowerShell resolve a
rem bare `pact-check` to this file via PATHEXT, the same way POSIX
rem shells resolve the extensionless sibling. Kept in lockstep with it.
setlocal
set "here=%~dp0"
set "script=%here%..\skills\verify\scripts\pact_check.py"

set "launch=%here%..\hooks\launch.py"

where /q py
if errorlevel 1 goto usepython
py -3 "%launch%" "%script%" %*
exit /b %errorlevel%

:usepython
python "%launch%" "%script%" %*
exit /b %errorlevel%
