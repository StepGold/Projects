#ifndef BULLET_H
#define BULLET_H

#include "miniaudio.h"
#include <SDL3/SDL.h>
#include <stdbool.h>

typedef struct {
    float x, y;
    int direction;
    bool active;
} Bullet;

void bullet_init(Bullet* bullet, float x, float y, int direction, ma_sound* bullet_sound);
void bullet_init_texture(SDL_Renderer* renderer);
bool bullet_update(Bullet* bullet);
void bullet_render(const Bullet* bullet, SDL_Renderer* renderer);
void bullet_delete_textures();

#endif
