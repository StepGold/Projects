#define _CRT_SECURE_NO_WARNINGS
#include "record.h"
#include <stdio.h>
#include <SDL3/SDL.h>

int read_highscore() {
    FILE* file = fopen("highscore.txt", "r");
    if (!file) return 0;

    char buffer[32];
    int highscore = 0;

    if (fgets(buffer, sizeof(buffer), file)) {
        sscanf(buffer, "%d", &highscore);
    }

    fclose(file);
    return highscore;
}

void write_highscore(int highscore) {
    FILE* file = fopen("highscore.txt", "w");

    fprintf(file, "%d", highscore);
    fclose(file);
}