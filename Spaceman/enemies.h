#ifndef ENEMIES_H
#define ENEMIES_H

#include <SDL3/SDL.h>
#include "miniaudio.h"
#include "enemy.h"
#include "player.h"

typedef struct EnemyNode {
    Enemy enemy;
    struct EnemyNode* next;
} EnemyNode;

void enemies_init(SDL_Renderer* renderer);

void enemies_create_wave(int wave);

void enemies_add(float x, float y, int wave);

void enemies_update(Player* player, ma_sound* monster_death_sound);

bool enemies_all_dead(void);

void enemies_render(SDL_Renderer* renderer);

void enemies_clear(void);

const EnemyNode* enemies_get_list(void);

#endif