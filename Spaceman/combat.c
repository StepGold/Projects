#include "SDL3/SDL.h"
#include "enemy.h"
#include "bullet.h"
#include "player.h"
#include <stdlib.h>
#include <stdio.h>
#include <walls.h>
#define MIN(a, b) ((a) < (b) ? (a) : (b))

bool intersect(float x1, float y1, float w1, float h1,
	float x2, float y2, float w2, float h2) {
	return (x1 - 3 <= x2 + w2 && x1 + w1 + 3 >= x2 && y1 - 3 <= y2 + h2 && y1 + h1 + 3 >= y2);
}

void combat_enemy_player(Enemy* enemy, Player* player) {
	if (!player->bonus_shield) {
		player->hp -= enemy->damage;
	}
}

void combat_bullet_enemy(Bullet* bullet, Enemy* enemy, Player* player) {
	if (bullet->active) {
		if (bullet->x > enemy->x - 6 && bullet->x < enemy->x + 36 && bullet->y > enemy->y - 6 && bullet->y < enemy->y + 36) {
			enemy->hp -= player->damage;
			bullet->active = false;
		}
	}
}

void combat_bullet_wall(Bullet* bullet) {
	if (!bullet->active) return;

	int walls_count = 0;
	const Wall* walls = get_walls_coordinates(&walls_count);
	int* indexes = get_walls_indexes();
	for (int i = 0; i < walls_count; i++) {
		float wall_x = MIN(walls[indexes[i]].x1, walls[indexes[i]].x2);
		float wall_y = MIN(walls[indexes[i]].y1, walls[indexes[i]].y2);
		float wall_w = abs(walls[indexes[i]].x2 - walls[indexes[i]].x1);
		float wall_h = abs(walls[indexes[i]].y2 - walls[indexes[i]].y1);

		if (intersect(bullet->x, bullet->y, 4, 4, wall_x, wall_y, wall_w, wall_h)) {
			bullet->active = false;
			break;
		}
	}
}
