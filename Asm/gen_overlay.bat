@echo off

REM copy "Originais\arm9_splash.bin" "arm9.bin" /B/Y
REM copy "Originais\overlay_0019.bin" "overlay_0019.bin" /B/Y
REM copy "Originais\overlay_0023.bin" "overlay_0023.bin" /B/Y

rem armips.exe arm9.asm
rem blz.exe -en9 arm9.bin

armips.exe overlay9_0033_novo.asm
blz.exe -en overlay_0033.bin

REM copy "overlay_0002_nocompression.bin" "overlay_0002.bin" /B/Y
REM blz.exe -en overlay_0002.bin

REM copy "arm9.bin" "..\Arquivos Gerais" /B/Y
copy "overlay_0033.bin" "..\Arquivos Gerais" /B/Y