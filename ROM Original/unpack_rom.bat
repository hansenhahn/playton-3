@echo off

md PLAYTON3_IT
cd PLAYTON3_IT
..\ndstool -x "..\5284 - Professor Layton e il Futuro Perduto, Il (Italy) [b].nds" -9 arm9.bin -7 arm7.bin -y9 y9.bin -y7 y7.bin -d data -y overlay -t banner.bin -h header.bin

