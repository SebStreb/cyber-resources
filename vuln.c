#include <stdio.h>
#include <string.h>

void vuln(char* arg) {
    char buffer[256];
    strcpy(buffer, arg);
    printf("%s\n", buffer);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: %s arg", argv[0]);
    }
    vuln(argv[1]);
    return 0;
}
