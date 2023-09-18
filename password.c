#include "stdio.h"
#include "string.h"

int check_password(char* password) {
    int checked = 0;
    char password_buffer[16];

    strcpy(password_buffer, password);

    if (strcmp(password_buffer, "good") == 0) {
        checked = 1;
    }

    return checked;
}

int main(int argc, char* argv[]) {
    if (argc != 2) { 
        printf("missing argument\n"); 
        return 1; 
    }

    if (check_password(argv[1])) {
        printf("access granted\n");
    } else {
        printf("Bad password!\n");
    }

    return 0;
}