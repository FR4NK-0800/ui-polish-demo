@echo off
cd /d "%~dp0"
start /MIN "" python server.py 3000
echo Server started at http://localhost:3000
echo.
