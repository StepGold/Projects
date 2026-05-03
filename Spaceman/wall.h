#ifndef WALL_H
#define WALL_H

#include <SDL3/SDL.h>

typedef struct {
	float x1, y1;
	float x2, y2;
	SDL_Texture* lazer;
} Wall;

void wall_init(Wall* wall, float x1, float y1, float x2, float y2);
void init_wall_texture(SDL_Renderer* renderer);
void wall_render(const Wall* wall, SDL_Renderer* renderer);
void wall_delete_textures(void);
#endif;