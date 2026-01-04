@echo off

echo "Layton's Assembler by DiegoHH"

REM rem Arquivos copiados do espanhol/italiano, ou alterados o original, pelo fato de serem maiores ou terem a paleta de cores modificada
copy "Arquivos Gerais\load_a.cani" "Arquivos Originais\uk\ani\menu\uk\load_a.cani" /B/Y
copy "Arquivos Gerais\save_a.cani" "Arquivos Originais\uk\ani\menu\uk\save_a.cani" /B/Y
copy "Arquivos Gerais\fk_spr.cani" "Arquivos Originais\uk\ani\menu\uk\fk_spr.cani" /B/Y
copy "Arquivos Gerais\quit_btn.cani" "Arquivos Originais\uk\ani\nazo\uk\quit_btn.cani" /B/Y


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