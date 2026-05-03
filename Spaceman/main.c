#define SDL_MAIN_USE_CALLBACKS 1
#define MINIAUDIO_IMPLEMENTATION
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>
#include "miniaudio.h"
#include <SDL3_image/SDL_image.h>
#include <SDL3_ttf/SDL_ttf.h>
#include "player.h"
#include "bullets.h"
#include "enemies.h"
#include "bonuses.h"
#include "walls.h"
#include "HUD.h"
#include "window.h"
#include "record.h"
#include "stdio.h"

static SDL_Window* window;
static SDL_Renderer* renderer;

SDL_Texture* back_texture = NULL;

static const int W = 800, H = 600;
static int time_shot = 4;
static bool playing = false;

static int window_number = 0;
static int current_score = 0;
static int high_score;

static ma_engine audio_engine;
ma_sound  doom_sound;
ma_sound bullet_sound;
ma_sound monster_death_sound;

SDL_AppResult SDL_AppInit(void** appstate, int argc, char* argv[]) {
    SDL_Init(0);
    SDL_CreateWindowAndRenderer("2D_Game", W, H, 0, &window, &renderer);

    ma_result result = ma_engine_init(NULL, &audio_engine);
    ma_sound_init_from_file(&audio_engine, "doom.mp3", MA_SOUND_FLAG_LOOPING, NULL, NULL, &doom_sound);
    ma_sound_init_from_file(&audio_engine, "bullet_sound.mp3", 0, NULL, NULL, &bullet_sound);
    ma_sound_init_from_file(&audio_engine, "monster_death.mp3", 0, NULL, NULL, &monster_death_sound);

    back_texture = IMG_LoadTexture(renderer, "assets/back1.png");

    high_score = read_highscore();

    init_hud(renderer);
    init_player();
    bullets_init();
    enemies_init(renderer);
    bonuses_init(renderer);
    walls_init(renderer);
    init_window_textures(renderer);
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppIterate(void* appstate) {
    if (playing) {
        SDL_SetRenderDrawColor(renderer, 30, 30, 30, 255);
        SDL_RenderClear(renderer);

        SDL_FRect rect = { 0, 0, 4, 4 };
        SDL_GetTextureSize(back_texture, &rect.w, &rect.h);
        SDL_RenderTexture(renderer, back_texture, NULL, &rect);

        bonuses_update(player.x, player.y, &player, renderer);
        bonuses_render(renderer);
        walls_render(renderer);

        const bool* keys = SDL_GetKeyboardState(NULL);
        update_player_position(keys);
        update_player_shot_direction(keys);
        render_player(renderer);


        if (time_shot == 0) {
            if (player.shot_direction || player.bonus_all_dir) {
                if (player.bonus_all_dir) {
                    for (int i = 1; i < 9; i++) {
                        bullets_add(player.x, player.y, i, renderer, &bullet_sound);
                    }
                }
                else {
                    bullets_add(player.x, player.y, player.shot_direction, renderer, &bullet_sound);
                }
                time_shot = (player.bonus_fast_shot ? 8 : 16);
            }
        }
        else {
            time_shot -= 1;
        }

        if (player.bonus_speed) {
            player.time_bonus_speed -= 1;
            if (player.time_bonus_speed == 0) {
                player.bonus_speed = false;
            }
        }

        if (player.bonus_fast_shot) {
            player.time_bonus_fast_shot -= 1;
            if (player.time_bonus_fast_shot == 0) {
                player.bonus_fast_shot = false;
            }
        }

        if (player.bonus_all_dir) {
            player.time_bonus_all_dir -= 1;
            if (player.time_bonus_all_dir == 0) {
                player.bonus_all_dir = false;
            }
        }

        if (player.bonus_shield) {
            player.time_bonus_shield -= 1;
            if (player.time_bonus_shield == 0) {
                player.bonus_shield = false;
            }
        }

        draw_hud(renderer);

        bullets_update();
        bullets_render(renderer);

        if (enemies_all_dead()) {
            enemies_create_wave(player.wave);
            player.wave = player.wave + 2;
            if (player.wave % 10 == 1) {
                player.wave = player.wave + 2;
            }
        }

        enemies_update(&player, &monster_death_sound);
        enemies_render(renderer);

        playing = player.hp > 0;
        current_score = (player.wave / 10) * 4 + (player.wave % 10) / 2 - 1;
        high_score = current_score > high_score ? current_score : high_score;
    }
    else {
        ma_sound_stop(&doom_sound);
        ma_sound_seek_to_pcm_frame(&doom_sound, 0);


        const bool* keys = SDL_GetKeyboardState(NULL);

        switch (window_number) {
        case 0:
            window0_render(renderer);

            if (keys[SDL_SCANCODE_ESCAPE] && keys[SDL_SCANCODE_SPACE]) {
                return SDL_APP_SUCCESS;
            }
            else if (keys[SDL_SCANCODE_SPACE]) {
                window_number = 1;
            }

            break;
        case 1:
            window1_render(renderer, high_score, current_score);

            if (keys[SDL_SCANCODE_ESCAPE]) {
                window_number = 0;
            }
            else if (keys[SDL_SCANCODE_RETURN]) {
                if (player.wave != 3) {
                    bullets_clear();
                    enemies_clear();
                    bonuses_clear();
                    wall_delete_textures();
                    init_player();
                    bullets_init();
                    enemies_init(renderer);
                    bonuses_init(renderer);
                    walls_init(renderer);
                }
                playing = true;
                ma_sound_start(&doom_sound);
                ma_sound_set_volume(&doom_sound, 1.3f);
                ma_engine_set_volume(&audio_engine, 0.03f);
            }
            else if (keys[SDL_SCANCODE_Q]) {
                window_number = 2;
            }

            break;
        case 2:
            window2_render(renderer);

            if (keys[SDL_SCANCODE_E]) {
                window_number = 1;
            }

            break;
        default:
            break;
        }


    }

    SDL_RenderPresent(renderer);
    SDL_Delay(16);
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppEvent(void* appstate, SDL_Event* event) {
    switch (event->type) {
    case SDL_EVENT_QUIT:
        return SDL_APP_SUCCESS;
    default:
        break;
    }
    return SDL_APP_CONTINUE;
}

void SDL_AppQuit(void* appstate, SDL_AppResult result) {
    write_highscore(high_score);
    bullets_clear();
    enemies_clear();
    bonuses_clear();
    SDL_DestroyTexture(back_texture);
    window_delete_textures();
    ma_sound_stop(&doom_sound);
    ma_sound_stop(&bullet_sound);
    ma_sound_stop(&monster_death_sound);
    ma_sound_uninit(&doom_sound);
    ma_sound_uninit(&bullet_sound);
    ma_sound_uninit(&monster_death_sound);
    ma_engine_uninit(&audio_engine);
    delete_hud();
    wall_delete_textures();
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
}
