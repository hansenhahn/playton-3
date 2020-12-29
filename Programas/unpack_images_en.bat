@echo Monkeys Traduções

@echo "Calling tl_img.py to unpack background"
pypy tl_img.py -m e0 -s "../ROM Original/PLAYTON3/data/lt3/mini" -d "../Imagens Originais/bg/mini"
rem pypy tl_img.py -m e0 -s "../ROM Original/PLAYTON3/data/lt3/nazo" -d "../Imagens Originais/bg/nazo"
rem pypy tl_img.py -m e0 -s "../ROM Original/PLAYTON3/data/lt3/img" -d "../Imagens Originais/bg/img"


REM echo "Calling tl_img.py to unpack animation"
REM python tl_img.py -m e1 -s "../ROM Original/PLAYTON3/data/lt3" -d "../Imagens Originais"

pause