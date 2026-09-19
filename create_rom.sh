#!/bin/bash
set -e
echo "Layton's Assembler by DiegoHH (Linux)"
# feature flags: 0 = use original (debug), 1 = pack translated
ENABLE_OVERLAY_COMPRESSION="${ENABLE_OVERLAY_COMPRESSION:-0}"
ENABLE_IMAGES="${ENABLE_IMAGES:-1}"
ENABLE_TEXT="${ENABLE_TEXT:-1}"
ENABLE_SPLASH="${ENABLE_SPLASH:-1}"
export ENABLE_OVERLAY_COMPRESSION ENABLE_IMAGES ENABLE_TEXT ENABLE_SPLASH
echo "Overlay: $ENABLE_OVERLAY_COMPRESSION Images: $ENABLE_IMAGES Text: $ENABLE_TEXT Splash: $ENABLE_SPLASH"
# clean build: always start from original (idea do script é montagem clean)
echo "Restoring ROM Modificada from ROM Original (clean)"
rm -rf "ROM Modificada/PLAYTON3"
cp -a "ROM Original/PLAYTON3" "ROM Modificada/PLAYTON3"
# auto-use venv if present (no need to source manually)
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    echo "venv activated: $(python --version)"
elif [ -f "venv/bin/python" ]; then
    export PATH="$PWD/venv/bin:$PATH"
fi
# fallback python
PYTHON="${PYTHON:-$(command -v python3 2>/dev/null || command -v python)}"
export PYTHON
echo "Using $PYTHON"

# Arquivos copiados do espanhol/italiano (só se imagens)
if [ "$ENABLE_IMAGES" = "1" ]; then
    cp -f "Arquivos Gerais/load_a.cani" "Arquivos Originais/uk/ani/menu/uk/load_a.cani" 2>/dev/null || true
    cp -f "Arquivos Gerais/save_a.cani" "Arquivos Originais/uk/ani/menu/uk/save_a.cani" 2>/dev/null || true
    cp -f "Arquivos Gerais/fk_spr.cani" "Arquivos Originais/uk/ani/menu/uk/fk_spr.cani" 2>/dev/null || true
    cp -f "Arquivos Gerais/quit_btn.cani" "Arquivos Originais/uk/ani/nazo/uk/quit_btn.cani" 2>/dev/null || true
else
    echo "Arquivos Gerais copy disabled (ENABLE_IMAGES=0)"
fi

# Gera e aplica a splash no arm9 (patch do entry point)
if [ "$ENABLE_SPLASH" = "1" ]; then
    echo "Building splash (arm9)..."
    bash Splash/make_splash.sh
    cp -f "Splash/arm9_splash.bin" "ROM Modificada/PLAYTON3/arm9.bin"
    cp -f "Splash/arm9_splash.bin" "Asm/Originais/arm9_splash.bin"
else
    echo "Splash disabled (ENABLE_SPLASH=0)"
    cp -f "ROM Original/PLAYTON3/arm9.bin" "Asm/Originais/arm9_splash.bin"
fi

# Cria os overlays
cd Asm
bash gen_overlay.sh
cd ..

# Executa os packers de overlay, imagem e texto (usando Python3)
cd Programas
if [ "$ENABLE_IMAGES" = "1" ]; then
    bash pack_images_en.sh
else
    echo "Images packing disabled (ENABLE_IMAGES=0) - restoring original"
    cp -rf "../ROM Original/PLAYTON3/data/lt3/bg" "../ROM Modificada/PLAYTON3/data/lt3/" 2>/dev/null || true
    cp -rf "../ROM Original/PLAYTON3/data/lt3/ani" "../ROM Modificada/PLAYTON3/data/lt3/" 2>/dev/null || true
    cp -rf "../ROM Original/PLAYTON3/data/lt3/btl" "../ROM Modificada/PLAYTON3/data/lt3/" 2>/dev/null || true
fi
cd ..
if [ "$ENABLE_TEXT" = "1" ]; then
    cd Programas3
    bash pack_text_en.sh
    cd ..
else
    echo "Text packing disabled (ENABLE_TEXT=0) - restoring original"
    cp -rf "../ROM Original/PLAYTON3/data/lt3/txt" "../ROM Modificada/PLAYTON3/data/lt3/" 2>/dev/null || true
    cp -rf "../ROM Original/PLAYTON3/data/lt3/rc" "../ROM Modificada/PLAYTON3/data/lt3/" 2>/dev/null || true
fi

# Copia fonte só se texto, overlay só se overlay
if [ "$ENABLE_TEXT" = "1" ]; then
    echo "Copying translated font"
    cp -f "Fontes/font_en1.cfnt" "ROM Modificada/PLAYTON3/data/lt3/fnt/" 2>/dev/null || true
else
    echo "Font copy disabled (ENABLE_TEXT=0)"
fi
if [ "$ENABLE_OVERLAY_COMPRESSION" = "1" ]; then
    echo "Copying patched arm9 + overlays"
    cp -f "Arquivos Gerais/arm9.bin" "ROM Modificada/PLAYTON3/arm9.bin" 2>/dev/null || true
    cp -f "Arquivos Gerais/overlay_0006.bin" "ROM Modificada/PLAYTON3/overlay/" 2>/dev/null || true
    cp -f "Arquivos Gerais/overlay_0033.bin" "ROM Modificada/PLAYTON3/overlay/" 2>/dev/null || true
else
    echo "Overlay copy disabled (ENABLE_OVERLAY_COMPRESSION=0)"
fi

# Ajusta o y9 para o tamanho comprimido real dos overlays (o recomprimido muda de tamanho)
"${PYTHON:-python3}" "Asm/fix_y9.py" "ROM Modificada/PLAYTON3/y9.bin" "ROM Modificada/PLAYTON3/overlay" 2>/dev/null || true

# Monta a ROM nova e gera um patch
cd ROM\ Modificada
bash pack_rom.sh
bash do_patch.sh
cd ..
