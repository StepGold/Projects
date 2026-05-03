#ifndef HUD_H
#define HUD_H

#include <SDL3/SDL.h>

void init_hud(SDL_Renderer* renderer);

void draw_hud(SDL_Renderer* renderer);

void delete_hud(void);

#endif

