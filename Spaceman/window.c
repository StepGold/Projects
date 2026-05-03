#include "window.h"
#include "record.h"
#include "player.h"
#include <SDL3/SDL.h>
#include <SDL3_image/SDL_image.h>
#include <SDL3_ttf/SDL_ttf.h>
#include "stdio.h"

SDL_Texture* back0_texture = NULL;
SDL_Texture* space_texture = NULL;
SDL_Texture* spaceman_texture = NULL;
SDL_Texture* back_w1_texture = NULL;
SDL_Texture* back_w2_texture = NULL;
SDL_Texture* score_texture = NULL;
SDL_Texture* keys_texture = NULL;
SDL_Texture* record_texture = NULL;
SDL_Texture* wasd_texture = NULL;
SDL_Texture* strel_texture = NULL;
SDL_Texture* move_texture = NULL;
SDL_Texture* shot_texture = NULL;
SDL_Texture* numbers_texture = NULL;
SDL_Texture* use_texture = NULL;
SDL_Texture* return_texture = NULL;
static TTF_Font* font_score_and_record;
SDL_Texture* score_info;
SDL_Texture* record_info;
SDL_Surface* text_surface;

static SDL_Color score_text_color = { 255, 255, 255, 255 };
static SDL_Color record_text_color = { 255, 215, 0, 255 };

void init_window_textures(SDL_Renderer* renderer) {
    TTF_Init();
    back0_texture = IMG_LoadTexture(renderer, "assets/back0.png");
    space_texture = IMG_LoadTexture(renderer, "assets/space.png");
    spaceman_texture = IMG_LoadTexture(renderer, "assets/spaceman.png");
    back_w1_texture = IMG_LoadTexture(renderer, "assets/back_w1.png");
    back_w2_texture = IMG_LoadTexture(renderer, "assets/back_w2.png");
    score_texture = IMG_LoadTexture(renderer, "assets/score.png");
    keys_texture = IMG_LoadTexture(renderer, "assets/keys.png");
    record_texture = IMG_LoadTexture(renderer, "assets/record.png");
    wasd_texture = IMG_LoadTexture(renderer, "assets/wasd.png");
    strel_texture = IMG_LoadTexture(renderer, "assets/strelki.png");
    move_texture = IMG_LoadTexture(renderer, "assets/move.png");
    shot_texture = IMG_LoadTexture(renderer, "assets/shoot.png");
    numbers_texture = IMG_LoadTexture(renderer, "assets/numbers.png");
    use_texture = IMG_LoadTexture(renderer, "assets/bonuses.png");
    return_texture = IMG_LoadTexture(renderer, "assets/return.png");
    font_score_and_record = TTF_OpenFont("assets/font.ttf", 56);
}

void window0_render(SDL_Renderer* renderer) {
    SDL_RenderClear(renderer);

    SDL_FRect rect0 = { 0, 0, 800, 600 };
    SDL_RenderTexture(renderer, back0_texture, NULL, &rect0);

    SDL_FRect rect1 = { 80, 30, 650, 150 };
    SDL_RenderTexture(renderer, spaceman_texture, NULL, &rect1);

    SDL_FRect rect2 = { 150, 400, 4, 4 };
    SDL_GetTextureSize(space_texture, &rect2.w, &rect2.h);
    SDL_RenderTexture(renderer, space_texture, NULL, &rect2);
}


void window1_render(SDL_Renderer* renderer, int high_score, int current_score) {
    SDL_RenderClear(renderer);

    SDL_FRect rect_men = { 0, 0, 800, 600 };
    SDL_RenderTexture(renderer, back_w1_texture, NULL, &rect_men);

    SDL_FRect rect_text_spaceman = { 340, 30, 470, 100 };
    SDL_RenderTexture(renderer, spaceman_texture, NULL, &rect_text_spaceman);

    SDL_FRect rect_score = { 550, 200, 92, 42 };
    SDL_RenderTexture(renderer, score_texture, NULL, &rect_score);

    SDL_FRect rect_record = { 550, 270, 150, 50 };
    SDL_RenderTexture(renderer, record_texture, NULL, &rect_record);

    SDL_FRect rect_keys = { 550, 490, 250, 115 };
    SDL_RenderTexture(renderer, keys_texture, NULL, &rect_keys);

    SDL_FRect score_info_rect = { 650, 187, 0, 0 };
    char* score_info_text[4];
    _itoa_s(current_score, score_info_text, 4, 10);
    text_surface = TTF_RenderText_Solid(font_score_and_record, score_info_text, strlen(score_info_text), score_text_color);
    score_info = SDL_CreateTextureFromSurface(renderer, text_surface);
    SDL_GetTextureSize(score_info, &score_info_rect.w, &score_info_rect.h);
    SDL_DestroySurface(text_surface);
    SDL_RenderTexture(renderer, score_info, NULL, &score_info_rect);
    SDL_DestroyTexture(score_info);

    SDL_FRect record_info_rect = { 700, 260, 0, 0 };
    char* record_info_text[4];
    _itoa_s(high_score, record_info_text, 4, 10);
    text_surface = TTF_RenderText_Solid(font_score_and_record, record_info_text, strlen(record_info_text), record_text_color);
    record_info = SDL_CreateTextureFromSurface(renderer, text_surface);
    SDL_GetTextureSize(record_info, &record_info_rect.w, &record_info_rect.h);
    SDL_DestroySurface(text_surface);
    SDL_RenderTexture(renderer, record_info, NULL, &record_info_rect);
    SDL_DestroyTexture(record_info);
}


void window2_render(SDL_Renderer* renderer) {
    SDL_RenderClear(renderer);

    SDL_FRect rect_men = { 0, 0, 800, 600 };
    SDL_RenderTexture(renderer, back_w1_texture, NULL, &rect_men);

    SDL_FRect rect_text_spaceman = { 340, 30, 470, 100 };
    SDL_RenderTexture(renderer, spaceman_texture, NULL, &rect_text_spaceman);

    SDL_SetRenderDrawColor(renderer, 10, 10, 70, 255);
    SDL_FRect rect_back = { 400, 200, 400, 400 };
    SDL_RenderFillRect(renderer, &rect_back);

    SDL_FRect rect_wasd = { 410, 200, 150, 110 };
    SDL_RenderTexture(renderer, wasd_texture, NULL, &rect_wasd);

    SDL_FRect rect_strel = { 415, 310, 140, 130 };
    SDL_RenderTexture(renderer, strel_texture, NULL, &rect_strel);

    SDL_FRect rect_num = { 420, 450, 130, 85 };
    SDL_RenderTexture(renderer, numbers_texture, NULL, &rect_num);

    SDL_FRect rect_move = { 580, 240, 100, 47 };
    SDL_RenderTexture(renderer, move_texture, NULL, &rect_move);

    SDL_FRect rect_shot = { 580, 365, 120, 50 };
    SDL_RenderTexture(renderer, shot_texture, NULL, &rect_shot);

    SDL_FRect rect_use = { 580, 465, 190, 60 };
    SDL_RenderTexture(renderer, use_texture, NULL, &rect_use);


    SDL_FRect rect_return = { 700, 565, 90, 35 };
    SDL_RenderTexture(renderer, return_texture, NULL, &rect_return);
}


void window_delete_textures() {
    SDL_DestroyTexture(back0_texture);
    SDL_DestroyTexture(space_texture);
    SDL_DestroyTexture(spaceman_texture);
    SDL_DestroyTexture(back_w1_texture);
    SDL_DestroyTexture(back_w2_texture);
    SDL_DestroyTexture(score_texture);
    SDL_DestroyTexture(keys_texture);
    SDL_DestroyTexture(record_texture);
    SDL_DestroyTexture(wasd_texture);
    SDL_DestroyTexture(strel_texture);
    SDL_DestroyTexture(move_texture);
    SDL_DestroyTexture(shot_texture);
    SDL_DestroyTexture(numbers_texture);
    SDL_DestroyTexture(use_texture);
    SDL_DestroyTexture(return_texture);
    TTF_CloseFont(font_score_and_record);
}
