#ifndef BULLETS_H
#define BULLETS_H

#include <SDL3/SDL.h>
#include "bullet.h"

typedef struct BulletNode {
    Bullet bullet;
    struct BulletNode* next;
} BulletNode;

void bullets_init(void);

void bullets_add(float x, float y, int direction, SDL_Renderer* renderer, ma_sound* bullet_sound);

int bullets_update(void);

void bullets_render(SDL_Renderer* renderer);

void bullets_clear(void);

const BulletNode* bullets_get_list(void);

#endif
