#include <stdio.h>

void func(char *str) {
  int i;
  char buf[28];
  for (i=0;i<=28;i++) {
    buf[i] = str[i];
  }
}

int main(int argc, char **argv) {
  func(argv[1]);
}

