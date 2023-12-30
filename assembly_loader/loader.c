#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <windows.h>

size_t fsize(FILE *f) {
  size_t pos, len;
  pos = ftell(f);
  fseek(f, 0, SEEK_END);
  len = ftell(f);
  fseek(f, pos, SEEK_SET);
  return len;
}

void* Loadbinary(const char* file_path) {
	FILE* f = NULL;
	void *code = NULL;
	size_t file_size;

	f = fopen(file_path, "rb");
	if (!f) {
		printf("error: openning file");
		return NULL;
	}

	file_size = fsize(f);

	void* buffer = malloc(file_size);
	if (!buffer) {
		printf("error: allocation memory 1");
		fclose(f);
		return NULL;
	}

	fread(buffer, 1, file_size, f);
	fclose(f);

	void* exec_mem = VirtualAlloc(NULL,
		file_size,
		MEM_COMMIT | MEM_RESERVE,
		PAGE_EXECUTE_READWRITE
		);
	if (exec_mem == NULL) {
		printf("error: allocation memory pages");
		free(buffer);
		return NULL;
	}

	memcpy(exec_mem, buffer, file_size);
	free(buffer);

	return exec_mem;
}

int main(int argc, char **argv) {
	const char* path;
	void *data;

	puts("ASM / embedded code Loader - https://0xyxzi.ct8.pl/");

	if (argc != 2) {
		printf("usage: loader.exe file.bin");
		return -1;
	}

	path = argv[1];

	void* shellcode_address = Loadbinary(path);
	if (shellcode_address == NULL) {
		printf("error: loading binary into memory");
		return -1;
	}

	printf("Binary loaded at address: %p\n", shellcode_address);

	void(*func)() = (void(*)())shellcode_address;
	func();

	printf("Press ENTER to close program\n");
	char c = getchar();

	VirtualFree(shellcode_address, 0, MEM_RELEASE);

	return 0;
}