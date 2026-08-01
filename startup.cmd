@echo off

echo ===============================
echo Starting WSL
echo ===============================

wsl -d Ubuntu

echo.
echo ===============================
echo Docker Build
echo ===============================

docker compose build

echo.
echo ===============================
echo Docker Up
echo ===============================

docker compose up -d

echo.
echo ===============================
echo Container IP
echo ===============================

for /f %%i in ('docker inspect -f "{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}" xampp') do set IP=%%i

echo.
echo XAMPP IP = %IP%
echo.

start http://%IP%

echo.

docker exec -it xampp bash
