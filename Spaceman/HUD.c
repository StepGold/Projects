#include <SDL3/SDL.h>
#include <SDL3_image/SDL_image.h>
#include <SDL3_ttf/SDL_ttf.h>
#include <player.h>
#include "string.h"

static SDL_Texture* heartTexture = NULL;
static SDL_Texture* shieldTexture = NULL;
static SDL_Texture* speedTexture = NULL;
static SDL_Texture* fast_shotTexture = NULL;
static SDL_Texture* all_dirTexture = NULL;
static SDL_Texture* swordTexture = NULL;
SDL_Surface* text_surface;
static TTF_Font* font_wave_info;
static TTF_Font* font_bonus_help;
static TTF_Font* font_hp_and_damage_info;
SDL_Texture* wave_info;
SDL_Texture* bonus_help1;
SDL_Texture* bonus_help2;
SDL_Texture* bonus_help3;
SDL_Texture* bonus_help4;
SDL_Texture* hp_info;
SDL_Texture* damage_info;

static SDL_Color text_color = { 255, 255, 255, 255 };

void init_hud(SDL_Renderer* renderer) {
    TTF_Init();
    font_wave_info = TTF_OpenFont("assets/font.ttf", 48);
    font_bonus_help = TTF_OpenFont("assets/font.ttf", 36);
    font_hp_and_damage_info = TTF_OpenFont("assets/font.ttf", 70);
    heartTexture = IMG_LoadTexture(renderer, "assets/heart.png");
    shieldTexture = IMG_LoadTexture(renderer, "assets/shield.png");
    speedTexture = IMG_LoadTexture(renderer, "assets/speed.png");
    fast_shotTexture = IMG_LoadTexture(renderer, "assets/fast_shot.png");
    all_dirTexture = IMG_LoadTexture(renderer, "assets/all_dir.png");
    swordTexture = IMG_LoadTexture(renderer, "assets/sword.png");

    char* bonus_help_text[2];
    itoa(1, bonus_help_text, 10);
    text_surface = TTF_RenderText_Solid(font_bonus_help, bonus_help_text, strlen(bonus_help_text), text_color);
    bonus_help1 = SDL_CreateTextureFromSurface(renderer, text_surface);
    SDL_DestroySurface(text_surface);
    itoa(2, bonus_help_text, 10);
    text_surface = TTF_RenderText_Solid(font_bonus_help, bonus_help_text, strlen(bonus_help_text), text_color);
    bonus_help2 = SDL_CreateTextureFromSurface(renderer, text_surface);
    SDL_DestroySurface(text_surface);
    itoa(3, bonus_help_text, 10);
    text_surface = TTF_RenderText_Solid(font_bonus_help, bonus_help_text, strlen(bonus_help_text), text_color);
    bonus_help3 = SDL_CreateTextureFromSurface(renderer, text_surface);
    SDL_DestroySurface(text_surface);
    itoa(4, bonus_help_text, 10);
    text_surface = TTF_RenderText_Solid(font_bonus_help, bonus_help_text, strlen(bonus_help_text), text_color);
    bonus_help4 = SDL_CreateTextureFromSurface(renderer, text_surface);
    SDL_DestroySurface(text_surface);
}

void draw_hud(SDL_Renderer* renderer) {
    SDL_FRect HUD_rect = { 0, 500, 800, 100 };
    SDL_SetRenderDrawColor(renderer, 50, 50, 50, 255);
    SDL_RenderFillRect(renderer, &HUD_rect);

    SDL_FRect hud_bar_rect = {180, 500, 3, 100};
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderFillRect(renderer, &hud_bar_rect);
    hud_bar_rect.x = 365;
    SDL_RenderFillRect(renderer, &hud_bar_rect);
    hud_bar_rect.x = 470;
    SDL_RenderFillRect(renderer, &hud_bar_rect);
    hud_bar_rect.x = 580;
    SDL_RenderFillRect(renderer, &hud_bar_rect);
    hud_bar_rect.x = 685;
    SDL_RenderFillRect(renderer, &hud_bar_rect);


    SDL_FRect heart_rect = { 60, 500, 100, 100 };
    SDL_FRect hp_info_rect = { 40, 510, 0, 0 };
    SDL_RenderTexture(renderer, heartTexture, NULL, &heart_rect);
    char* hp_info_text[2];
    itoa(player.hp, hp_info_text, 10);
    text_surface = TTF_RenderText_Solid(font_hp_and_damage_info, hp_info_text, strlen(hp_info_text), text_color);
    hp_info = SDL_CreateTextureFromSurface(renderer, text_surface);
    SDL_GetTextureSize(hp_info, &hp_info_rect.w, &hp_info_rect.h);
    SDL_DestroySurface(text_surface);
    SDL_RenderTexture(renderer, hp_info, NULL, &hp_info_rect);
    SDL_DestroyTexture(hp_info);

    SDL_FRect sword_rect = { 255, 515, 75, 75 };
    SDL_FRect damage_info_rect = { 215, 510, 0, 0 };
    SDL_RenderTexture(renderer, swordTexture, NULL, &sword_rect);
    char* damage_info_text[10];
    itoa(player.damage, damage_info_text, 10);
    text_surface = TTF_RenderText_Solid(font_hp_and_damage_info, damage_info_text, strlen(damage_info_text), text_color);
    damage_info = SDL_CreateTextureFromSurface(renderer, text_surface);
    SDL_GetTextureSize(damage_info, &damage_info_rect.w, &damage_info_rect.h);
    SDL_DestroySurface(text_surface);
    SDL_RenderTexture(renderer, damage_info, NULL, &damage_info_rect);
    SDL_DestroyTexture(damage_info);


    SDL_FRect speed_rect = { 370, 505, 100, 100 };
    SDL_FRect shield_rect = { 488, 510, 80, 80 };
    SDL_FRect fast_shot_rect = { 595, 510, 80, 80 };
    SDL_FRect all_dir_rect = { 714, 520, 60, 60 };
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);

    SDL_FRect bonus_square_panel = { 385, 515, 70, 70 };
    SDL_SetRenderDrawColor(renderer, 70, 70, 70, 255);
    SDL_RenderFillRect(renderer, &bonus_square_panel);
    bonus_square_panel.x = 493;
    SDL_RenderFillRect(renderer, &bonus_square_panel);
    bonus_square_panel.x = 599;
    SDL_RenderFillRect(renderer, &bonus_square_panel);
    bonus_square_panel.x = 709;
    SDL_RenderFillRect(renderer, &bonus_square_panel);

    if (player.have_bonus_speed) {
        SDL_RenderTexture(renderer, speedTexture, NULL, &speed_rect);
    }
    if (player.have_bonus_shield) {
        SDL_RenderTexture(renderer, shieldTexture, NULL, &shield_rect);
    }
    if (player.have_bonus_fast_shot) {
        SDL_RenderTexture(renderer, fast_shotTexture, NULL, &fast_shot_rect);
    }
    if (player.have_bonus_all_dir) {
        SDL_RenderTexture(renderer, all_dirTexture, NULL, &all_dir_rect);
    }

    SDL_FRect wave_info_rect = {10, 5, 0, 0};
    char wave_text[15];
    int wave_number = (player.wave / 10) * 4 + (player.wave % 10) / 2 - 1;
    itoa(wave_number, wave_text, 10);
    char* ptr = wave_text;
    text_surface = TTF_RenderText_Solid(font_wave_info, wave_text, strlen(wave_text), text_color);
    wave_info = SDL_CreateTextureFromSurface(renderer, text_surface);
    SDL_GetTextureSize(wave_info, &wave_info_rect.w, &wave_info_rect.h);
    SDL_DestroySurface(text_surface);
    SDL_RenderTexture(renderer, wave_info, NULL, &wave_info_rect);
    SDL_DestroyTexture(wave_info);

    SDL_FRect bonus_help_rect = { 375, 555, 2, 2 };
    SDL_GetTextureSize(bonus_help1, &bonus_help_rect.w, &bonus_help_rect.h);
    SDL_RenderTexture(renderer, bonus_help1, NULL, &bonus_help_rect);
    bonus_help_rect.x += 105;
    SDL_GetTextureSize(bonus_help2, &bonus_help_rect.w, &bonus_help_rect.h);
    SDL_RenderTexture(renderer, bonus_help2, NULL, &bonus_help_rect);
    bonus_help_rect.x += 105;
    SDL_GetTextureSize(bonus_help3, &bonus_help_rect.w, &bonus_help_rect.h);
    SDL_RenderTexture(renderer, bonus_help3, NULL, &bonus_help_rect);
    bonus_help_rect.x += 105;
    SDL_GetTextureSize(bonus_help4, &bonus_help_rect.w, &bonus_help_rect.h);
    SDL_RenderTexture(renderer, bonus_help4, NULL, &bonus_help_rect);


}

void delete_hud() {
    SDL_DestroyTexture(heartTexture);
    SDL_DestroyTexture(shieldTexture);
    SDL_DestroyTexture(speedTexture);
    SDL_DestroyTexture(fast_shotTexture);
    SDL_DestroyTexture(all_dirTexture);
    SDL_DestroyTexture(swordTexture);
    SDL_DestroyTexture(bonus_help1);
    SDL_DestroyTexture(bonus_help2);
    SDL_DestroyTexture(bonus_help3);
    SDL_DestroyTexture(bonus_help4);
    TTF_CloseFont(font_wave_info);
    TTF_CloseFont(font_bonus_help);
    TTF_CloseFont(font_hp_and_damage_info);
}