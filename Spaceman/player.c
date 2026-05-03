#include "player.h"
#include <SDL3/SDL.h>
#include <SDL3_image/SDL_image.h>
#include <stdio.h>
#include <wall.h>
#include <walls.h>
#include <combat.h>
#define MIN(a, b) ((a) < (b) ? (a) : (b))

static const float W = 800, H = 500;
static const float speed1 = 2, speed2 = 1.5;

Player player;

void init_player() {
    player = (Player){
        .x = (W / 2) - 10,
        .y = (H / 2 - 20),
        .hp = 3,
        .damage = 1,
        .movement_direction = 0,
        .shot_direction = 0,
        .have_bonus_speed = false,
        .have_bonus_fast_shot = false,
        .have_bonus_all_dir = false,
        .have_bonus_shield = false,
        .bonus_speed = false,
        .bonus_all_dir = false,
        .bonus_fast_shot = false,
        .bonus_shield = false,
        .time_bonus_speed = 0,
        .time_bonus_all_dir = 0,
        .time_bonus_fast_shot = 0,
        .time_bonus_shield = 0,
        .img = 0,
        .tick = 0,
        .wave = 3
    };
}

void update_player_position(const bool* keys) {
    if (keys[SDL_SCANCODE_W]) {
        if (keys[SDL_SCANCODE_A]) {
            player.movement_direction = 7;
        }
        else if (keys[SDL_SCANCODE_D]) {
            player.movement_direction = 5;
        }
        else {
            player.movement_direction = 6;
        }
    }
    else if (keys[SDL_SCANCODE_S]) {
        if (keys[SDL_SCANCODE_A]) {
            player.movement_direction = 1;
        }
        else if (keys[SDL_SCANCODE_D]) {
            player.movement_direction = 3;
        }
        else {
            player.movement_direction = 2;
        }
    }
    else if (keys[SDL_SCANCODE_A]) {
        player.movement_direction = 8;
    }
    else if (keys[SDL_SCANCODE_D]) {
        player.movement_direction = 4;
    }
    else {
        player.movement_direction = 0;
    }

    if (keys[SDL_SCANCODE_1] && player.have_bonus_speed) {
        player.have_bonus_speed = false;
        player.bonus_speed = true;
        player.time_bonus_speed = 300;
    }
    if (keys[SDL_SCANCODE_2] && player.have_bonus_shield) {
        player.have_bonus_shield = false;
        player.bonus_shield = true;
        player.time_bonus_shield = 300;
    }
    if (keys[SDL_SCANCODE_3] && player.have_bonus_fast_shot) {
        player.have_bonus_fast_shot = false;
        player.bonus_fast_shot = true;
        player.time_bonus_fast_shot = 300;
    }
    if (keys[SDL_SCANCODE_4] && player.have_bonus_all_dir) {
        player.have_bonus_all_dir = false;
        player.bonus_all_dir = true;
        player.time_bonus_all_dir = 300;
    }
    float new_x = player.x;
    float new_y = player.y;


    switch (player.movement_direction) {
    case 1:
        new_x -= speed2 * (player.bonus_speed ? 2 : 1) * (player.x > 0);
        new_y += speed2 * (player.bonus_speed ? 2 : 1) * (player.y < H - 40);
        break;
    case 3:
        new_x += speed2 * (player.bonus_speed ? 2 : 1) * (player.x < W - 20);
        new_y += speed2 * (player.bonus_speed ? 2 : 1) * (player.y < H - 40);
        break;
    case 5:
        new_x += speed2 * (player.bonus_speed ? 2 : 1) * (player.x < W - 20);
        new_y -= speed2 * (player.bonus_speed ? 2 : 1) * (player.y > 0);
        break;
    case 7:
        new_x -= speed2 * (player.bonus_speed ? 2 : 1) * (player.x > 0);
        new_y -= speed2 * (player.bonus_speed ? 2 : 1) * (player.y > 0);
        break;
    case 2:
        new_y += speed1 * (player.bonus_speed ? 2 : 1) * (player.y < H - 40);
        break;
    case 4:
        new_x += speed1 * (player.bonus_speed ? 2 : 1) * (player.x < W - 20);
        break;
    case 6:
        new_y -= speed1 * (player.bonus_speed ? 2 : 1) * (player.y > 0);
        break;
    case 8:
        new_x -= speed1 * (player.bonus_speed ? 2 : 1) * (player.x > 0);
        break;
    }
    int walls_count;
    const int* walls = get_walls_indexes();
    const Wall* walls_coordinates = get_walls_coordinates(&walls_count);
    int blocked = 0;
    for (int i = 0; i < walls_count; i++) {
        float wall_x = walls_coordinates[walls[i]].x1;
        float wall_y = walls_coordinates[walls[i]].y1;
        float wall_w = abs(walls_coordinates[walls[i]].x2 - walls_coordinates[walls[i]].x1);
        float wall_h = abs(walls_coordinates[walls[i]].y2 - walls_coordinates[walls[i]].y1);

        blocked = intersect(new_x, new_y, 32, 40, wall_x, wall_y, wall_w, wall_h);
        if (blocked) {
            blocked = intersect(new_x, player.y, 32, 40, wall_x, wall_y, wall_w, wall_h) ? 2 : 1;
            break;
        }
    }
    if (blocked) {
        if (player.movement_direction == 1 || player.movement_direction == 3 ||
            player.movement_direction == 5 || player.movement_direction == 7) {
            if (blocked == 1) {
                player.x = new_x;
            }
            else {
                player.y = new_y;
            }
        }
    }
    else {
        player.x = new_x;
        player.y = new_y;
    }
}


void update_player_shot_direction(const bool* keys) {
    if (keys[SDL_SCANCODE_KP_8] || keys[SDL_SCANCODE_UP]) {
        if (keys[SDL_SCANCODE_KP_4] || keys[SDL_SCANCODE_LEFT]) {
            player.shot_direction = 7;
        }
        else if (keys[SDL_SCANCODE_KP_6] || keys[SDL_SCANCODE_RIGHT]) {
            player.shot_direction = 5;
        }
        else {
            player.shot_direction = 6;
        }
    }
    else if (keys[SDL_SCANCODE_KP_5] || keys[SDL_SCANCODE_DOWN]) {
        if (keys[SDL_SCANCODE_KP_4] || keys[SDL_SCANCODE_LEFT]) {
            player.shot_direction = 1;
        }
        else if (keys[SDL_SCANCODE_KP_6] || keys[SDL_SCANCODE_RIGHT]) {
            player.shot_direction = 3;
        }
        else {
            player.shot_direction = 2;
        }
    }
    else if (keys[SDL_SCANCODE_KP_4] || keys[SDL_SCANCODE_LEFT]) {
        player.shot_direction = 8;
    }
    else if (keys[SDL_SCANCODE_KP_6] || keys[SDL_SCANCODE_RIGHT]) {
        player.shot_direction = 4;
    }
    else {
        player.shot_direction = 0;
    }
}

void render_player(SDL_Renderer* renderer) {
    if (player.bonus_shield) {
        SDL_SetRenderDrawColor(renderer, 230, 0, 130, 255);
        SDL_FRect rect1 = { player.x - 2, player.y - 2, 36, 44 };
        SDL_RenderFillRect(renderer, &rect1);
    }

    SDL_FRect rect = { player.x, player.y, 20, 40 };

    SDL_Texture* playerTexture = NULL;

    switch (player.shot_direction)
    {
    case 0:
        switch (player.img)
        {
        case 0:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman1.png");
            break;
        case 1:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman2.png");
            break;
        case 2:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman3.png");
            break;
        case 3:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman4.png");
            break;
        case 4:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman5.png");
            break;
        case 5:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman6.png");
            break;
        }
        break;
    case 1:
        switch (player.img)
        {
        case 0:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman43.png");
            break;
        case 1:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman44.png");
            break;
        case 2:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman45.png");
            break;
        case 3:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman46.png");
            break;
        case 4:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman47.png");
            break;
        case 5:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman48.png");
            break;
        }
        break;
    case 2:
        switch (player.img)
        {
        case 0:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman25.png");
            break;
        case 1:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman26.png");
            break;
        case 2:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman27.png");
            break;
        case 3:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman28.png");
            break;
        case 4:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman29.png");
            break;
        case 5:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman30.png");
            break;
        }
        break;
    case 3:
        switch (player.img)
        {
        case 0:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman19.png");
            break;
        case 1:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman20.png");
            break;
        case 2:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman21.png");
            break;
        case 3:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman22.png");
            break;
        case 4:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman23.png");
            break;
        case 5:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman24.png");
            break;
        }
        break;
    case 4:
        switch (player.img)
        {
        case 0:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman1.png");
            break;
        case 1:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman2.png");
            break;
        case 2:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman3.png");
            break;
        case 3:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman4.png");
            break;
        case 4:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman5.png");
            break;
        case 5:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman6.png");
            break;
        }
        break;
    case 5:
        switch (player.img)
        {
        case 0:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman7.png");
            break;
        case 1:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman8.png");
            break;
        case 2:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman9.png");
            break;
        case 3:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman10.png");
            break;
        case 4:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman11.png");
            break;
        case 5:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman12.png");
            break;
        }
        break;
    case 6:
        switch (player.img)
        {
        case 0:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman13.png");
            break;
        case 1:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman14.png");
            break;
        case 2:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman15.png");
            break;
        case 3:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman16.png");
            break;
        case 4:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman17.png");
            break;
        case 5:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman18.png");
            break;
        }
        break;
    case 7:
        switch (player.img)
        {
        case 0:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman37.png");
            break;
        case 1:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman38.png");
            break;
        case 2:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman39.png");
            break;
        case 3:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman40.png");
            break;
        case 4:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman41.png");
            break;
        case 5:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman42.png");
            break;
        }
        break;
    case 8:
        switch (player.img)
        {
        case 0:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman31.png");
            break;
        case 1:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman32.png");
            break;
        case 2:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman33.png");
            break;
        case 3:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman34.png");
            break;
        case 4:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman35.png");
            break;
        case 5:
            playerTexture = IMG_LoadTexture(renderer, "assets/gman36.png");
            break;
        }
        break;
    default:
        break;
    }

    if (player.movement_direction) {
        player.img = (player.tick / 10) % 6;
        player.tick = (player.tick + 1) % 60;
    }

    SDL_GetTextureSize(playerTexture, &rect.w, &rect.h);
    SDL_RenderTexture(renderer, playerTexture, NULL, &rect);
    SDL_DestroyTexture(playerTexture);
}
