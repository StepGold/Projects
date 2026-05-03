#include "SDL3/SDL.h"
#include "miniaudio.h"
#include "enemies.h"
#include "player.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

static EnemyNode* enemy_list = NULL;

int get_random_number(int number) {
    static int initialized = 0;
    if (!initialized) {
        srand(time(NULL));
        initialized = 1;
    }

    return rand() % number;
}


void enemies_init(SDL_Renderer* renderer) {
    enemy_list = NULL;
    enemy_init_textures(renderer);
    init_enemy_font(renderer);
}

void enemies_create_wave(int wave) {
    float spawn_x[] = { 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 785, 785, 785, 785, 785, 785, 785, 785, 785, 785 };
    float spawn_y[] = { 5, 50, 150, 100, 200, 250, 300, 350, 400, 450, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 50, 100, 150, 200, 250, 300, 350, 400, 450 };

    int count = wave % 10;
    int index;

    for (int i = 0; i < count; i++) {
        index = get_random_number(33);
        enemies_add(spawn_x[index], spawn_y[index], wave);
    }
}

void enemies_add(float x, float y, int wave) {
    EnemyNode* new_node = malloc(sizeof(EnemyNode));

    int hp, damage;

    hp = wave / 10 + 1;
    damage = wave / 10 + 1;

    enemy_init(&new_node->enemy, x, y, hp, damage);
    new_node->next = enemy_list;
    enemy_list = new_node;
}

void enemies_update(Player* player, ma_sound* monster_death_sound) {
    EnemyNode** ptr = &enemy_list;

    while (*ptr) {
        if (enemy_update(&(*ptr)->enemy, player, monster_death_sound)) {
            ptr = &(*ptr)->next;
        }
        else {
            EnemyNode* to_remove = *ptr;
            *ptr = (*ptr)->next;
        }
    }
}

bool enemies_all_dead(void) {
    return (enemy_list == NULL);
}

void enemies_render(SDL_Renderer* renderer) {
    for (EnemyNode* node = enemy_list; node; node = node->next) {
        enemy_render(&node->enemy, renderer);
    }
}

void enemies_clear(void) {
    while (enemy_list) {
        EnemyNode* to_remove = enemy_list;
        enemy_list = enemy_list->next;
        free(to_remove);
    }
    enemy_delete_textures();
}

const EnemyNode* enemies_get_list(void) {
    return enemy_list;
}