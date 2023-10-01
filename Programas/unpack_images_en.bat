@echo Monkeys Traduções

REM @echo "Calling tl_img.py to unpack background"
REM pypy tl_img.py -m e0 -s "../ROM Original/PLAYTON3/data/lt3" -s1 "../Arquivos Originais/uk/bg" -d "../Imagens Originais/uk/bg"

echo "Calling tl_img.py to unpack animation"
pypy tl_img.py -m e1 -s "../ROM Original/PLAYTON3/data/lt3" -s1 "../Arquivos Originais/uk/ani" -d "../Imagens Originais/uk/ani"

pause