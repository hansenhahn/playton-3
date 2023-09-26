@echo Monkeys Traduções

@echo "Calling tl_img.py to unpack background"
pypy tl_img.py -m e0 -s "../ROM Original/PLAYTON3/data/lt3" -s1 "../Arquivos Originais/uk/bg" -d "../Imagens Originais/uk/bg"

REM echo "Calling tl_img.py to unpack animation"
rem pypy tl_img.py -m e1 -s "../ROM Original/PLAYTON3/data/lt3" -d "../Imagens Originais/ani"

pause