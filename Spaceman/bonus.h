#ifndef BONUS_H
#define BONUS_H

#include <SDL3/SDL.h>

typedef struct {
	float x, y;
	int bonus_type;
	bool taken;
} Bonus;

void bonus_init(Bonus* bonus, float x, float y);
void bonus_init_textures(SDL_Renderer* renderer);
void bonuses_back_render(SDL_Renderer* renderer);
void bonus_render(const Bonus* bonus, SDL_Renderer* renderer);
void bonus_delete_textures(void);

#endif;
