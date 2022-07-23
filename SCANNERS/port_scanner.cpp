#include <iostream>
#include <arpa/inet.h>
#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

using namespace std;

int main(int argc, char **argv)
{
	// help
	if (argc != 4)
	{
		cout << "Usage: ./port_scanner target_ip num_of_ports" << endl;
		cout << "example: ./port_scanner 127.0.0.1 100 - scan ports 1 - 100 for 127.0.0.1 address" << endl;
	}
	
	char* targetIP = argv[1];
	int endPort = atoi(argv[2]);

	int sock = 0, client_fd, valread;
	// int portNum = 1337;
	struct sockaddr_in serv_addr;
	char buffer[1024] = { 0 };

    serv_addr.sin_family = AF_INET;

    // convert IPv4 or IPv6 addresses to binary format
    if (inet_pton(AF_INET, targetIP, &serv_addr.sin_addr)
        <= 0) {
        printf(
            "\nInvalid address/ Address not supported \n");
        return -1;
    }
    for (int i = 1; i <= endPort; i++)
    {
    	serv_addr.sin_port = htons(i);
    	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Socket creation error \n");
        return -1;
    	}
    	if ((client_fd = connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr))) < 0)
    	{
    		cout << "[-] Port " << i << " is close" << endl;
    	}
    	else
    	{
    		cout << "[+] Port " << i << " is Open" << endl;
    	}
    	close(client_fd);
    }
    return 0;
}