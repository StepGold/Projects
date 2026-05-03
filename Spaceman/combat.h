#ifndef COMBAT_H
#define COMBAT_H

#include <SDL3/SDL.h>
#include "player.h"
#include "bullet.h"
#include "enemy.h"
#include <stdbool.h>
#include <wall.h>

bool intersect(float x1, float y1, float w1, float h1,
    float x2, float y2, float w2, float h2);
void combat_enemy_player(Enemy* enemy, Player* player);
void combat_bullet_enemy(Bullet* bullet, Enemy* enemy, Player* player);
void combat_bullet_wall(Bullet* bullet);

#endif
