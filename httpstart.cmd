SET PV=python-3.7.9-embed-win32
SET PV=python-3.9.0-embed-win32
echo PV;

%HOMEPATH%\Desktop\%PV%\python.exe -m http.server 80 --bind 192.168.137.1  --directory %HOMEPATH%\Desktop\memo
%HOMEPATH%\Desktop\%PV%\python.exe -m http.server 80 --bind 192.168.11.102 --directory %HOMEPATH%\Desktop\memo
%HOMEPATH%\Desktop\%PV%\python.exe -m http.server 80 --bind 192.168.11.105 --directory %HOMEPATH%\Desktop\memo
%HOMEPATH%\Desktop\%PV%\python.exe -m http.server 80 --bind 192.168.11.108 --directory %HOMEPATH%\Desktop\memo
%HOMEPATH%\Desktop\%PV%\python.exe -m http.server 80 --bind 192.168.1.221 --directory %HOMEPATH%\Desktop\memo
