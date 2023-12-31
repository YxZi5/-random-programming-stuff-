Crypter to crypt shellcode saved in binary file, using XOR binary operation.

compilation:

<code>g++.exe crypter.cpp -o crypter.exe</code>

<code>g++.exe decrypt_loader.cpp -o decrypt_loader.exe</code>

Usage:

<code>crypter.exe shellcode.bin <key_in_decimal></code>

<code>decrypt_loader.exe <key_in_decimal></code>
