@echo off

echo "Layton's Assembler by DiegoHH"

rem Executa os packers de overlay, imagem e texto
REM cd Programas
REM call pack_images.bat
REM call pack_texts.bat
REM cd ..

rem Copia os arquivos de fonte
REM copy "Fontes\font.NFTR" "ROM Modificada\DEATHNOTEDS\data\data\font" /B/Y

rem Monta a ROM nova e gera um patch
cd ROM Modificada
call pack_rom.bat
call do_patch.bat
cd ..