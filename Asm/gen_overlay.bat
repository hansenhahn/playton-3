@echo off

REM gera arm9 com a tabela de weekly puzzles (precisa de Originais\arm9_splash.bin)
armips.exe arm9.asm
copy "arm9.bin" "..\Arquivos Gerais" /B/Y

REM overlay 0006: weekly puzzles (contadores + getter -> tabela no arm9)
armips.exe overlay_0006_novo.asm
where python >nul 2>nul && (python blz -en overlay_0006.bin) || (blz.exe -en overlay_0006.bin)
copy "overlay_0006.bin" "..\Arquivos Gerais" /B/Y

REM overlay 0033: porta oculta
armips.exe overlay9_0033_novo.asm
where python >nul 2>nul && (python blz -en overlay_0033.bin) || (blz.exe -en overlay_0033.bin)
copy "overlay_0033.bin" "..\Arquivos Gerais" /B/Y
