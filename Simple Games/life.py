import random


def proris(li):
    for i in range(0, 200):
        for j in range(0, 200):
            if li[i][j]:
                pygame.draw.rect(sc, (255, 255, 255), (i*5, j*5, 5, 5))


def cnt(li, n, m):
    k = 0
    if li[n+1][m+1]:
        k += 1
    if li[n-1][m-1]:
        k += 1
    if li[n+1][m-1]:
        k += 1
    if li[n-1][m+1]:
        k += 1
    if li[n+1][m]:
        k += 1
    if li[n][m+1]:
        k += 1
    if li[n-1][m]:
        k += 1
    if li[n][m-1]:
        k += 1

    return k


def opr(li, x, y):
    if li[x][y] == 1:
        if 1 < cnt(li, x, y) < 4:
            return 1
        else: return 0
    else:
        if 2 < cnt(li, x, y) < 4:
            return 1
        else: return 0



def obr(li):
    li1 = []
    for _ in range(200):
        li1.append([0] * 200)

    for i in range(1, 199):
        for j in range(1, 199):
            li1[i][j] = opr(li, i, j)

    return li1



import pygame
pygame.init()


BLACK = (0, 0, 0)
FPS = 5
fl = True


sc = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()


li = []
for _ in range(200):
    li.append([0]* 200)

s = []
for _ in range(10000):
    aa = random.randint(10, 190)
    bb = random.randint(10, 190)
    ss = str(aa) + ' ' + str(bb)
    s.append(ss)

#s = ['50 47', '50 50', '51 51 ', '46 46', '46 47', '43 43', '43 42', '43 41', '43 40', '44 44', '45 45', '49 51', '46 46', '44 44', '43 43', '43 44', '42 45', '42 43', '45 46', '46 45', '50 46', '51 48', '50 48', '49 48', '48 47', '47 47', '47 46', '48 46']
for a in s:
    b, c = map(int, a.split())
    li[b][c] = 1

while fl:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fl = False

    sc.fill(BLACK)
    li = obr(li).copy()
    proris(li)

    pygame.display.flip()



pygame.quit()
