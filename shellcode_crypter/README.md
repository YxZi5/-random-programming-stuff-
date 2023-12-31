Shellcode crypter program to crypt shellcode, shellcode in binary format saved in file, using XOR binary operation.

compilation:

<code>g++.exe crypter.cpp -o crypter.exe</code>

<code>g++.exe decrypt_loader.cpp -o decrypt_loader.exe</code>

Usage:

<code>crypter.exe shellcode.bin <key_in_decimal></code>

<code>decrypt_loader.exe <key_in_decimal></code>
