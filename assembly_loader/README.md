Simple program which load compiled assembly code without any haders (clean assembly) into memory of itself memory space by allocating new pages of memory using WinAPI function VirtualAlloc()

Compilation:
<code>gcc.exe loader.c -o loader.exe</code>

Usage:
<code>loader.exe code.bin</code>

Example code (hex view):
<code>
00000000  31 c0 64 a1 30 00 00 00  8b 40 0c 8b 40 14 8b 00  |1.d.0....@..@...|
00000010  8b 00 8b 40 10 89 45 fc  8b 58 3c 01 c3 8b 5b 78  |...@..E..X<...[x|
00000020  01 c3 8b 7b 20 01 c7 89  7d f8 8b 4b 24 01 c1 89  |...{ ...}..K$...|
00000030  4d f4 8b 53 1c 01 c2 89  55 f0 8b 53 14 89 55 ec  |M..S....U..S..U.|
00000040  eb 32 31 c0 8b 55 ec 8b  7d f8 8b 75 18 31 c9 fc  |.21..U..}..u.1..|
00000050  8b 3c 87 03 7d fc 66 83  c1 08 f3 a6 74 05 40 39  |.<..}.f.....t.@9|
00000060  d0 72 e4 8b 4d f4 8b 55  f0 66 8b 04 41 8b 04 82  |.r..M..U.f..A...|
00000070  03 45 fc c3 ba 78 78 65  63 c1 ea 08 52 68 57 69
</code>
