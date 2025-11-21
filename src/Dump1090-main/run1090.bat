@echo off
echo Starting Dump1090...
dump1090.exe --interactive --net --net-ro-port 30002 --net-sbs-port 30003 --net-http-port 8080
pause