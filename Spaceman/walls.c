#include "walls.h"
#include "player.h"
#include "time.h"
#include <stdlib.h>
#include <stdio.h>

static const Wall walls_coordinates[36] = {
    {  150,  100,  220,  107 },
    {  110,  100,  117,  170 },
    {  150,  150,  220,  157 },
    {  170,  100,  177,  170 }, // Лево-верх/
    {  130,  260,  200,  267 },
    {  130,  200,  137,  270 },
    {  130,  230,  200,  237 },
    {  160,  200,  167,  270 }, // Лево-центр/
    {  120,  370,  190,  377 },
    {  130,  330,  137,  400 },
    {  120,  330,  190,  337 },
    {  180,  330,  187,  400 }, // Лево-низ/
    {  650,  100,  720,  107 },
    {  610,  100,  617,  170 },
    {  650,  150,  720,  157 },
    {  670,  100,  677,  170 }, // Право-верх/
    {  630,  260,  700,  267 },
    {  660,  200,  667,  270 },
    {  630,  230,  700,  237 },
    {  630,  200,  637,  270 }, // Право-центр/
    {  620,  370,  690,  377 },
    {  630,  330,  637,  400 },
    {  620,  330,  690,  337 },
    {  680,  330,  687,  400 }, // Право-низ/
    {  365,  220,  435,  227 },
    {  350,  205,  357,  275 },
    {  365,  290,  435,  297 },
    {  450,  205,  457,  275 }, // Центр/
    {  380,  100,  450,  107 },
    {  360,  110,  430,  117 },
    {  360,  120,  430,  127 },
    {  370,  130,  440,  137 }, // Центр-верх//
    {  380,  400,  450,  407 },
    {  360,  410,  430,  417 },
    {  360,  380,  430,  387 },
    {  370,  390,  440,  397 }, // Центр-низ//
};

static int walls[5];

int get_random(int number) {
    static int initialized = 0;
    if (!initialized) {
        srand(time(NULL));
        initialized = 1;
    }

    return rand() % number;
}

void walls_init(SDL_Renderer* renderer) {
    init_wall_texture(renderer);
    int r1 = get_random(3);
    int r2 = get_random(3);
    int r3 = get_random(3);
    walls[0] = r1 * 4 + get_random(4);
    walls[1] = ((r1 + 1) % 3) * 4 + get_random(4);
    walls[2] = 12 + r2 * 4 + get_random(4);
    walls[3] = 12 + ((r2 + 1) % 3) * 4 + get_random(4);
    walls[4] = 24 + r3 * 4 + get_random(4);

}


const Wall* get_walls_coordinates(int* n) {
    *n = 5;
    return walls_coordinates;
}

int* get_walls_indexes(void) {
    return walls;
}

void walls_render(SDL_Renderer* renderer) {
    for (int i = 0; i < 5; i++) {
        wall_render(&walls_coordinates[walls[i]], renderer);
    }
}
