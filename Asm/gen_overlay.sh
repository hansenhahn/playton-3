#!/bin/bash
set -e
cd "$(dirname "$0")"
ENABLE_OVERLAY_COMPRESSION="${ENABLE_OVERLAY_COMPRESSION:-0}"

run_armips() {
    local asm="$1"
    if [ -x ./armips ]; then
        ./armips "$asm"
    elif command -v armips >/dev/null 2>&1; then
        armips "$asm"
    else
        wine armips.exe "$asm" 2>/dev/null || echo "armips not found, skipping"
    fi
}

run_blz() {
    local f="$1"
    if [ -x ./blz ]; then
        ./blz -en "$f"
    elif [ -f ./blz ] && command -v python3 >/dev/null 2>&1; then
        python3 ./blz -en "$f"
    elif command -v blz >/dev/null 2>&1; then
        blz -en "$f"
    else
        wine blz.exe -en "$f" 2>/dev/null || echo "blz not found, skipping"
    fi
}

if [ "$ENABLE_OVERLAY_COMPRESSION" = "0" ]; then
    echo "Overlay compression disabled (ENABLE_OVERLAY_COMPRESSION=0) - using original"
    if [ -f "Originais/overlay9_0033.bin" ]; then
        cp -f "Originais/overlay9_0033.bin" "overlay_0033.bin"
    elif [ -f "Originais/overlay_0033.bin" ]; then
        cp -f "Originais/overlay_0033.bin" "overlay_0033.bin"
    fi
    cp -f "overlay_0033.bin" "../Arquivos Gerais/overlay_0033.bin" 2>/dev/null || true
    echo "overlay 0033 original restored"
    exit 0
fi

# arm9: tabela de weekly puzzles sobre as strings de build do SDK
if [ -f "Originais/arm9_splash.bin" ]; then
    run_armips arm9.asm
    cp -f "arm9.bin" "../Arquivos Gerais/arm9.bin"
    echo "arm9 built (weekly table @ 0x02000BC5)"
else
    echo "AVISO: Originais/arm9_splash.bin ausente - arm9 nao patchado"
fi

# overlay 0006: getter dos weekly puzzles
run_armips overlay_0006_novo.asm
run_blz "overlay_0006.bin"
cp -f "overlay_0006.bin" "../Arquivos Gerais/overlay_0006.bin"
echo "overlay 0006 built"

# overlay 0033: porta oculta
sed 's/\\/\//g' overlay9_0033_novo.asm > overlay9_0033_novo_linux.asm
run_armips overlay9_0033_novo_linux.asm
run_blz "overlay_0033.bin"
cp -f "overlay_0033.bin" "../Arquivos Gerais/overlay_0033.bin"
echo "overlay 0033 built"

echo "overlays built"
