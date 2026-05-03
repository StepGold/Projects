#include "bonus.h"
#include <SDL3_image/SDL_image.h>
#include <stdio.h>
#include <stdlib.h>

static SDL_Texture* speedTexture;
static SDL_Texture* shieldTexture;
static SDL_Texture* fast_shotTexture;
static SDL_Texture* all_dirTexture;
static SDL_Texture* heartTexture;
static SDL_Texture* swordTexture;
static SDL_Texture* back_bonus_texture;

static SDL_FRect bg1 = { 215.0, 195.0, 36, 36 };
static SDL_FRect bg2 = { 575.0, 195.0, 36, 36 };
static SDL_FRect bg3 = { 575.0, 295.0, 36, 36 };
static SDL_FRect bg4 = { 215.0, 295.0, 36, 36 };


void bonus_init(Bonus* bonus, float x, float y) {
    bonus->x = x;
    bonus->y = y;
    bonus->taken = false;
}

void bonus_init_textures(SDL_Renderer* renderer) {
    speedTexture = IMG_LoadTexture(renderer, "assets/speed.png");
    shieldTexture = IMG_LoadTexture(renderer, "assets/shield.png");
    fast_shotTexture = IMG_LoadTexture(renderer, "assets/fast_shot.png");
    all_dirTexture = IMG_LoadTexture(renderer, "assets/all_dir.png");
    heartTexture = IMG_LoadTexture(renderer, "assets/heart.png");
    swordTexture = IMG_LoadTexture(renderer, "assets/sword.png");
    back_bonus_texture = IMG_LoadTexture(renderer, "assets/green.png");
}

void bonuses_back_render(SDL_Renderer* renderer) {
    SDL_RenderTexture(renderer, back_bonus_texture, NULL, &bg1);
    SDL_RenderTexture(renderer, back_bonus_texture, NULL, &bg2);
    SDL_RenderTexture(renderer, back_bonus_texture, NULL, &bg3);
    SDL_RenderTexture(renderer, back_bonus_texture, NULL, &bg4);
}

void bonus_render(const Bonus* bonus, SDL_Renderer* renderer) {
    if (bonus->taken) return;

    SDL_FRect rect = { bonus->x, bonus->y, 25, 25 };

    switch (bonus->bonus_type) {
    case 0:
        SDL_RenderTexture(renderer, speedTexture, NULL, &rect);
        break;
    case 1:
        SDL_RenderTexture(renderer, shieldTexture, NULL, &rect);
        break;
    case 2:
        SDL_RenderTexture(renderer, fast_shotTexture, NULL, &rect);
        break;
    case 3:
        SDL_RenderTexture(renderer, all_dirTexture, NULL, &rect);
        break;
    case 4:
        SDL_RenderTexture(renderer, heartTexture, NULL, &rect);
        break;
    case 5:
        SDL_RenderTexture(renderer, swordTexture, NULL, &rect);
        break;
    default:
        break;
    }
}

void bonus_delete_textures() {
    SDL_DestroyTexture(speedTexture);
    SDL_DestroyTexture(shieldTexture);
    SDL_DestroyTexture(speedTexture);
    SDL_DestroyTexture(fast_shotTexture);
    SDL_DestroyTexture(heartTexture);
    SDL_DestroyTexture(swordTexture);
    SDL_DestroyTexture(back_bonus_texture);
}
