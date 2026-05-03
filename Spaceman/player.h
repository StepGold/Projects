#ifndef PLAYER_H
#define PLAYER_H

#include <SDL3/SDL.h>


typedef struct {
    float x, y;
    int hp;
    int damage;
    int movement_direction;
    int shot_direction;
    bool have_bonus_speed, have_bonus_fast_shot, have_bonus_all_dir, have_bonus_shield;
    bool bonus_speed, bonus_all_dir, bonus_fast_shot, bonus_shield;
    int time_bonus_speed, time_bonus_all_dir, time_bonus_fast_shot, time_bonus_shield;
    int img, tick, wave;
} Player;

extern Player player;

void init_player();
void update_player_position(const bool* keys);
void update_player_shot_direction(const bool* keys);
void render_player(SDL_Renderer* renderer);

#endif
