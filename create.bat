@echo off
if exist App rd /s /q Temp
mkdir Temp
cd Temp
copy ..\lib\index.html index.html
copy ..\lib\skulpt.min.js skulpt.min.js
copy ..\lib\skulpt.min.js skulpt.min.js
copy ..\lib\skulpt-stdlib.js skulpt-stdlib.js
copy ..\lib\jquery.min.js jquery.min.js
copy ..\lib\package.json package.json
..\bin\gen_module.exe "..\src" "..\Temp" "codeskulptor.py"
..\bin\7za.exe a -tzip App.zip *
cd ..
if exist App goto end1
	mkdir App
:end1
copy /b bin\nw.exe+Temp\App.zip App\Run.exe
rd /s /q Temp
cd App
if exist locales goto end2
	mkdir locales
:end2
copy ..\lib\locales\* locales 
copy ..\lib\icudtl.dat icudtl.dat
copy ..\lib\nw.pak nw.pak
copy ..\lib\ffmpegsumo.dll ffmpegsumo.dll
copy ..\lib\libGLESv2.dll libGLESv2.dll
copy ..\lib\libEGL.dll libEGL.dll
echo Done!
pause

