#include <SDL3_image/SDL_image.h>
#include <SDL3_ttf/SDL_ttf.h>
#include "miniaudio.h"
#include "enemy.h"
#include "player.h"
#include "bullets.h"
#include "bullet.h"
#include "combat.h"
#include "walls.h"
#include <stdlib.h>
#include <stdio.h>
#include "string.h"

SDL_Surface* text_surface;
static TTF_Font* font_enemy_lvl;
SDL_Texture* enemy_lvl_text;
static SDL_Color text_color = { 255, 255, 255, 255 };

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

static const float W = 800, H = 500;
static const float speed1 = 5, speed2 = 2;

static SDL_Texture* monster1;
static SDL_Texture* monster2;
static SDL_Texture* monster3;
static SDL_Texture* monster4;
static SDL_Texture* monster5;
static SDL_Texture* monster6;
static SDL_Texture* monster7;

void init_enemy_font(SDL_Renderer* renderer) {
	font_enemy_lvl = TTF_OpenFont("assets/font.ttf", 19);
}

void enemy_init(Enemy* enemy, float x, float y, int hp, int damage) {
	enemy->x = x;
	enemy->y = y;
	enemy->hp = hp;
	enemy->maxHp = hp;
	enemy->damage = damage;
	enemy->attack = false;
	enemy->img = 0;
	enemy->tick_img = 0;
	enemy->tick = 0;
	enemy->wall_movement = 0;
	enemy->wall_tick = 0;
}

bool intersection(float x1, float y1, float* wx, float* wy, float* ww, float* wh) {
	bool blocked = false;
	float wall_x;
	float wall_y;
	float wall_w;
	float wall_h;
	int walls_count;
	const int* walls = get_walls_indexes();
	const Wall* walls_coordinates = get_walls_coordinates(&walls_count);
	for (int i = 0; i < walls_count; i++) {
		wall_x = walls_coordinates[walls[i]].x1;
		wall_y = walls_coordinates[walls[i]].y1;
		wall_w = abs(walls_coordinates[walls[i]].x2 - walls_coordinates[walls[i]].x1);
		wall_h = abs(walls_coordinates[walls[i]].y2 - walls_coordinates[walls[i]].y1);

		blocked = intersect(x1, y1, 30, 30, wall_x, wall_y, wall_w, wall_h);
		if (blocked) {
			*wx = wall_x;
			*wy = wall_y;
			*ww = wall_w;
			*wh = wall_h;
			return true;
		}
	}
	return false;

}
void enemy_init_textures(SDL_Renderer* renderer) {
	monster1 = IMG_LoadTexture(renderer, "assets/monster1.png");
	monster2 = IMG_LoadTexture(renderer, "assets/monster2.png");
	monster3 = IMG_LoadTexture(renderer, "assets/monster3.png");
	monster4 = IMG_LoadTexture(renderer, "assets/monster4.png");
	monster5 = IMG_LoadTexture(renderer, "assets/monster5.png");
	monster6 = IMG_LoadTexture(renderer, "assets/monster6.png");
	monster7 = IMG_LoadTexture(renderer, "assets/monster7.png");
}

bool enemy_update(Enemy* enemy, Player* player, ma_sound* monster_death_sound) {
	int distance = abs(player->x - enemy->x) + abs(player->y - enemy->y);
	enemy->attack = distance <= 50;

	for (BulletNode* node = bullets_get_list(); node; node = node->next) {
		combat_bullet_enemy(&node->bullet, enemy, player);
	}

	if (enemy->hp > 0) {
		if (enemy->tick == 0 && enemy->attack) {
			enemy->tick = 180;
			combat_enemy_player(enemy, player);
		}
		else if (enemy->tick < 60) {
			if (enemy->wall_tick) {
				if (enemy->wall_movement == 1) {
					enemy->x += speed2;
				}
				else if (enemy->wall_movement == 2) {
					enemy->y -= speed2;
				}
				else if (enemy->wall_movement == 3) {
					enemy->x -= speed2;
				}
				else if (enemy->wall_movement == 4) {
					enemy->y += speed2;
				}
				enemy->wall_tick -= 1;
			}
			else {
				float wx = 0, wy = 0, ww = 0, wh = 0;
				float dx = player->x - enemy->x;
				float dy = player->y - enemy->y;
				float path = MAX(abs(dx), abs(dy));
				if (intersection(enemy->x, enemy->y + (dy > 0 ? 2 : -2), &wx, &wy, &ww, &wh) || intersection(enemy->x + (dx > 0 ? 2 : -2), enemy->y, &wx, &wy, &ww, &wh)) {
					if (intersection(enemy->x, enemy->y + (dy > 0 ? 2 : -2), &wx, &wy, &ww, &wh)) {
						if (abs(dx) > 150) {
							if (dx > 0) {
								enemy->x += speed2;
							}
							else {
								enemy->x -= speed2;
							}
						}
						else {
							if (wx + ww - enemy->x - 15 < enemy->x + 15 - wx) {
								enemy->x += speed2;
							}
							else {
								enemy->x -= speed2;
							}
							if (!intersection(enemy->x, enemy->y + (dy > 0 ? 2 : -2), &wx, &wy, &ww, &wh)) {
								enemy->wall_tick = 18;
								enemy->wall_movement = (dy > 0 ? 4 : 2);
							}
						}
					}
					else {
						if (abs(dy) > 100) {
							if (dy > 0) {
								enemy->y += speed2;
							}
							else {
								enemy->y -= speed2;
							}
						}
						else {
							if (wy + wh - enemy->y - 15 < enemy->y + 15 - wy) {
								enemy->y += speed2;
							}
							else {
								enemy->y -= speed2;
							}
							if (!intersection(enemy->x + (dx > 0 ? 2 : -2), enemy->y, &wx, &wy, &ww, &wh)) {
								enemy->wall_tick = 18;
								enemy->wall_movement = (dx > 0 ? 1 : 3);
							}
						}
					}
				}
				else if (path == abs(dy)) {
					if (dy > 0) {
						enemy->y += speed2;
					}
					else {
						enemy->y -= speed2;
					}
				}
				else {
					if (dx > 0) {
						enemy->x += speed2;
					}
					else {
						enemy->x -= speed2;
					}
				}
			}
		}
	}
	else {
		ma_sound_set_volume(monster_death_sound, 0.55f);
		ma_sound_start(monster_death_sound);
		ma_sound_seek_to_pcm_frame(monster_death_sound, 0);
	}
	if (enemy->tick > 0) {
		enemy->tick -= 1;
	}

	return enemy->hp > 0;

}

void enemy_render(Enemy* enemy, SDL_Renderer* renderer) {
	if (enemy->hp <= 0) {
		return;
	}

	SDL_FRect scale = { enemy->x, enemy->y - 15, 30, 8 };
	SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
	SDL_RenderFillRect(renderer, &scale);
	SDL_FRect hp_scale = { enemy->x + 2, enemy->y - 13, 26 * ((double)enemy->hp / (double)enemy->maxHp), 4 };
	SDL_SetRenderDrawColor(renderer, 0, 200, 0, 255);
	SDL_RenderFillRect(renderer, &hp_scale);
	SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
	if (enemy->maxHp > 1 && enemy->maxHp < 6) {
		for (int i = 1; i < enemy->hp; i++) {
			SDL_FRect bar_rect = { enemy->x + (26.0f / (float)enemy->maxHp) * i + 2, enemy->y - 15, 1, 8};
			SDL_RenderFillRect(renderer, &bar_rect);
		}
	}

	SDL_FRect enemy_lvl_rect = { enemy->x - 8, enemy->y - 24, 0, 0 };
	char* buf[4];
	int lvl_number = (((player.wave / 10) * 4 + (player.wave % 10) / 2 - 1) - 1) / 4 + 1;
	_itoa_s(lvl_number, buf, 4, 10);
	text_surface = TTF_RenderText_Solid(font_enemy_lvl, buf, strlen(buf), text_color);
	enemy_lvl_text = SDL_CreateTextureFromSurface(renderer, text_surface);
	if (lvl_number > 9) {
		enemy_lvl_rect.x = enemy->x - 14;
	}
	SDL_GetTextureSize(enemy_lvl_text, &enemy_lvl_rect.w, &enemy_lvl_rect.h);
	SDL_DestroySurface(text_surface);
	SDL_RenderTexture(renderer, enemy_lvl_text, NULL, &enemy_lvl_rect);
	SDL_DestroyTexture(enemy_lvl_text);

	SDL_FRect rect = { enemy->x, enemy->y, 30, 30 };
	SDL_Texture* enemyTexture = NULL;
	switch (enemy->img) {
	case 0:
		enemyTexture = monster1;
		break;
	case 1:
		enemyTexture = monster2;
		break;
	case 2:
		enemyTexture = monster3;
		break;
	case 3:
		enemyTexture = monster4;
		break;
	case 4:
		enemyTexture = monster5;
		break;
	case 5:
		enemyTexture = monster6;
		break;
	case 6:
		enemyTexture = monster7;
		break;
	}

	enemy->img = (enemy->tick_img / 10) % 7;
	enemy->tick_img = (enemy->tick_img + 1) % 60;

	SDL_GetTextureSize(enemyTexture, &rect.w, &rect.h);
	SDL_RenderTexture(renderer, enemyTexture, NULL, &rect);
}

void enemy_delete_textures() {
	SDL_DestroyTexture(monster1);
	SDL_DestroyTexture(monster2);
	SDL_DestroyTexture(monster3);
	SDL_DestroyTexture(monster4);
	SDL_DestroyTexture(monster5);
	SDL_DestroyTexture(monster6);
	SDL_DestroyTexture(monster7);
	TTF_CloseFont(font_enemy_lvl);
}