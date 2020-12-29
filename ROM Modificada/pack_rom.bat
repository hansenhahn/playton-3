@echo off

del "5295_-_Professor_Layton_and_the_Lost_Future_BR_NDS.nds"
cd PLAYTON3
..\ndstool -c "..\5295_-_Professor_Layton_and_the_Lost_Future_BR_NDS.nds" -9 arm9.bin -7 arm7.bin -y9 y9.bin -y7 y7.bin -d data -y overlay -t banner.bin -h header.bin
cd ..

