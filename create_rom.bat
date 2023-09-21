@echo off

echo "Layton's Assembler by DiegoHH"

rem Cria os overlays
cd Asm
call gen_overlay.bat
cd ..

rem Executa os packers de overlay, imagem e texto
cd Programas
call pack_images_en.bat
call pack_text_en.bat
cd ..

rem Copia os arquivos de fonte
copy "Fontes\font_en1.cfnt" "ROM Modificada\PLAYTON3\data\lt3\fnt" /B/Y

copy "Arquivos Gerais\overlay_0033.bin" "ROM Modificada\PLAYTON3\overlay" /B/Y

rem Monta a ROM nova e gera um patch
cd ROM Modificada
call pack_rom.bat
rem call do_patch.bat
cd ..