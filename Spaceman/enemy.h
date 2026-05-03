#ifndef ENEMY_H
#define ENEMY_H

#include <SDL3/SDL.h>
#include "miniaudio.h"
#include "player.h"
#include <stdbool.h>

typedef struct {
    float x, y;
    int hp;
    int maxHp;
    int damage;
    bool attack;
    int img;
    int tick_img;
    int tick;
    int wall_movement, wall_tick;
} Enemy;

void init_enemy_font(SDL_Renderer* renderer);
void enemy_init(Enemy* enemy, float x, float y, int hp, int damage);
void enemy_init_textures(SDL_Renderer* renderer);
bool enemy_update(Enemy* enemy, Player* player, ma_sound* monster_death_sound);
void enemy_render(const Enemy* enemy, SDL_Renderer* renderer);
void enemy_delete_textures(void);

#endif
