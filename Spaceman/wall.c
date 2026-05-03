#include "wall.h"
#include <SDL3/SDL.h>
#include <SDL3_image/SDL_image.h>
#include <stdio.h>

static SDL_Texture* verticalLazer = NULL;
static SDL_Texture* horisontalLazer = NULL;

void wall_init(Wall* wall, float x1, float y1, float x2, float y2) {
	wall->x1 = x1;
	wall->x2 = x2;
	wall->y1 = y1;
	wall->y2 = y2;
}

void init_wall_texture(SDL_Renderer* renderer) {
	verticalLazer = IMG_LoadTexture(renderer, "assets/verticalLazer.png");
	horisontalLazer = IMG_LoadTexture(renderer, "assets/horisontalLazer.png");
}

void wall_render(const Wall* wall, SDL_Renderer* renderer) {
	SDL_FRect rect = { wall->x1, wall->y1, (abs(wall->x1 - wall->x2)), (abs(wall->y1 - wall->y2)) };
	if (rect.w < rect.h) {
		SDL_RenderTexture(renderer, verticalLazer, NULL, &rect);
	}
	else {
		SDL_RenderTexture(renderer, horisontalLazer, NULL, &rect);
	}
}

void wall_delete_textures() {
	SDL_DestroyTexture(verticalLazer);
	SDL_DestroyTexture(horisontalLazer);
}