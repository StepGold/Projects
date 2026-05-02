import pygame
pygame.init()
import random

clock = pygame.time.Clock()
FPS = 2
sc = pygame.display.set_mode((1, 1))


def prov(x, y):
    j = True
    for i in a:
        if (x == i[0]) and (y == i[1]):
            j = False

    return j


def spawn(t):
    b, c = random.randint(1, 8), random.randint(1, 8)
    while not prov(b, c):
        b, c = random.randint(1, 8), random.randint(1, 8)

    return (b, c)


def nash():
    global fl
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                fl = 'u'
            elif event.key == pygame.K_RIGHT:
                fl = 'r'
            elif event.key == pygame.K_LEFT:
                fl = 'l'
            elif event.key == pygame.K_DOWN:
                fl = 'd'

    return


def nex(d, k):
    x, y = d[0], d[1]
    if k == 'r':
        return (x, y + 1)
    elif k == 'l':
        return (x, y - 1)
    elif k == 'u':
        return (x - 1, y)
    else:
        return (x + 1, y)


def vivod():
    for i in range(len(li)):
        print(*li[i])



li = [['_']*10] + [['|'] + ['*']*8 + ['|'] for gg in range(8)] + [['_']*10]
vivod()
a = [(1, 2), (1, 1)]
li[1][2], li[1][1] = '%', '$'
vivod()
go = True
fl = 'r'
k = 0

while go:
    nash()
    kor = nex(a[0], fl)

    if k % 2 == 0:
        apple = spawn(a)
        if '0' not in (li[1] + li[2] + li[2] + li[3] + li[4] + li[5] + li[6] + li[7] + li[8] + li[9]):
            li[apple[0]][apple[1]] = '0'

    if li[kor[0]][kor[1]] == '0':
        li[kor[0]][kor[1]] = '%'
        li[a[0][0]][a[0][1]] = '$'
        a = [kor] + a
    elif li[kor[0]][kor[1]] == '*':
        li[kor[0]][kor[1]] = '%'
        li[a[0][0]][a[0][1]] = '$'
        li[a[-1][0]][a[-1][1]] = '*'
        a = [kor] + a[:-1]
    else:
        break

    k += 1
    vivod()
    clock.tick(FPS)

