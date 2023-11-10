#include <iostream>
#include <stdio.h>
#include <windows.h>
#include <vector>

using namespace std;

void search_for_rwx(HANDLE process, int pid) {
	SIZE_T pages_info;
	MEMORY_BASIC_INFORMATION p;
	LPVOID addrs = 0;

	int page_exe_readwrite = 0;
	int page_exe = 0;
	int page_exe_read = 0;
	int page_exe_writecopy = 0;

	while (pages_info = VirtualQueryEx(process, addrs, &p, sizeof(p))) {
		if (pages_info == 0) {
			cout << "error at reading information from process";
			exit(0);
		}

		addrs = (LPVOID)((DWORD_PTR)p.BaseAddress + p.RegionSize);

		DWORD protect = p.AllocationProtect;
		if (protect == PAGE_EXECUTE_READWRITE) {
			printf("[+] PAGE_EXECUTE_READWRITE memory page found from 0x%x to 0x%x | PID: %i\n", p.BaseAddress, addrs, pid);
			page_exe_readwrite += 1;
		}
		else if (protect == PAGE_EXECUTE) {
			printf("[+] PAGE_EXECUTE memory page found from 0x%x to 0x%x | PID: %i\n", p.BaseAddress, addrs, pid);
			page_exe += 1;
		}
		else if (protect == PAGE_EXECUTE_READ) {
			printf("[+] PAGE_EXECUTE_READ memory page found from 0x%x to 0x%x | PID: %i\n", p.BaseAddress, addrs, pid);
			page_exe_read += 1;
		}
		else if (protect == PAGE_EXECUTE_WRITECOPY) {
			printf("[+] PAGE_EXECUTE_WRITECOPY memory page found from 0x%x to 0x%x | PID: %i\n", p.BaseAddress, addrs, pid);
			page_exe_writecopy += 1;
		}
	}

	printf("\n");
	printf("PAGE_EXECUTE_READWRITE: %i\n", page_exe_readwrite);
	printf("PAGE_EXECUTE: %i\n", page_exe);
	printf("PAGE_EXECUTE_READ: %i\n", page_exe_read);
	printf("PAGE_EXECUTE_WRITECOPY: %i\n", page_exe_writecopy);

}

vector<string> scan_for_strings(HANDLE process) {
	vector<string> result;

	SYSTEM_INFO sysInfo;
	GetSystemInfo(&sysInfo);

	MEMORY_BASIC_INFORMATION p;
	LPBYTE address = 0;

	while (address < sysInfo.lpMaximumApplicationAddress) {
		SIZE_T proc_info = VirtualQueryEx(process,
			address,
			&p,
			sizeof(p)
		);
		
		if (proc_info == 0) {
			printf("error at qering information about process");
			return result;
		}

		if (p.State == MEM_COMMIT && (p.Type == MEM_MAPPED || p.Type == MEM_PRIVATE)) {
			vector<char> buffer(p.RegionSize);
			SIZE_T bytesRead;

			bool read_data = ReadProcessMemory(process,
				address,
				&buffer[0],
				p.RegionSize,
				&bytesRead
			);
			if (read_data == 0) {
				printf("error at reading data from process memory");
				return result;
			}

			string current_string;
			for (SIZE_T i = 0; i < bytesRead; ++i) {
				if (buffer[i] > 32 && buffer[i] <= 126) {
					current_string += buffer[i];
				}

				if (buffer[i] == 32) {
					result.push_back(current_string);
					current_string = "";
				}

			}

		}

		address += p.RegionSize;
	}
	return result;
}

int main(int argc, char* argv[]) {
	if (argc != 3) {
		printf("usage: memory_scanner.exe pid 1 / 2\n");
		printf("1 - check for memory pages with executable priviliges\n2 - dump strings from memory\n");
		return -1;
	}

	int pid = atoi(argv[1]);
	int option = atoi(argv[2]);
	HANDLE ph;

	if (option == 1) {
		ph = OpenProcess(MAXIMUM_ALLOWED,
			false,
			pid
		);
		if (ph == NULL) {
			printf("error at openning handle to process");
			return -2;
		}

		search_for_rwx(ph, pid);
	}
	else {
		auto strings = scan_for_strings(ph);
		if ( strings.size() <= 0 ) {
			return -1;
		}

		for (size_t i = 0; i < strings.size(); ++i) {
			cout << strings[i] << endl;
		}
	}

	return 0;
}