#ifndef WALLS_H
#define WALLS_H

#include "SDL3/SDL.h"
#include "wall.h"

void walls_init(SDL_Renderer* renderer);
void walls_render(SDL_Renderer* renderer);
const Wall* get_walls_coordinates(int* n);
int* get_walls_indexes(void);
#endif;