#include "miniaudio.h"
#include "bullet.h"
#include <SDL3/SDL.h>
#include <SDL3_image/SDL_image.h>

static const float W = 800, H = 500;
static const float speed1 = 5, speed2 = 3.5;

static SDL_Texture* bullet_texture;

void bullet_init(Bullet* bullet, float x, float y, int direction,  ma_sound* bullet_sound) {
    bullet->x = x;
    bullet->y = y;
    bullet->direction = direction;
    bullet->active = true;
    ma_sound_set_volume(bullet_sound, 4.2f);
    ma_sound_start(bullet_sound);
    ma_sound_seek_to_pcm_frame(bullet_sound, 0);
}

void bullet_init_texture(SDL_Renderer* renderer) {
    bullet_texture = IMG_LoadTexture(renderer, "assets/bullet3.png");
}

bool bullet_update(Bullet* bullet) {
    if (!bullet->active) return false;

    switch (bullet->direction) {
    case 1:
        bullet->x -= speed2;
        bullet->y += speed2;
        break;
    case 2:
        bullet->y += speed1;
        break;
    case 3:
        bullet->x += speed2;
        bullet->y += speed2;
        break;
    case 4:
        bullet->x += speed1;
        break;
    case 5:
        bullet->x += speed2;
        bullet->y -= speed2;
        break;
    case 6:
        bullet->y -= speed1;
        break;
    case 7:
        bullet->x -= speed2;
        bullet->y -= speed2;
        break;
    case 8:
        bullet->x -= speed1;
        break;
    }

    if (bullet->x < -4 || bullet->x > W || bullet->y < -4 || bullet->y > H) {
        bullet->active = false;
        return false;
    }

    return true;
}

void bullet_render(const Bullet* bullet, SDL_Renderer* renderer) {
    if (!bullet->active) return;
    SDL_FRect rect = { bullet->x - 2, bullet->y - 2, 4, 4 };

    SDL_GetTextureSize(bullet_texture, &rect.w, &rect.h);
    SDL_RenderTexture(renderer, bullet_texture, NULL, &rect);
}

void bullet_delete_textures() {
    SDL_DestroyTexture(bullet_texture);
}
