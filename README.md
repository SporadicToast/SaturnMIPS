# SaturnMIPS
CS21 - UPD, Project 2 encoder
# 

![Untitled](https://i.imgur.com/2480Ulw.png)

### Saturn MIPS

- Saturn MIPS is a encoder that allows the input of instructions, registers, immediates and commands and converts it to machine code.

![Untitled](https://i.imgur.com/6UhJ1XY.png)

- Input the relevant details into the command line and it outputs it to two places, out.txt for machine code, out_eng.txt for “kinda” human readable MIPS.
- Limitations:
    - Jumps and Branches must be computed, for jumps, just get the line number (1 indexed) and it automatically changes it to MIPS machine code equivalent
    - Branches are computed normally (PC+4 offsets).
    - Clear your own text files, literal do-it-yourself solution.
    - Spaghetti code.
- Usage:
    - Run `run.bat` or run via `python SaturnMIPS.py` *OR*
    - Download the [release](https://github.com/SporadicToast/SaturnMIPS/releases/tag/RC) and **SaturnMIPS.exe**
    - Input instruction, register(s), immediates (in decimal only sorry).
    - Look at `out.txt` for machine code and `out_eng.txt` for human readable code.
    - Make sure you clean that text file after because my program DOES NOT do it for you lmao.
