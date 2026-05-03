#include <SDL3/SDL.h>
#include <SDL3_image/SDL_image.h>
#include "bonuses.h"
#include "player.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

typedef struct BonusNode {
    Bonus bonus;
    struct BonusNode* next;
} BonusNode;

static BonusNode* bonus_list = NULL;
static Uint32 last_spawn = 0;


static const float SPAWN_POSITIONS[4][2] = {
    {220, 200},
    {580, 200},
    {580, 300},
    {220, 300}
};

void bonuses_init(SDL_Renderer* renderer) {
    bonus_list = NULL;
    last_spawn = SDL_GetTicks();
    bonus_init_textures(renderer);
}

void bonuses_update(float player_x, float player_y, Player* player, SDL_Renderer* renderer) {
    Uint32 now = SDL_GetTicks();
    if (now - last_spawn >= 7500) {
        BonusNode* new_node = malloc(sizeof(BonusNode));
        int position_index = rand() % 4;
        float bx = SPAWN_POSITIONS[position_index][0];
        float by = SPAWN_POSITIONS[position_index][1];
        bonus_init(&new_node->bonus, bx, by);
        new_node->next = bonus_list;
        bonus_list = new_node;
        new_node->bonus.bonus_type = rand() % 6;
        last_spawn = now;
    }

    BonusNode* ptr = bonus_list;
    while (ptr) {
        if (!ptr->bonus.taken) {
            float distance = abs(player_x - ptr->bonus.x) + abs(player_y - ptr->bonus.y);

            if (distance <= 30) {
                ptr->bonus.taken = true;
                switch (ptr->bonus.bonus_type) {
                case 0:
                    player->have_bonus_speed = true;
                    break;

                case 1:
                    player->have_bonus_shield = true;
                    break;

                case 2:
                    player->have_bonus_fast_shot = true;;
                    break;

                case 3:
                    player->have_bonus_all_dir = true;
                    break;

                case 4:
                    player->hp++;
                    break;

                case 5:
                    player->damage++;
                    break;
                }

            }
        }
        ptr = ptr->next;
    }
}

void bonuses_render(SDL_Renderer* renderer) {
    bonuses_back_render(renderer);
    for (BonusNode* node = bonus_list; node; node = node->next) {
        bonus_render(&node->bonus, renderer);
    }
}

void bonuses_clear(void) {
    while (bonus_list) {
        BonusNode* to_remove = bonus_list;
        bonus_list = bonus_list->next;
        free(to_remove);
    }
    bonus_delete_textures();
}
