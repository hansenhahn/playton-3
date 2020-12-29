@echo off

md PLAYTON3
cd PLAYTON3
..\ndstool -x "..\5295_-_Professor_Layton_and_the_Lost_Future_EUR_NDS.nds" -9 arm9.bin -7 arm7.bin -y9 y9.bin -y7 y7.bin -d data -y overlay -t banner.bin -h header.bin

