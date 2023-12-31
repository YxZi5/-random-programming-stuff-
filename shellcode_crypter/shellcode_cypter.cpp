#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;


size_t fsize(FILE *f) {
  size_t pos, len;
  pos = ftell(f);
  fseek(f, 0, SEEK_END);
  len = ftell(f);
  fseek(f, pos, SEEK_SET);
  return len;
}

unsigned char* encryptShellcode(unsigned char decryptedShellcode[], int shellcodeLength, unsigned char xorKey) {
  unsigned char* encryptedShellcode = new unsigned char[shellcodeLength];
  
  // Decrypt each hex character using XOR function
  for (int i = 0; i < shellcodeLength; i++) {
    encryptedShellcode[i] = decryptedShellcode[i] ^ xorKey;
  }

  return encryptedShellcode;
}

unsigned char* parse_file(const char* file_path, size_t &len) {
	FILE* f = NULL;
	size_t file_size;

	f = fopen(file_path, "rb");
	if (!f) {
		return NULL;
	}

	file_size = fsize(f);
	len = file_size;

	unsigned char* buffer = new unsigned char[file_size];
	
	fread(buffer, 1, file_size, f);
	// memcpy(buffer, f, file_size);
	fclose(f);

	return buffer;
}

int main(int argc, char **argv) {
	if (argc != 3) {
		cout << "usage: crypter.exe shellcode_path.bin key" << endl;
		return -1;
	}

	int key = atoi(argv[2]);
	size_t shellcode_len;


	unsigned char* shellcode = parse_file(argv[1], shellcode_len);
	// shellcode = (unsigned char)shellcode;
	
	printf("Shellcode lenght: %d\n", shellcode_len);

	printf("Shellcode: ");
	for (size_t i = 0; i < shellcode_len; i++) {
		printf("\\x%02X", shellcode[i]);
	}

	unsigned char* EncryptedShellcode	= encryptShellcode(shellcode, shellcode_len, key);

	printf("\nEncrypted shellcode: ");
	for (int i = 0; i < shellcode_len; i++) {
		cout << "\\x" << hex << (int)EncryptedShellcode[i];
		// printf("\\x%02X", EncryptedShellcode[i]);
	}

	delete EncryptedShellcode;
	delete shellcode;

	return 0;
}