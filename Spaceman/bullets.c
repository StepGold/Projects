#include "bullets.h"
#include <stdlib.h>
#include <combat.h>

static BulletNode* bullet_list = NULL;

void bullets_init(void) {
    bullet_list = NULL;
}

void bullets_add(float x0, float y0, int direction, SDL_Renderer* renderer, ma_sound* bullet_sound) {
    BulletNode* new_node = malloc(sizeof(BulletNode));

    float x, y;

    switch (direction)
    {
    case 1:
        x = x0 - 4;
        y = y0 + 40;
        break;
    case 2:
        x = x0 + 8;
        y = y0 + 40;
        break;
    case 3:
        x = x0 + 20;
        y = y0 + 40;
        break;
    case 4:
        x = x0 + 20;
        y = y0 + 18;
        break;
    case 5:
        x = x0 + 20;
        y = y0 - 4;
        break;
    case 6:
        x = x0 + 8;
        y = y0 - 4;
        break;
    case 7:
        x = x0 - 4;
        y = y0 - 4;
        break;
    case 8:
        x = x0 - 4;
        y = y0 + 18;
        break;
    default:
        x = x0 + 20;
        y = y0 + 18;
        break;
    }

    bullet_init(&new_node->bullet, x, y, direction, bullet_sound);
    bullet_init_texture(renderer);
    new_node->next = bullet_list;
    bullet_list = new_node;
}

int bullets_update(void) {
    int active_count = 0;
    BulletNode** ptr = &bullet_list;
    for (BulletNode* node = bullets_get_list(); node; node = node->next) {
        combat_bullet_wall(&node->bullet);
    }

    while (*ptr) {
        if (bullet_update(&(*ptr)->bullet)) {
            active_count++;
            ptr = &(*ptr)->next;
        }
        else {
            BulletNode* to_remove = *ptr;
            *ptr = (*ptr)->next;
            free(to_remove);
        }
    }

    return active_count;
}

void bullets_render(SDL_Renderer* renderer) {
    for (BulletNode* node = bullet_list; node; node = node->next) {
        bullet_render(&node->bullet, renderer);
    }
}

void bullets_clear(void) {
    while (bullet_list) {
        BulletNode* to_remove = bullet_list;
        bullet_list = bullet_list->next;
        free(to_remove);
    }
    bullet_delete_textures();
}

const BulletNode* bullets_get_list(void) {
    return bullet_list;
}
