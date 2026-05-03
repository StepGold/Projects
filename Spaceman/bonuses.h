#ifndef BONUSES_H
#define BONUSES_H

#include "SDL3/SDL.h"
#include "bonus.h"
#include "player.h"

void bonuses_init(SDL_Renderer* renderer);
void bonuses_update(float player_x, float player_y, Player* player, SDL_Renderer* renderer);
void bonuses_render(SDL_Renderer* renderer);
void bonuses_clear(void);

#endif;
