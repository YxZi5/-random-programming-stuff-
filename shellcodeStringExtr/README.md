Tool for extracting string from decompiled shellcode to asm format (decompiler ndisasm.exe).

32-bit example:

1. Decompile compiled binary to assembly format:

<code>ndisasm.exe -b 32 shellcode.bin > assembly.asm</code>

2.extract strings:

<code>python3 extr.py assembly.asm
hex value: 63657878 | after conversion: xxec
hex value: 456e6957 | after conversion: WinE
hex value: 6578652e | after conversion: .exe
hex value: 636c6163 | after conversion: calc
hex value: 73736501 | after conversion: ess
hex value: 636f7250 | after conversion: Proc
hex value: 74697845 | after conversion: Exit</code>
