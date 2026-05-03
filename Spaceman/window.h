#ifndef WINDOW_H
#define WINDOW_H

#include <SDL3/SDL.h>

void init_window_textures(SDL_Renderer* renderer);
void window0_render(SDL_Renderer* renderer);
void window1_render(SDL_Renderer* renderer, int high_score, int current_score);
void window2_render(SDL_Renderer* renderer);
void window3_render(SDL_Renderer* renderer);
void window_delete_textures(void);
#endif;
