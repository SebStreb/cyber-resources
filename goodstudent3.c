#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define SIZE 32

void yes() {
    printf("Yes you are!\n");
}

void no() {
    printf("Not yet...\n");
}

int check() {
    char buffer[SIZE];
    gets(buffer);
    return strcasecmp(buffer, "Of course!\n");
}

int main(int argc, char* argv[]) {
    printf("Are you a good student?\n> ");

    if (check() == 0) {
        yes();
    } else {
        no();
    }

    return 0;
}
