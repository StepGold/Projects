import pygame
pygame.init()
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

#Данные:
W = 1280
H = 780
FPS = 30
schet = 0
lin = [W/2, H/2]
xx = W/2
yy = H/2
xx1, sdf, udar =15, -30, 0
font = pygame.font.SysFont('arial',64,True)
font1 = pygame.font.SysFont('arial',46,True)
font2 = pygame.font.SysFont('arial',55,True)
font3 = pygame.font.SysFont('arial',75,True)
chit1 = False

#Цвета:
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,100,0)
GREEN1 = (0,255,0)
GREEN2 = (29, 88, 36)
BLUE = (44, 6, 74)
PURPLE = (255,0,255)
BIRUZ = (0,255,255)
YELLOW = (255,255,0)
COLORS = [RED,GREEN,BLUE,PURPLE,BIRUZ,YELLOW]

clock = pygame.time.Clock()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('STEPBALL')

bot_img = pygame.image.load(path.join(img_dir, "Bot.png")).convert()
igrok_img = pygame.image.load(path.join(img_dir, "Igrok.png")).convert()
ball2_img = pygame.image.load(path.join(img_dir, "BALL.png")).convert()
ball1_img = pygame.image.load(path.join(img_dir, "BALL1.png")).convert()
vrp1_img = pygame.image.load(path.join(img_dir, "Vratar1.png")).convert()
vr1_img = pygame.image.load(path.join(img_dir, "Vratar2.png")).convert()
vrr1_img = pygame.image.load(path.join(img_dir, "Vratar3.png")).convert()
vrp2_img = pygame.image.load(path.join(img_dir, "Vratar11.png")).convert()
vr2_img = pygame.image.load(path.join(img_dir, "Vratar22.png")).convert()
vrr2_img = pygame.image.load(path.join(img_dir, "Vratar33.png")).convert()
per_img = pygame.image.load(path.join(img_dir, "per.png")).convert()
but_img = pygame.image.load(path.join(img_dir, "but.png")).convert()
cup_img = pygame.image.load(path.join(img_dir, "cup.png")).convert()
g1v1_img = pygame.image.load(path.join(img_dir, "g1v1.png")).convert()
kv_w_img = pygame.image.load(path.join(img_dir, "kv1.png")).convert()
kv_r_img = pygame.image.load(path.join(img_dir, "kv2.png")).convert()
kv_g_img = pygame.image.load(path.join(img_dir, "kv3.png")).convert()
pobeda_img = pygame.image.load(path.join(img_dir, "Pobeda.png")).convert()
win_img = pygame.image.load(path.join(img_dir, "WIN.png")).convert()
los_img = pygame.image.load(path.join(img_dir, "LOS.png")).convert()
clickenter_img = pygame.image.load(path.join(img_dir, "Clickenter.png")).convert()
clickent_img = pygame.image.load(path.join(img_dir, "Clickent.png")).convert()
clickspace_img = pygame.image.load(path.join(img_dir, "Clickspace.png")).convert()
clickenterforstart_img = pygame.image.load(path.join(img_dir, "Clickenterforstart.png")).convert()
igrok1pobedil_img = pygame.image.load(path.join(img_dir, "Igrok1pobedil.png")).convert()
igrok2pobedil_img = pygame.image.load(path.join(img_dir, "Igrok2pobedil.png")).convert()
f8_img = pygame.image.load(path.join(img_dir, "f8.png")).convert()
f4_img = pygame.image.load(path.join(img_dir, "f4.png")).convert()
f2_img = pygame.image.load(path.join(img_dir, "f2.png")).convert()
f1_img = pygame.image.load(path.join(img_dir, "f1.png")).convert()
startent_img = pygame.image.load(path.join(img_dir, "Startent.png")).convert()
klava_img = pygame.image.load(path.join(img_dir, "klava1.png")).convert()

ball_img = ball2_img

vrp_img = vrp1_img
vr_img = vr1_img
vrr_img = vrr1_img

class Klava(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((500, 159))
        self.image = klava_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 250, H // 2 - 120

class Ent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((633, 47))
        self.image = startent_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 316, H // 2 + 85

class Final(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((322, 55))
        self.image = f8_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 161, H // 2 - 105

    def ff4(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((326, 51))
        self.image = f4_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 160, H // 2 - 105

    def ff2(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((324, 56))
        self.image = f2_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 160, H // 2 - 105

    def ff(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((197, 59))
        self.image = f1_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 120, H // 2 - 105

class Loss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((288, 65))
        self.image = los_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 154, H // 2 - 135
    def pust(self):
        self.image = pygame.Surface((1, 2))

class Winn(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((191, 62))
        self.image = win_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 115, H // 2 - 135
    def pust(self):
        self.image = pygame.Surface((1, 2))

class Clickent(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((304, 39))
        self.image = clickent_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 320, H // 2 + 70

class Clickspace(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 39))
        self.image = clickspace_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 + 31, H // 2 + 70

class Clickenterforstart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((635, 49))
        self.image = clickenterforstart_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 318, H // 2 + 95

class Igrokk1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((414, 64))
        self.image = igrok1pobedil_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 207, H // 2 - 135
    def pust(self):
        self.image = pygame.Surface((1, 1))

class Igrokk2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((414, 62))
        self.image = igrok2pobedil_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 207, H // 2 - 135
    def pust(self):
        self.image = pygame.Surface((1, 1))

class Clickenter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((647, 47))
        self.image = clickenter_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 323, H // 2 + 95

class Pobeda(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((276, 59))
        self.image = pobeda_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W // 2 - 145, H // 2 - 162

class kvad9(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 125, H - 115
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img

class kvad10(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 125, H - 37
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img

class kvad7(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 185, H - 115
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img
    def pust(self):
        self.image = pygame.Surface((45, 45))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(but_img, (1, 1))
        self.rect.x, self.rect.centery = W - 365, H - 115

class kvad8(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 185, H - 37
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img
    def pust(self):
        self.image = pygame.Surface((45, 45))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(but_img, (1, 1))
        self.rect.x, self.rect.centery = W - 365, H - 115

class kvad5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 245, H - 115
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img
    def pust(self):
        self.image = pygame.Surface((45, 45))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(but_img, (1, 1))
        self.rect.x, self.rect.centery = W - 365, H - 115

class kvad6(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 245, H - 37
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img
    def pust(self):
        self.image = pygame.Surface((45, 45))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(but_img, (1, 1))
        self.rect.x, self.rect.centery = W - 365, H - 115

class kvad3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 305, H - 115
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img
    def pust(self):
        self.image = pygame.Surface((45, 45))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(but_img, (1, 1))
        self.rect.x, self.rect.centery = W - 365, H - 115

class kvad4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 305, H - 37
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img
    def pust(self):
        self.image = pygame.Surface((45, 45))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(but_img, (1, 1))
        self.rect.x, self.rect.centery = W - 365, H - 115

class kvad1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 365, H - 115
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img
    def pust(self):
        self.image = pygame.Surface((45, 45))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(but_img, (1, 1))
        self.rect.x, self.rect.centery = W - 365, H - 115

class kvad2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image = kv_w_img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W - 365, H - 37
    def zab(self):
        self.image = kv_g_img
    def nezab(self):
        self.image = kv_r_img
    def pust(self):
        self.image = pygame.Surface((45, 45))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(but_img, (1, 1))
        self.rect.x, self.rect.centery = W - 365, H - 115

class Cup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = cup_img
        self.image.set_colorkey(GREEN2)
        self.image = pygame.transform.scale(cup_img, (92, 130))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W//2 - 215, H//2 - 40

    def win(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = cup_img
        self.image.set_colorkey(GREEN2)
        self.image = pygame.transform.scale(cup_img, (110, 160))
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = W//2, H//2 - 10

class G1v1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = g1v1_img

        self.image = pygame.transform.scale(g1v1_img, (120, 120))
        self.image.set_colorkey(GREEN2)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.centery = W//2 + 100, H//2 - 20

class Perchi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = per_img
        self.image.set_colorkey(GREEN1)
        self.image = pygame.transform.scale(per_img, (130, 130))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W - 150, 15

    def pust(self):
        self.image = pygame.Surface((100, 100))
        self.image = per_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(per_img, (1, 1))
        self.rect.x, self.rect.y = W - 150, 50

class Butsi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = but_img
        self.image.set_colorkey(GREEN1)
        self.image = pygame.transform.scale(but_img, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = W - 150, 25

    def pust(self):
        self.image = pygame.Surface((100, 100))
        self.image = but_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(but_img, (1, 1))
        self.rect.x, self.rect.y = W - 150, 50


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 70))
        self.image = ball_img
        self.image.set_colorkey(GREEN2)
        self.rect = self.image.get_rect()
        self.rect.center = (W / 2 - 10, H / 2  + 180)

    #ЕДЕНИЦА111111111111
    def ball11(self, ww, hh):
        ww, hh = ww - 5, hh - 5
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        self.image.set_colorkey(GREEN2)
        self.rect.x += -38
        self.rect.y += -34

        if self.rect.x < 380 and self.rect.y < 340 :
            self.rect.x += -25
            self.rect.y += -22
            ww, hh = ww - 5, hh - 5
            self.image = pygame.transform.scale(ball_img, (ww, hh))
            return(1, ww, hh)
        else:
            return(0, ww, hh)

    def ball12(self, speedx, f):
        self.rect.x += speedx
        if speedx > 0 :
            return(1, speedx - 1,f)
        elif f == 30:
            return(2, 0, f)
        else:
            return(1, 0, f+1)

    #ДВОЙКА2222222222222
    def ball21(self, ww, hh):
        ww, hh = ww - 6, hh - 6
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        self.image.set_colorkey(GREEN2)
        self.rect.x += 0
        self.rect.y += -40
        if self.rect.y < 320:
            return(1, ww, hh, 1)
        elif self.rect.y < 340:
            return (0, ww, hh, 1)
        else:
            return(0, ww, hh, 0)

    def ball22(self, speedx,f,kof):
        if speedx != -13:
            self.rect.y -= speedx
            if kof == 7:
                speedx -= 1
                return(1, speedx,f,kof)
            else: return(1, speedx,f,kof + 1)
        elif f == 30:
            return(2, -13, f,kof)
        else:
            return(1, -13, f+1,kof)

    #ТРОЙКА333333333
    def ball31(self, ww, hh):
        ww, hh = ww - 5, hh - 5
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        self.image.set_colorkey(GREEN2)
        self.rect.x += 48
        self.rect.y += -34

        if self.rect.x > 860 and self.rect.y < 340 :
            self.rect.x += 28
            self.rect.y += -21
            ww, hh = ww - 5, hh - 5
            self.image = pygame.transform.scale(ball_img, (ww, hh))
            return(1, ww, hh)
        else:
            return(0, ww, hh)

    def ball32(self, speedx,f):
        self.rect.x += speedx
        if speedx != 0 :
            return(1, speedx + 1, f)
        elif f == 30:
            return(2, 0, f)
        else: return(1, 0, f+1)

    #ЧЕТВЕРКА4444444444
    def ball41(self, ww, hh,g):
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        self.image.set_colorkey(GREEN2)
        if self.rect.x < 390 and self.rect.y < 330 and g != 5:
            self.rect.x += -5
            return(0, ww, hh, g+1, 1)
        elif g == 5:
            return(1, ww, hh, g, 1)
        else:
            ww, hh = ww - 6, hh - 6
            self.rect.x += -35
            self.rect.y += -50
            return(0,ww,hh,g, 0)

    def ball42(self, speedx):
        self.rect.y += speedx
        if self.rect.y < 310:
            return (1, speedx + 1)
        else:
            return (2, 8)

    def ball43(self, speedx):
        self.rect.y -= speedx
        if speedx > 0:
            return (2, speedx - 1)
        else:
            return (3, 7)

    def ball44(self, speedx, f):
        self.rect.y += speedx
        if speedx > 0:
            return (3, speedx - 1, f)
        elif f == 30:
            return (4, 0, f)
        else:
            return (3, 0, f + 1)

    # ПЯТЕРКА55555555555
    def ball51(self, ww, hh, g):
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        self.image.set_colorkey(GREEN2)
        if self.rect.y < 230 and g != 5:
            return (0, ww, hh, g + 1,1)
        elif g == 5:
            return (1, ww, hh, g,1)
        else:
            ww, hh = ww - 5, hh - 5
            self.rect.x += 3
            self.rect.y += -45
            return (0, ww, hh, g,0)

    def ball52(self, speedx):
        self.rect.y += speedx
        if self.rect.y < 310:
            return (1, speedx + 1)
        else:
            return (2, 8)

    def ball53(self, speedx):
        self.rect.y -= speedx
        if speedx > 0:
            return (2, speedx - 1)
        else:
            return (3, 7)

    def ball54(self, speedx, f):
        self.rect.y += speedx
        if speedx > 0:
            return (3, speedx - 1, f)
        elif f == 30:
            return (4, 0, f)
        else:
            return (3, 0, f + 1)




    #ШЕСТРЕКА666666666
    def ball61(self, ww, hh,g):
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        self.image.set_colorkey(GREEN2)
        if self.rect.x > 860 and self.rect.y < 330 and g != 5:
            self.rect.x += 5
            return(0, ww, hh, g+1, 1)
        elif g == 5:
            return(1, ww, hh, g, 1)
        else:
            ww, hh = ww - 6, hh - 6
            self.rect.x += 48
            self.rect.y += -50
            return(0,ww,hh,g, 0)

    def ball62(self, speedx):
        self.rect.y += speedx
        if self.rect.y < 310:
            return (1, speedx + 1)
        else:
            return (2, 8)

    def ball63(self, speedx):
        self.rect.y -= speedx
        if speedx > 0:
            return (2, speedx - 1)
        else:
            return (3, 7)

    def ball64(self, speedx, f):
        self.rect.y += speedx
        if speedx > 0:
            return (3, speedx - 1, f)
        elif f == 30:
            return (4, 0, f)
        else:
            return (3, 0, f + 1)

    # СЕМЕРКА7777777
    def ball71(self, ww, hh,g):
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        self.image.set_colorkey(GREEN2)
        if self.rect.x < 390 and self.rect.y < 330 and g != 5:
            self.rect.x += -5
            return(0, ww, hh, g+1, 1)
        elif g == 5:
            return(1, ww, hh, g, 1)
        else:
            ww, hh = ww - 6, hh - 6
            self.rect.x += -35
            self.rect.y += -62
            return(0,ww,hh,g, 0)

    def ball72(self, speedx):
        self.rect.y += speedx
        if self.rect.y < 300:
            return (1, speedx + 1)
        else:
            return (2, 12)

    def ball73(self, speedx):
        self.rect.y -= speedx
        if speedx > 0:
            return (2, speedx - 1)
        else:
            return (3, 11)

    def ball74(self, speedx, f):
        self.rect.y += speedx
        if speedx > 0:
            return (3, speedx - 1, f)
        elif f == 30:
            return (4, 0, f)
        else:
            return (3, 0, f + 1)

    #ВОСЬМЕРКА8888888888

    def ball81(self, ww, hh, g):
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        self.image.set_colorkey(GREEN2)
        if self.rect.y < 185 and g != 5:
            return (0, ww, hh, g + 1, 1)
        elif g == 5:
            return (1, ww, hh, g, 1)
        else:
            ww, hh = ww - 6, hh - 6
            self.rect.y += -65
            return (0, ww, hh, g, 0)

    def ball82(self, speedx):
        self.rect.y += speedx
        if self.rect.y < 320:
            return (1, speedx + 1)
        else:
            return (2, 12)

    def ball83(self, speedx):
        self.rect.y -= speedx
        if speedx > 0:
            return (2, speedx - 1)
        else:
            return (3, 11)

    def ball84(self, speedx, f):
        self.rect.y += speedx
        if speedx > 0:
            return (3, speedx - 1, f)
        elif f == 30:
            return (4, 0, f)
        elif f == 0:
            self.rect.y += -2
            return (3, 0, f + 1)
        else:
            return (3, 0, f + 1)

    #ДЕВЯТКА9999999
    def ball91(self, ww, hh,g):
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        self.image.set_colorkey(GREEN2)
        if self.rect.x > 860 and self.rect.y < 330 and g != 5:
            self.rect.x += 5
            return(0, ww, hh, g+1, 1)
        elif g == 5:
            return(1, ww, hh, g, 1)
        else:
            ww, hh = ww - 6, hh - 6
            self.rect.x += 46
            self.rect.y += -62
            return(0,ww,hh,g, 0)

    def ball92(self, speedx):
        self.rect.y += speedx
        if self.rect.y < 300:
            return (1, speedx + 1)
        else:
            return (2, 12)

    def ball93(self, speedx):
        self.rect.y -= speedx
        if speedx > 0:
            return (2, speedx - 1)
        else:
            return (3, 11)

    def ball94(self, speedx, f):
        self.rect.y += speedx
        if speedx > 0:
            return (3, speedx - 1, f)
        elif f == 30:
            return (4, 0, f)
        elif f == 0:
            self.rect.y += -2
            return (3, 0, f + 1)
        else:
            return (3, 0, f + 1)

    def ballotbv(self, speedx):
        self.rect.y -= speedx
        return(speedx - 1)

    def ballotbg(self, speedx):
        self.rect.x += speedx
        if speedx > 0:
            return(speedx - 1)
        else: return(speedx + 1)

    def ballotbgg(self, speedx, speedy):
        self.rect.x += speedx
        self.rect.y += speedy
        if speedx > 0:
            return(speedx - 0.5, speedy + 0.2)
        else: return(speedx + 0.5, speedy + 0.2)

    def ballotb2(self, speedx, ww, hh):
        self.rect.y += speedx
        self.image = pygame.transform.scale(ball_img, (ww, hh))
        return(speedx - 1, ww + 1, hh + 1)

    def ballotb51(self, speedx):
        self.rect.y += speedx
        if self.rect.y < 350:
            return(1, speedx + 1)
        else: return(2, 9)

    def ballotb52(self, speedx):
        self.rect.y -= speedx
        if speedx != 0 :
            return(2, speedx - 1)
        else: return(3, 0)

    def ballotb53(self, speedx):
        self.rect.y += speedx
        if speedx != 9 :
            return(3, speedx + 1)
        else: return(4, 10)



def goal1(f,udar, speedx, flag,ww,hh, flagdraw):
    if udar == 0:
        udar,ww,hh = ball.ball11(ww,hh)
    if udar == 1:
        udar, speedx, f = ball.ball12(speedx, f)
        flagdraw = False
    if udar == 2:
        flag = False
    return(f,udar, speedx, flag, ww, hh, flagdraw)

def goal2(f,udar, speedx, flag,ww,hh,kof, flagdraw):
    if udar == 0:
        udar,ww,hh, q = ball.ball21(ww,hh)
    if udar == 1:
        flagdraw = False
        udar, speedx,f,kof = ball.ball22(speedx,f,kof)
    if udar == 2:
        flag = False
    return(f,udar, speedx, flag, ww, hh,kof, flagdraw)

def goal3(f,udar, speedx, flag,ww,hh, flagdraw):
    if udar == 0:
        udar,ww,hh = ball.ball31(ww,hh)
    if udar == 1:
        flagdraw = False
        udar, speedx,f = ball.ball32(speedx,f)
    if udar == 2:
        flag = False
    return(f,udar, speedx, flag, ww, hh, flagdraw)

def goal4(f, g, udar, speedx, flag,ww,hh, flagdraw):
    if udar == 0:
        udar,ww,hh, g, mjk = ball.ball41(ww,hh,g)
    if udar == 1:
        flagdraw = False
        udar, speedx = ball.ball42(speedx)
    if udar == 2:
        udar, speedx = ball.ball43(speedx)
    if udar == 3:
        udar, speedx, f = ball.ball44(speedx, f)
    if udar == 4:
        flag = False
    return(f,g,udar, speedx, flag, ww, hh, flagdraw)

def goal5(f, g, udar, speedx, flag,ww,hh, flagdraw):
    if udar == 0:
        udar,ww,hh, g, mjk = ball.ball51(ww,hh,g)
    if udar == 1:
        flagdraw = False
        udar, speedx = ball.ball52(speedx)
    if udar == 2:
        udar, speedx = ball.ball53(speedx)
    if udar == 3:
        udar, speedx, f = ball.ball54(speedx, f)
    if udar == 4:
        flag = False
    return(f,g,udar, speedx, flag, ww, hh, flagdraw)

def goal6(f, g, udar, speedx, flag,ww,hh, flagdraw):
    if udar == 0:
        udar,ww,hh, g, mgk = ball.ball61(ww,hh,g)
    if udar == 1:
        flagdraw = False
        udar, speedx = ball.ball62(speedx)
    if udar == 2:
        udar, speedx= ball.ball63(speedx)
    if udar == 3:
        udar, speedx, f = ball.ball64(speedx, f)
    if udar == 4:
        flag = False
    return(f,g,udar, speedx, flag, ww, hh, flagdraw)


def goal7(f, g, udar, speedx, flag,ww,hh, flagdraw):
    if udar == 0:
        udar,ww,hh, g,mjk = ball.ball71(ww,hh,g)
    if udar == 1:
        flagdraw = False
        udar, speedx= ball.ball72(speedx)
    if udar == 2:
        udar, speedx = ball.ball73(speedx)
    if udar == 3:
        udar, speedx, f = ball.ball74(speedx, f)
    if udar == 4:
        flag = False
    return(f,g,udar, speedx, flag, ww, hh, flagdraw)

def goal8(f, g, udar, speedx, flag,ww,hh, flagdraw):
    if udar == 0:
        udar,ww,hh, g, mjk = ball.ball81(ww,hh,g)
    if udar == 1:
        flagdraw = False
        udar, speedx= ball.ball82(speedx)
    if udar == 2:
        udar, speedx = ball.ball83(speedx)
    if udar == 3:
        udar, speedx, f = ball.ball84(speedx, f)
    if udar == 4:
        flag = False
    return(f,g,udar, speedx, flag, ww, hh, flagdraw)

def goal9(f, g, udar, speedx, flag,ww,hh, flagdraw):
    if udar == 0:
        udar,ww,hh, g, mjk = ball.ball91(ww,hh,g)
    if udar == 1:
        flagdraw = False
        udar, speedx= ball.ball92(speedx)
    if udar == 2:
        udar, speedx = ball.ball93(speedx)
    if udar == 3:
        udar, speedx, f = ball.ball94(speedx, f)
    if udar == 4:
        flag = False
    return(f,g,udar, speedx, flag, ww, hh, flagdraw)

def otbil1(udar, speedx,ww,hh, flag, q):
    q, f = vratar.vr1(q)
    if udar == 0:
        udar, ww, hh = ball.ball11(ww, hh)
    elif udar == 1 and speedx != 0:
        speedx = ball.ballotbg(speedx)
    if speedx == 0 and f:
        flag = False
    return(udar, speedx,ww,hh, flag, q)

def otbil2(udar, speedx,ww,hh, flag,m, flagdraw):
    if udar == 0:
        k, ww, hh, udar = ball.ball21(ww, hh)
    elif udar == 1 and speedx != 0:
        flagdraw = False
        speedx, ww, hh = ball.ballotb2(speedx, ww, hh)
    if speedx == 0 and m != 30:
        m += 1
    elif speedx == 0 and m == 30:
        flag = False
    return(udar, speedx,ww,hh, flag, m, flagdraw)

def otbil3(udar, speedx,ww,hh, flag, q):
    q, f = vratar.vr3(q)
    if udar == 0:
        udar, ww, hh = ball.ball31(ww, hh)
    elif udar == 1 and speedx != 0:
        speedx = ball.ballotbg(speedx)
    if speedx == 0 and f:
        flag = False
    return(udar, speedx,ww,hh, flag, q)

def otbil4(udar, speedx,ww,hh, flag, g, speedy,q):
    q, f = vratar.vr4(q)
    if udar == 0:
        x, ww, hh, g, udar = ball.ball41(ww, hh, g)
    elif udar == 1 and speedx != -9:
        speedx, speedy = ball.ballotbgg(speedx, speedy)
    if speedx == -9 and f:
        flag = False
    return(udar, speedx,ww,hh, flag, g, speedy,q)

def otbil5(udar, speedx, ww,hh, flag, g):
    if udar == 0:
        x, ww, hh, g, udar = ball.ball51(ww, hh, g)
    elif udar == 1:
        udar, speedx = ball.ballotb51(speedx)
    elif udar == 2:
        udar, speedx = ball.ballotb52(speedx)
    elif udar == 3:
        udar, speedx = ball.ballotb53(speedx)
    elif udar == 4 and g != 15:
        g += 1
    elif g == 15 and g == 15:
        flag = False
    return(udar, speedx, ww,hh, flag, g)


def otbil6(udar, speedx,ww,hh, flag, g, speedy, q):
    q, f = vratar.vr6(q)
    if udar == 0:
        x, ww, hh, g, udar = ball.ball61(ww, hh, g)
    elif udar == 1 and speedx != 9:
        speedx, speedy = ball.ballotbgg(speedx, speedy)
    if speedx == 9 and f:
        flag = False
    return(udar, speedx,ww,hh, flag, g, speedy, q)

def otbil7(udar, sp,ww,hh, flag, g, q):
    q, f = vratar.vr7(q)
    if udar == 0:
        x, ww, hh, g, udar = ball.ball71(ww, hh, g)
    elif udar == 1 and sp != 0:
        sp = ball.ballotbv(sp)
    if sp == 0 and f:
        flag = False
    return(udar, sp,ww,hh, flag, g, q)

def otbil8(udar, sp,ww,hh, flag, g, q):
    q, f = vratar.vr8(q)
    if udar == 0:
        x, ww, hh, g, udar = ball.ball81(ww, hh, g)
    elif udar == 1 and sp != 0:
        sp = ball.ballotbv(sp)
    if sp == 0 and f:
        flag = False
    return(udar, sp,ww,hh, flag, g, q)

def otbil9(udar, sp,ww,hh, flag, g, q):
    q, f = vratar.vr9(q)
    if udar == 0:
        x, ww, hh, g, udar = ball.ball91(ww, hh, g)
    elif udar == 1 and sp != 0:
        sp = ball.ballotbv(sp)
    if sp == 0 and f:
        flag = False
    return(udar, sp,ww,hh, flag, g, q)

class Vratar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((300, 188))
        self.image = vrp_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (W / 2, H / 2 - 110)


    def  vr1(self, q):
        if q == 0:
            self.image = pygame.transform.rotate(vrp_img, 6)
            return(q + 1, False)
        if q == 1:
            self.image = pygame.transform.rotate(vrp_img, 6)
            return(q + 1, False)
        if q == 2:
            self.image = pygame.transform.rotate(vrp_img, 6)
            return(q + 1, False)
        elif q == 3:
            x, y = self.rect.bottomright
            self.image = pygame.Surface((200, 126))
            self.image = vr_img
            self.image.set_colorkey(WHITE)
            self.rect.bottomright = x - 100, y + 20
            return(q + 1, False)
        elif q == 4:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 30, y
            return(q + 1, False)
        elif q == 5:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 30, y
            return(q + 1, False)
        elif q == 6:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 30, y
            return(q + 1, False)
        elif q == 7:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 15, y
            return (q + 1, False)
        elif q == 8:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 15, y
            return (q + 1, False)
        elif q == 9:
            return(q, True)

    def  vr3(self, q):
        if q == 0:
            self.image = pygame.transform.rotate(vrp_img, -6)
            return(q + 1, False)
        elif q == 1:
            self.image = pygame.transform.rotate(vrp_img, -6)
            return(q + 1, False)
        elif q == 2:
            self.image = pygame.transform.rotate(vrp_img, -6)
            return(q + 1, False)
        elif q == 3:
            x, y = self.rect.bottomright
            self.image = pygame.Surface((200, 126))
            self.image = vrr_img
            self.image.set_colorkey(WHITE)
            self.rect.bottomright = x + 100, y + 20
            return(q + 1, False)
        elif q == 4:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 25, y
            return(q + 1, False)
        elif q == 5:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 25, y
            return(q + 1, False)
        elif q == 6:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 25, y
            return(q + 1, False)
        elif q == 7:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 15, y
            return (q + 1, False)
        elif q == 8:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 15, y
            return (q + 1, False)
        elif q == 9:
            return(q, True)

    def vr4(self, q):
        if q == 0:
            self.image = pygame.transform.rotate(vrp_img, 8)
            return (q + 1, False)
        elif q == 1:
            self.image = pygame.transform.rotate(vrp_img, 8)
            return (q + 1, False)
        elif q == 2:
            self.image = pygame.transform.rotate(vrp_img, 8)
            return (q + 1, False)
        elif q == 3:
            x, y = self.rect.bottomright
            self.image = pygame.Surface((200, 126))
            self.image = vr_img
            self.image.set_colorkey(WHITE)
            self.image = pygame.transform.rotate(vr_img, -15)
            self.rect.bottomright = x - 50, y - 20
            return(q + 1, False)
        elif q == 4:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 28, y - 10
            return (q + 1, False)
        elif q == 5:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 28, y - 10
            return (q + 1, False)
        elif q == 6:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 28, y - 10
            return (q + 1, False)
        elif q == 7:
            self.image = pygame.transform.rotate(vr_img, 1)
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 25, y + 10
            return (q + 1, False)
        elif q == 8:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 25, y + 15
            return (q + 1, False)
        elif q == 9:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 20, y + 15
            return (q + 1, False)
        elif q == 10:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 15, y + 15
            return (q + 1, False)
        elif q == 11:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 7, y + 15
            return (q + 1, False)
        elif q == 12:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 4, y + 15
            return (q + 1, False)
        elif q == 13:
            return(q, True)


    def vr6(self, q):
        if q == 0:
            self.image = pygame.transform.rotate(vrp_img, -8)
            return (q + 1, False)
        elif q == 1:
            self.image = pygame.transform.rotate(vrp_img, -8)
            return (q + 1, False)
        elif q == 2:
            self.image = pygame.transform.rotate(vrp_img, -8)
            return (q + 1, False)
        elif q == 3:
            x, y = self.rect.bottomright
            self.image = pygame.Surface((200, 126))
            self.image = vrr_img
            self.image.set_colorkey(WHITE)
            self.image = pygame.transform.rotate(vrr_img, 15)
            self.rect.bottomright = x + 40, y - 20
            return(q + 1, False)
        elif q == 4:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 28, y - 10
            return (q + 1, False)
        elif q == 5:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 28, y - 10
            return (q + 1, False)
        elif q == 6:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 28, y - 10
            return (q + 1, False)
        elif q == 7:
            self.image = pygame.transform.rotate(vrr_img, 1)
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 25, y + 10
            return (q + 1, False)
        elif q == 8:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 25, y + 15
            return (q + 1, False)
        elif q == 9:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 20, y + 15
            return (q + 1, False)
        elif q == 10:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 15, y + 15
            return (q + 1, False)
        elif q == 11:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 7, y + 15
            return (q + 1, False)
        elif q == 12:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 4, y + 15
            return (q + 1, False)
        elif q == 13:
            return(q, True)

    def vr7(self, q):
        if q == 0:
            self.image = pygame.transform.rotate(vrp_img, 11)
            return (q + 1, False)
        elif q == 1:
            self.image = pygame.transform.rotate(vrp_img, 11)
            return (q + 1, False)
        elif q == 2:
            self.image = pygame.transform.rotate(vrp_img, 11)
            return (q + 1, False)
        elif q == 3:
            x, y = self.rect.bottomright
            self.image = pygame.Surface((200, 126))
            self.image = vr_img
            self.image.set_colorkey(WHITE)
            self.image = pygame.transform.rotate(vr_img, -30)
            self.rect.bottomright = x - 40, y - 40
            return(q + 1, False)
        elif q == 4:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 30, y - 26
            self.image = pygame.transform.rotate(vr_img, -22)
            return (q + 1, False)
        elif q == 5:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 30, y - 26
            self.image = pygame.transform.rotate(vr_img, -14)
            return (q + 1, False)
        elif q == 6:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 30, y - 26
            self.image = pygame.transform.rotate(vr_img, -7)
            return (q + 1, False)
        elif q == 7:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 30, y
            self.image = pygame.transform.rotate(vr_img, -7)
            return (q + 1, False)
        elif q == 8:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 26, y + 5
            self.image = pygame.transform.rotate(vr_img, -1)
            return (q + 1, False)
        elif q == 9:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 22, y + 10
            return (q + 1, False)
        elif q == 10:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 17, y + 15
            return (q + 1, False)
        elif q == 11:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 14, y + 20
            return (q + 1, False)
        elif q == 12:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 11, y + 25
            return (q + 1, False)
        elif q == 13:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 9, y + 27
            return (q + 1, False)
        elif q == 14:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 6, y + 27
            return (q + 1, False)
        elif q == 15:
            x, y = self.rect.bottomright
            self.rect.bottomright = x - 6, y + 27
            return (q + 1, False)
        elif q != 45:
            return(q + 1, False)
        elif q == 45:
            return(q, True)

    def vr8(self, q):
        if q == 0:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 13
            return(q + 1, False)
        elif q == 1:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 13
            return(q + 1, False)
        elif q == 2:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 13
            return(q + 1, False)
        elif q == 3:
            self.image = pygame.Surface((200, 126))
            self.image = vr_img
            self.image.set_colorkey(WHITE)
            self.image = pygame.transform.rotate(vr_img, -90)
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 26, y - 40
            return(q + 1, False)
        elif q == 4:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y - 20
            return (q + 1, False)
        elif q == 5:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y - 20
            return (q + 1, False)
        elif q == 6:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y - 20
            return (q + 1, False)
        elif q == 7:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y - 20
            return (q + 1, False)
        elif q == 8:
            return (q + 1, False)
        elif q == 9:
            return (q + 1, False)
        elif q == 10:
            return (q + 1, False)
        elif q == 11:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 5
            return (q + 1, False)
        elif q == 12:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 7
            return (q + 1, False)
        elif q == 13:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 8
            return (q + 1, False)
        elif q == 14:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 11
            return (q + 1, False)
        elif q == 15:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 11
            return (q + 1, False)
        elif q == 16:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 11
            return (q + 1, False)
        elif q == 17:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 11
            return (q + 1, False)
        elif q == 18:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 11
            return (q + 1, False)
        elif q == 19:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y + 11
            return (q + 1, False)
        elif q == 20:
            self.image = pygame.Surface((300, 188))
            self.image = vrp_img
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (W / 2, H / 2 - 70)
            return (q + 1, False)
        elif q == 21:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y - 6
            return (q + 1, False)
        elif q == 22:
            x, y = self.rect.bottomright
            self.rect.bottomright = x, y - 6
            return (q + 1, False)
        elif q == 23:
            return(q, True)

    def vr9(self, q):
        if q == 0:
            self.image = pygame.transform.rotate(vrp_img, -11)
            return (q + 1, False)
        elif q == 1:
            self.image = pygame.transform.rotate(vrp_img, -11)
            return (q + 1, False)
        elif q == 2:
            self.image = pygame.transform.rotate(vrp_img, -11)
            return (q + 1, False)
        elif q == 3:
            x, y = self.rect.bottomright
            self.image = pygame.Surface((200, 126))
            self.image = vrr_img
            self.image.set_colorkey(WHITE)
            self.image = pygame.transform.rotate(vrr_img, 30)
            self.rect.bottomright = x + 40, y - 40
            return(q + 1, False)
        elif q == 4:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 23, y - 26
            self.image = pygame.transform.rotate(vrr_img, 22)
            return (q + 1, False)
        elif q == 5:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 23, y - 26
            self.image = pygame.transform.rotate(vrr_img, 14)
            return (q + 1, False)
        elif q == 6:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 23, y - 26
            self.image = pygame.transform.rotate(vrr_img, 7)
            return (q + 1, False)
        elif q == 7:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 23, y
            self.image = pygame.transform.rotate(vrr_img, 7)
            return (q + 1, False)
        elif q == 8:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 26, y + 5
            self.image = pygame.transform.rotate(vrr_img, 1)
            return (q + 1, False)
        elif q == 9:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 22, y + 10
            return (q + 1, False)
        elif q == 10:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 17, y + 15
            return (q + 1, False)
        elif q == 11:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 14, y + 20
            return (q + 1, False)
        elif q == 12:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 11, y + 25
            return (q + 1, False)
        elif q == 13:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 9, y + 27
            return (q + 1, False)
        elif q == 14:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 6, y + 27
            return (q + 1, False)
        elif q == 15:
            x, y = self.rect.bottomright
            self.rect.bottomright = x + 6, y + 27
            return (q + 1, False)
        elif q != 45:
            return (q + 1, False)
        elif q == 45:
            return (q, True)

def proris(ochered, flagdraw):

    if flagdraw and ochered not in (0, 11, -1, 12):
        vr_sprites.draw(sc)
        ball_sprites.draw(sc)
    elif not flagdraw and ochered not in (0, 11, -1, 12):
        ball_sprites.draw(sc)
        vr_sprites.draw(sc)

    if ochered in [2,4,6,8,10]:
        but.pust()
        per.__init__()
    elif ochered in [1,3,5,7,9]:
        per.pust()
        but.__init__()

    if ochered in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        all_sprites.draw(sc)
        kv_sprites.draw(sc)
        sc.blit(follow, (25, H - 100))
        sc.blit(Btext, (W - 60, H - 75))
        sc.blit(Ptext, (W - 60, H - 150))

    if ochered in (21,22,23,24,25,26,27,28,29,30):
        if (not going) and (not going1):
            sc.blit(P11text, (W - 270, 50))
            if ochered in (21,23,25,27,29):
                but.__init__()
                per.pust()
            else:
                but.pust()
                per.__init__()
        elif going1:
            sc.blit(P21text, (W - 270, 50))
            if ochered in (21,23,25,27,29):
                but.pust()
                per.__init__()
            else:
                per.pust()
                but.__init__()



    if ochered in (21, 22, 23, 24, 25, 26, 27, 28, 29, 30):
        all_sprites.draw(sc)
        kv_sprites.draw(sc)
        sc.blit(follow1, (25, H - 100))
        sc.blit(P2text, (W - 65, H - 75))
        sc.blit(P1text, (W - 65, H - 150))

    if ochered == 11:
        pygame.draw.rect(sc, WHITE, (W // 2 - 401, H // 2 - 201, 802, 402))
        pygame.draw.rect(sc, GREEN, (W//2 - 380, H//2 - 180, 760, 360))
        sc.blit(follow2, (W//2 - 60, H//2 - 35))
        # sc.blit(Clickente, (W // 2 - 305, H // 2 + 65))
        if not flagpobedi:
            winn.pust()
            loss.__init__()
        else:
            loss.pust()
            winn.__init__()
        o11.draw(sc)

    if ochered == 19:
        pygame.draw.rect(sc, WHITE, (W // 2 - 401, H // 2 - 201, 802, 402))
        pygame.draw.rect(sc, GREEN, (W//2 - 380, H//2 - 180, 760, 360))
        sc.blit(follow11, (W//2 - 50, H//2 - 35))
        # sc.blit(Clickente, (W // 2 - 305, H // 2 + 65))
        # sc.blit(Wontext, (W//2 - 215, H // 2 - 135))
        if winer == '  Игрок1 ':
            igrokk1.__init__()
            igrokk2.pust()
        else:
            igrokk1.pust()
            igrokk2.__init__()
        o19.draw(sc)

    if ochered == 0:
        pygame.draw.rect(sc, WHITE, (W // 2 - 401, H // 2 - 201, 802, 402))
        pygame.draw.rect(sc, BLUE, (W // 2 - 380, H // 2 - 180, 760, 360))
        if match == 1:
            final.__init__()
        elif match == 2:
            final.ff4()
        elif match == 3:
            final.ff2()
        elif match == 4:
            final.ff()
        # sc.blit(startenter, (W // 2 - 260, H // 2 - 0))
        o0.draw(sc)

    if ochered == -1:
        pygame.draw.rect(sc, WHITE, (W // 2 - 401, H // 2 - 201, 802, 402))
        pygame.draw.rect(sc, GREEN, (W // 2 - 380, H // 2 - 180, 760, 360))
        cup.__init__()
        g1v1.__init__()
        # sc.blit(Clickent, (W // 2 - 260, H // 2 + 60))
        # sc.blit(Clickspace, (W // 2 + 64, H // 2 + 60))
        ic.draw(sc)
        ic1.draw(sc)
        o1.draw(sc)

    if ochered == 12:
        pygame.draw.rect(sc, WHITE, (W // 2 - 401, H // 2 - 201, 802, 402))
        pygame.draw.rect(sc, GREEN, (W // 2 - 380, H // 2 - 180, 760, 360))
        cup.win()
        ic1.draw(sc)
        o12.draw(sc)

    if ochered == 20:
        pygame.draw.rect(sc, WHITE, (W // 2 - 401, H // 2 - 201, 802, 402))
        pygame.draw.rect(sc, GREEN, (W // 2 - 380, H // 2 - 180, 760, 360))
        # sc.blit(startenter, (W // 2 - 290, H // 2 + 70))
        o20.draw(sc)



vr_sprites = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()
o12 = pygame.sprite.Group()
ic = pygame.sprite.Group()
ic1 = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
kv_sprites = pygame.sprite.Group()
o1 = pygame.sprite.Group()
o0 = pygame.sprite.Group()
o11 = pygame.sprite.Group()
o19 = pygame.sprite.Group()
o20 = pygame.sprite.Group()

vratar = Vratar()
ball = Ball()
cup = Cup()
g1v1 = G1v1()
per = Perchi()
but = Butsi()
klava = Klava()
kv1, kv2, kv3, kv4, kv5, kv6, kv7, kv8, kv9, kv10 = kvad1(), kvad2(), kvad3(), kvad4(), kvad5(), kvad6(), kvad7(), kvad8(), kvad9(), kvad10()

pobeda = Pobeda()
clickenter = Clickenter()
clickenterforstart = Clickenterforstart()
clickent = Clickent()
clickspace = Clickspace()
igrokk1 = Igrokk1()
igrokk2 = Igrokk2()
winn = Winn()
loss = Loss()
final = Final()
ent = Ent()

clickenterforstart.__init__()
clickspace.__init__()
clickent.__init__()
pobeda.__init__()
clickenter.__init__()
ent.__init__()
klava.__init__()

kv_sprites.add(kv1, kv2, kv3, kv4, kv5, kv6, kv7, kv8, kv9, kv10)
all_sprites.add(per)
all_sprites.add(but)
vr_sprites.add(vratar)
ball_sprites.add(ball)
ic1.add(cup)
ic.add(g1v1)

o1.add(clickent, clickspace)
o0.add(ent, final)
o11.add(winn,clickenter, loss)
o12.add(pobeda, clickenter)
o19.add(clickenter, igrokk1, igrokk2)
o20.add(clickenterforstart, klava)

background = pygame.image.load(path.join(img_dir, "FON.png")).convert()
background_rect = background.get_rect()



flRunning = True

flagg1,flagg2, flagg3, flagg4, flagg5, flagg6, flagg7, flagg8, flagg9, flago1, flago2, flago3, flago4, flago5, flago6, flago7, flago8, flago9, = False,False,False,False,False,False,False,False,False, False,False,False,False,False,False,False,False,False
speedx1, speedx2, speedx3, speedx4, speedx5, speedx6, speedx7, speedx8, speedx9, speedy= 20, 6, -20,11,11,11,11,11,11, 0
speedotbgr, speedotbgl, speedotb2, speedotbv = 34, -30, 10, 25
kof, f,g,q, udar,  ww, hh = 0,0,0,0,0, 70, 70
vratar.__init__()
flagdraw = True
a = 0
going = False
goal = False
chit1 = False
s = ''

bot, igrok, player1, player2 = 0, 0, 0, 0
ochered = -1
enter = False
space = False
going1 = False

kofudara = 6
kofseiva = 2
save = random.randint(1, kofudara)
save1 = random.randint(1, kofseiva)
match = 1
nazvanie = '1/8 ФИНАЛА'
contry = random.choice(['  Швеция ', '  Эквадор ', '  Дания ','  Швеция ', '  Эквадор ', '  Дания ','  Швеция ', '  Эквадор ', '  Дания ','  Бот Данил '])

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flRunning = False
        if event.type == pygame.KEYDOWN:
            if not enter and not going and not flagg1 and not flagg2 and not flagg3 and not flagg4 and not flagg5 and not flagg6 and not flagg7 and not flagg8 and not flagg9 and not flago1 and not flago2 and not flago3 and not flago4 and not flago5 and not flago6 and not flago7 and not flago8 and not flago9:
                if ochered in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                        flagg1 = True
                        flago1 = True
                        going = True
                        s += '1'
                    if event.key == pygame.K_KP2 or event.key == pygame.K_2:
                        flagg2 = True
                        flago2 = True
                        going = True
                        s += '2'
                    if event.key == pygame.K_KP3 or event.key == pygame.K_3:
                        flagg3 = True
                        flago3 = True
                        going = True
                        s += '3'
                    if event.key == pygame.K_KP4 or event.key == pygame.K_4:
                        flagg4 = True
                        flago4 = True
                        going = True
                        s += '4'
                    if event.key == pygame.K_KP5 or event.key == pygame.K_5:
                        flagg5 = True
                        flago5 = True
                        going = True
                        s += '5'
                    if event.key == pygame.K_KP6 or event.key == pygame.K_6:
                        flagg6 = True
                        flago6 = True
                        going = True
                        s += '6'
                    if event.key == pygame.K_KP7 or event.key == pygame.K_7:
                        flagg7 = True
                        flago7 = True
                        going = True
                        s += '7'
                    if event.key == pygame.K_KP8 or event.key == pygame.K_8:
                        flagg8 = True
                        flago8 = True
                        going = True
                        s += '8'
                    if event.key == pygame.K_KP9 or event.key == pygame.K_9:
                        flagg9 = True
                        flago9 = True
                        going = True
                        s += '9'

            if ochered in (21, 22, 23, 24, 25, 26, 27, 28, 29, 30) and not going:
                if not going1:
                    if event.key == pygame.K_KP1:
                        going1 = True
                        if ochered in (21, 23, 25, 27, 29):
                            flagg1 = True
                            flago1 = True
                            ygol = 1
                        else:
                            keeper = 1
                    elif event.key == pygame.K_KP2:
                        going1 = True
                        if ochered in (21, 23, 25, 27, 29):
                            flagg2 = True
                            flago2 = True
                            ygol = 2
                        else:
                            keeper = 2
                    elif event.key == pygame.K_KP3:
                        going1 = True
                        if ochered in (21, 23, 25, 27, 29):
                            flagg3 = True
                            flago3 = True
                            ygol = 3
                        else:
                            keeper = 3
                    elif event.key == pygame.K_KP4:
                        going1 = True
                        if ochered in (21, 23, 25, 27, 29):
                            flagg4 = True
                            flago4 = True
                            ygol = 4
                        else:
                            keeper = 4
                    elif event.key == pygame.K_KP5:
                        going1 = True
                        if ochered in (21, 23, 25, 27, 29):
                            flagg5 = True
                            flago5 = True
                            ygol = 5
                        else:
                            keeper = 5
                    elif event.key == pygame.K_KP6:
                        going1 = True
                        if ochered in (21, 23, 25, 27, 29):
                            flagg6 = True
                            flago6 = True
                            ygol = 6
                        else:
                            keeper = 6
                    elif event.key == pygame.K_KP7:
                        going1 = True
                        if ochered in (21, 23, 25, 27, 29):
                            flagg7 = True
                            flago7 = True
                            ygol = 7
                        else:
                            keeper = 7
                    elif event.key == pygame.K_KP8:
                        going1 = True
                        if ochered in (21, 23, 25, 27, 29):
                            flagg8 = True
                            flago8 = True
                            ygol = 8
                        else:
                            keeper = 8
                    elif event.key == pygame.K_KP9:
                        going1 = True
                        if ochered in (21, 23, 25, 27, 29):
                            flagg9 = True
                            flago9 = True
                            ygol = 9
                        else:
                            keeper = 9
                elif going1:
                    if event.key == pygame.K_1:
                        going = True
                        going1 = False
                        if ochered in (22, 24, 26, 28, 30):
                            flagg1 = True
                            flago1 = True
                            ygol = 1
                        else:
                            keeper = 1
                    if event.key == pygame.K_2:
                        going = True
                        going1 = False
                        if ochered in (22, 24, 26, 28, 30):
                            flagg2 = True
                            flago2 = True
                            ygol = 2
                        else:
                            keeper = 2
                    if event.key == pygame.K_3:
                        going = True
                        going1 = False
                        if ochered in (22, 24, 26, 28, 30):
                            flagg3 = True
                            flago3 = True
                            ygol = 3
                        else:
                            keeper = 3
                    if event.key == pygame.K_4:
                        going = True
                        going1 = False
                        if ochered in (22, 24, 26, 28, 30):
                            flagg4 = True
                            flago4 = True
                            ygol = 4
                        else:
                            keeper = 4
                    if event.key == pygame.K_5:
                        going = True
                        going1 = False
                        if ochered in (22, 24, 26, 28, 30):
                            flagg5 = True
                            flago5 = True
                            ygol = 5
                        else:
                            keeper = 5
                    if event.key == pygame.K_6:
                        going = True
                        going1 = False
                        if ochered in (22, 24, 26, 28, 30):
                            flagg6 = True
                            flago6 = True
                            ygol = 6
                        else:
                            keeper = 6
                    if event.key == pygame.K_7:
                        going = True
                        going1 = False
                        if ochered in (22, 24, 26, 28, 30):
                            flagg7 = True
                            flago7 = True
                            ygol = 7
                        else:
                            keeper = 7
                    if event.key == pygame.K_8:
                        going = True
                        going1 = False
                        if ochered in (22, 24, 26, 28, 30):
                            flagg8 = True
                            flago8 = True
                            ygol = 8
                        else:
                            keeper = 8
                    if event.key == pygame.K_9:
                        going = True
                        going1 = False
                        if ochered in (22, 24, 26, 28, 30):
                            flagg9 = True
                            flago9 = True
                            ygol = 9
                        else:
                            keeper = 9
            if event.key == pygame.K_RETURN:
                enter = True
            elif event.key == pygame.K_SPACE:
                space = True
            elif event.key == pygame.K_ESCAPE:
                ochered = -1
            if '194725' in s:
                chit1 = True



    #Обновление
    ball_sprites.update()
    vr_sprites.update()

    if ochered in (1,3,5,7,9,21,23,25,27,29):
        vrp_img = vrp1_img
        vr_img = vr1_img
        vrr_img = vrr1_img
    elif ochered in (2,4,6,8,10,22,24,26,28,30):
        vrp_img = vrp2_img
        vr_img = vr2_img
        vrr_img = vrr2_img

    if ochered == 0:
        if enter:
            kv1.__init__()
            kv2.__init__()
            kv3.__init__()
            kv4.__init__()
            kv5.__init__()
            kv6.__init__()
            kv7.__init__()
            kv8.__init__()
            kv9.__init__()
            kv10.__init__()
            ochered = 1
            enter = False
            bot, igrok = 0, 0
            if match == 1:
                contry = random.choice(['  Швеция ', '  Эквадор ', '  Дания ','  Швеция ', '  Эквадор ', '  Дания ','  Швеция ', '  Эквадор ', '  Дания ','  Бот Данил '])
            elif match == 2:
                contry = random.choice(['  Бельгия ', '  Мексика ', '  Хорватия '])
            elif match == 3:
                contry = random.choice(['  Германия ', '  Аргентина ', '  Англия'])
            elif match == 4:
                contry = random.choice([ '  Франция ', '  Бразилия ', '  Франция ', '  Китай ', '  Бразилия ', '  Франция ', '  Бразилия ','  Бот Данил '])

    if ochered == -1:
        chit1 = False
        if enter:
            enter = False
            ochered = 0
        elif space:
            space = False
            ochered = 20

    if ochered == 12:
        if enter:
            enter = False
            ochered = -1
            match = 1
            nazvanie = '1/8 ФИНАЛА'

    if ochered == 11:
        if enter:
            enter = False
            if igrok > bot:
                match += 1
                flagpobedi = True
            else:
                flagpobedi = False
                s = ''
                chit1 = False
                ball_img = ball2_img
                match = 1
                ochered = -1
            if match == 5:
                ochered = 12
            elif match == 1:
                nazvanie = '1/8 ФИНАЛА'
                kofudara = 6
                kofseiva = 2
            elif match == 2:
                nazvanie = '1/4 ФИНАЛА'
                ochered = 0
                kofudara = 5
                kofseiva = 3
            elif match == 3:
                nazvanie = 'ПОЛУФИНАЛ'
                ochered = 0
                kofudara = 4
                kofseiva = 4
            elif match == 4:
                nazvanie = 'ФИНАЛ'
                ochered = 0
                kofudara = 3
                kofseiva = 5

    if ochered == 20:
        if enter:
            enter = False
            kv1.__init__()
            kv2.__init__()
            kv3.__init__()
            kv4.__init__()
            kv5.__init__()
            kv6.__init__()
            kv7.__init__()
            kv8.__init__()
            kv9.__init__()
            kv10.__init__()
            player1, player2 = 0, 0
            ochered = 21
            ball_img = ball2_img
            s = ''
            chit1 = False

    if ochered == 19:
        if enter:
            enter = False
            ochered = -1



    if going:
        if ochered in (21,22,23,24,25,26,27,28,29,30):
            if keeper == ygol or (keeper == 2 and ygol == 5) or (keeper == 5 and ygol == 2):
                goal = False
                if ygol == 1:
                    udar, speedotbgl, ww, hh, flago1, q = otbil1(udar, speedotbgl, ww, hh, flago1, q)
                    going = flago1
                if ygol == 2:
                    udar, speedotb2, ww, hh, flago2, kof, flagdraw = otbil2(udar, speedotb2, ww, hh, flago2, kof, flagdraw)
                    going = flago2
                if ygol == 3:
                    udar, speedotbgr, ww, hh, flago3, q = otbil3(udar, speedotbgr, ww, hh, flago3, q)
                    going = flago3
                if ygol == 4:
                    udar, speedotbgl, ww, hh, flago4, g, speedy, q = otbil4(udar, speedotbgl, ww, hh, flago4, g, speedy, q)
                    going = flago4
                if ygol == 5:
                    udar, speedx4, ww, hh, flago5, g = otbil5(udar, speedx4, ww, hh, flago5, g)
                    going = flago5
                if ygol == 6:
                    udar, speedotbgr, ww, hh, flago6, g, speedy, q = otbil6(udar, speedotbgr, ww, hh, flago6, g, speedy, q)
                    going = flago6
                if ygol == 7:
                    FPS = 26
                    udar, speedotbv, ww, hh, flago7, g, q = otbil7(udar, speedotbv, ww, hh, flago7, g, q)
                    going = flago7
                if ygol == 8:
                    udar, speedotbv, ww, hh, flago8, g, q = otbil8(udar, speedotbv, ww, hh, flago8, g, q)
                    going = flago8
                if ygol == 9:
                    FPS = 26
                    udar, speedotbv, ww, hh, flago9, g, q = otbil9(udar, speedotbv, ww, hh, flago9, g, q)
                    going = flago9
            else:
                li = [0, vratar.vr1, 0, vratar.vr3, vratar.vr4, 0, vratar.vr6, vratar.vr7, vratar.vr8, vratar.vr9]
                func = li[keeper]
                if keeper not in (2, 5): q, ff = func(q)
                if ygol == 1:
                    f, udar, speedx1, flagg1, ww, hh, flagdraw = goal1(f, udar, speedx1, flagg1, ww, hh, flagdraw)
                    going = flagg1
                if ygol == 2:
                    f, udar, speedx2, flagg2, ww, hh, kof, flagdraw = goal2(f, udar, speedx2, flagg2, ww, hh, kof, flagdraw)
                    going = flagg2
                if ygol == 3:
                    f, udar, speedx3, flagg3, ww, hh, flagdraw = goal3(f, udar, speedx3, flagg3, ww, hh, flagdraw)
                    going = flagg3
                if ygol == 4:
                    f, g, udar, speedx4, flagg4, ww, hh, flagdraw = goal4(f, g, udar, speedx4, flagg4, ww, hh, flagdraw)
                    going = flagg4
                if ygol == 5:
                    f, g, udar, speedx5, flagg5, ww, hh, flagdraw = goal5(f, g, udar, speedx5, flagg5, ww, hh, flagdraw)
                    going = flagg5
                if ygol == 6:
                    f, g, udar, speedx6, flagg6, ww, hh, flagdraw = goal6(f, g, udar, speedx6, flagg6, ww, hh, flagdraw)
                    going = flagg6
                if ygol == 7:
                    f, g, udar, speedx7, flagg7, ww, hh, flagdraw = goal7(f, g, udar, speedx7, flagg7, ww, hh, flagdraw)
                    going = flagg7
                if ygol == 8:
                    f, g, udar, speedx8, flagg8, ww, hh, flagdraw = goal8(f, g, udar, speedx8, flagg8, ww, hh, flagdraw)
                    going = flagg8
                if ygol == 9:
                    f, g, udar, speedx9, flagg9, ww, hh, flagdraw = goal9(f, g, udar, speedx9, flagg9, ww, hh, flagdraw)
                    going = flagg9
                goal = True

        if ochered in [1,3,5,7,9]  and ochered != 0:
            if save == 1:
                if flago1:
                    udar, speedotbgl, ww, hh, flago1, q = otbil1(udar, speedotbgl, ww, hh, flago1, q)
                    going = flago1
                elif flago2:
                    udar, speedotb2, ww, hh, flago2, kof, flagdraw = otbil2(udar, speedotb2, ww, hh, flago2, kof,
                                                                            flagdraw)
                    going = flago2
                elif flago3:
                    udar, speedotbgr, ww, hh, flago3, q = otbil3(udar, speedotbgr, ww, hh, flago3, q)
                    going = flago3
                elif flago4:
                    udar, speedotbgl, ww, hh, flago4, g, speedy, q = otbil4(udar, speedotbgl, ww, hh, flago4, g, speedy,
                                                                            q)
                    going = flago4
                elif flago5:
                    udar, speedx4, ww, hh, flago5, g = otbil5(udar, speedx4, ww, hh, flago5, g)
                    going = flago5
                elif flago6:
                    udar, speedotbgr, ww, hh, flago6, g, speedy, q = otbil6(udar, speedotbgr, ww, hh, flago6, g, speedy,
                                                                            q)
                    going = flago6
                elif flago7:
                    FPS = 26
                    udar, speedotbv, ww, hh, flago7, g, q = otbil7(udar, speedotbv, ww, hh, flago7, g, q)
                    going = flago7
                elif flago8:
                    udar, speedotbv, ww, hh, flago8, g, q = otbil8(udar, speedotbv, ww, hh, flago8, g, q)
                    going = flago8
                elif flago9:
                    FPS = 26
                    udar, speedotbv, ww, hh, flago9, g, q = otbil9(udar, speedotbv, ww, hh, flago9, g, q)
                    going = flago9
                goal = False
            else:
                if flagg1:
                    if a == 0:
                        a = random.choice([vratar.vr7, vratar.vr3, vratar.vr6, vratar.vr9])
                    q, ff = a(q)
                    f, udar, speedx1, flagg1, ww, hh, flagdraw = goal1(f, udar, speedx1, flagg1, ww, hh, flagdraw)
                    if ff and not flagg1:
                        going = False
                elif flagg2:
                    if a == 0:
                        a = random.choice([vratar.vr7, vratar.vr6, vratar.vr9, vratar.vr4])
                    q, ff = a(q)
                    f, udar, speedx2, flagg2, ww, hh, kof, flagdraw = goal2(f, udar, speedx2, flagg2, ww, hh, kof, flagdraw)
                    if ff and not flagg2:
                        going = False
                elif flagg3:
                    if a == 0:
                        a = random.choice([vratar.vr7, vratar.vr1, vratar.vr4, vratar.vr9])
                    q, ff = a(q)
                    f, udar, speedx3, flagg3, ww, hh, flagdraw = goal3(f, udar, speedx3, flagg3, ww, hh, flagdraw)
                    if ff and not flagg3:
                        going = False
                elif flagg4:
                    if a == 0:
                        a = random.choice([vratar.vr9, vratar.vr6, vratar.vr3])
                    q, ff = a(q)
                    f, g, udar, speedx4, flagg4, ww, hh, flagdraw = goal4(f, g, udar, speedx4, flagg4, ww, hh, flagdraw)
                    if ff and not flagg4:
                        going = False
                elif flagg5:
                    if a == 0:
                        a = random.choice([vratar.vr7, vratar.vr6, vratar.vr9, vratar.vr4, vratar.vr1, vratar.vr3])
                    q, ff = a(q)
                    f, g, udar, speedx5, flagg5, ww, hh, flagdraw = goal5(f, g, udar, speedx5, flagg5, ww, hh, flagdraw)
                    if ff and not flagg5:
                        going = False
                elif flagg6:
                    if a == 0:
                        a = random.choice([vratar.vr1, vratar.vr4, vratar.vr7])
                    q, ff = a(q)
                    f, g, udar, speedx6, flagg6, ww, hh, flagdraw = goal6(f, g, udar, speedx6, flagg6, ww, hh, flagdraw)
                    if ff and not flagg6:
                        going = False
                elif flagg7:
                    if a == 0:
                        a = random.choice([vratar.vr1, vratar.vr3, vratar.vr6, vratar.vr9])
                    q, ff = a(q)
                    f, g, udar, speedx7, flagg7, ww, hh, flagdraw = goal7(f, g, udar, speedx7, flagg7, ww, hh, flagdraw)
                    if ff and not flagg7:
                        going = False
                elif flagg8:
                    if a == 0:
                        a = random.choice([vratar.vr1, vratar.vr3, vratar.vr4, vratar.vr6, vratar.vr7, vratar.vr9])
                    q, ff = a(q)
                    f, g, udar, speedx8, flagg8, ww, hh, flagdraw = goal8(f, g, udar, speedx8, flagg8, ww, hh, flagdraw)
                    if ff and not flagg8:
                        going = False
                elif flagg9:
                    if a == 0:
                        a = random.choice([vratar.vr1, vratar.vr4, vratar.vr7, vratar.vr3])
                    q, ff = a(q)
                    f, g, udar, speedx9, flagg9, ww, hh, flagdraw = goal9(f, g, udar, speedx9, flagg9, ww, hh, flagdraw)
                    if ff and not flagg9:
                        going = False
                goal = True
        elif ochered in [2,4,6,8,10] and ochered != 0:
            if save1 == 1:
                if flago1:
                    udar, speedotbgl, ww, hh, flago1, q = otbil1(udar, speedotbgl, ww, hh, flago1, q)
                    going = flago1
                if flago2:
                    udar, speedotb2, ww, hh, flago2, kof, flagdraw = otbil2(udar, speedotb2, ww, hh, flago2, kof,flagdraw)
                    going = flago2
                if flago3:
                    udar, speedotbgr, ww, hh, flago3, q = otbil3(udar, speedotbgr, ww, hh, flago3, q)
                    going = flago3
                if flago4:
                    udar, speedotbgl, ww, hh, flago4, g, speedy, q = otbil4(udar, speedotbgl, ww, hh, flago4, g, speedy,q)
                    going = flago4
                if flago5:
                    udar, speedx4, ww, hh, flago5, g = otbil5(udar, speedx4, ww, hh, flago5, g)
                    going = flago5
                if flago6:
                    udar, speedotbgr, ww, hh, flago6, g, speedy, q = otbil6(udar, speedotbgr, ww, hh, flago6, g, speedy,q)
                    going = flago6
                if flago7:
                    FPS = 26
                    udar, speedotbv, ww, hh, flago7, g, q = otbil7(udar, speedotbv, ww, hh, flago7, g, q)
                    going = flago7
                if flago8:
                    udar, speedotbv, ww, hh, flago8, g, q = otbil8(udar, speedotbv, ww, hh, flago8, g, q)
                    going = flago8
                if flago9:
                    FPS = 26
                    udar, speedotbv, ww, hh, flago9, g, q = otbil9(udar, speedotbv, ww, hh, flago9, g, q)
                    going = flago9
                goal = False
            else:
                if flago1:
                    if a == 0:
                        a = random.choice([3,5,6,7,8,9])
                        if a == 3:
                            flag3 = True
                        elif a ==5:
                            flag5 = True
                        elif a ==6:
                            flag6 = True
                        elif a ==7:
                            flag7 = True
                        elif a ==8:
                            flag8 = True
                        elif a ==9:
                            flag9 = True
                    q, ff = vratar.vr1(q)
                    going = not ff
                    if a == 3:
                        f,udar, speedx3, flag3,ww,hh, flagdraw = goal3(f,udar, speedx3, flag3,ww,hh, flagdraw)
                        going = flag3
                    elif a == 5:
                        f, g, udar, speedx5, flag5, ww, hh, flagdraw = goal5(f, g, udar, speedx5, flag5, ww, hh, flagdraw)
                        going = flag5
                    elif a == 6:
                        f, g, udar, speedx6, flag6, ww, hh, flagdraw = goal6(f, g, udar, speedx6, flag6, ww, hh, flagdraw)
                        going = flag6
                    elif a == 7:
                        f, g, udar, speedx7, flag7, ww, hh, flagdraw = goal7(f, g, udar, speedx7, flag7, ww, hh, flagdraw)
                        going = flag7
                    elif a == 8:
                        f, g, udar, speedx8, flag8, ww, hh, flagdraw = goal8(f, g, udar, speedx8, flag8, ww, hh, flagdraw)
                        going = flag8
                    elif a == 9:
                        f, g, udar, speedx9, flag9, ww, hh, flagdraw = goal9(f, g, udar, speedx9, flag9, ww, hh, flagdraw)
                        going = flag9
                if flago2 or flago5:
                    if a == 0:
                        a = random.choice([1,3,4,6,7,9])
                        if a == 3:
                            flag3 = True
                        elif a ==1:
                            flag1 = True
                        elif a ==6:
                            flag6 = True
                        elif a ==7:
                            flag7 = True
                        elif a ==4:
                            flag4 = True
                        elif a ==9:
                            flag9 = True
                    if a == 3:
                        f,udar, speedx3, flag3,ww,hh, flagdraw = goal3(f,udar, speedx3, flag3,ww,hh, flagdraw)
                        going = flag3
                    elif a == 1:
                        f,udar, speedx1, flag1,ww,hh, flagdraw = goal1(f,udar, speedx1, flag1,ww,hh, flagdraw)
                        going = flag1
                    elif a == 6:
                        f, g, udar, speedx6, flag6, ww, hh, flagdraw = goal6(f, g, udar, speedx6, flag6, ww, hh, flagdraw)
                        going = flag6
                    elif a == 7:
                        f, g, udar, speedx7, flag7, ww, hh, flagdraw = goal7(f, g, udar, speedx7, flag7, ww, hh, flagdraw)
                        going = flag7
                    elif a == 4:
                        f,g,udar, speedx4, flag4,ww,hh, flagdraw = goal4(f, g, udar, speedx4, flag4,ww,hh, flagdraw)
                        going = flag4
                    elif a == 9:
                        f, g, udar, speedx9, flag9, ww, hh, flagdraw = goal9(f, g, udar, speedx9, flag9, ww, hh, flagdraw)
                        going = flag9
                if flago3:
                    if a == 0:
                        a = random.choice([1,5,4,7,8,9])
                        if a == 1:
                            flag1 = True
                        elif a ==5:
                            flag5 = True
                        elif a ==4:
                            flag4 = True
                        elif a ==7:
                            flag7 = True
                        elif a ==8:
                            flag8 = True
                        elif a ==9:
                            flag9 = True
                    q, ff = vratar.vr3(q)
                    going = not ff
                    if a == 1:
                        f,udar, speedx1, flag1,ww,hh, flagdraw = goal1(f,udar, speedx1, flag1,ww,hh, flagdraw)
                        going = flag1
                    elif a == 5:
                        f, g, udar, speedx5, flag5, ww, hh, flagdraw = goal5(f, g, udar, speedx5, flag5, ww, hh, flagdraw)
                        going = flag5
                    elif a == 4:
                        f,g,udar, speedx4, flag4,ww,hh, flagdraw = goal4(f, g, udar, speedx4, flag4,ww,hh, flagdraw)
                        going = flag4
                    elif a == 7:
                        f, g, udar, speedx7, flag7, ww, hh, flagdraw = goal7(f, g, udar, speedx7, flag7, ww, hh, flagdraw)
                        going = flag7
                    elif a == 8:
                        f, g, udar, speedx8, flag8, ww, hh, flagdraw = goal8(f, g, udar, speedx8, flag8, ww, hh, flagdraw)
                        going = flag8
                    elif a == 9:
                        f, g, udar, speedx9, flag9, ww, hh, flagdraw = goal9(f, g, udar, speedx9, flag9, ww, hh, flagdraw)
                        going = flag9
                if flago4:
                    if a == 0:
                        a = random.choice([3,6,8,9])
                        if a == 3:
                            flag3 = True
                        elif a ==6:
                            flag6 = True
                        elif a ==8:
                            flag8 = True
                        elif a ==9:
                            flag9 = True
                    q, ff = vratar.vr4(q)
                    going = not ff
                    if a == 3:
                        f, udar, speedx3, flag3, ww, hh, flagdraw = goal3(f, udar, speedx3, flag3, ww, hh, flagdraw)
                        going = flag3
                    elif a == 6:
                        f, g, udar, speedx6, flag6, ww, hh, flagdraw = goal6(f, g, udar, speedx6, flag6, ww, hh, flagdraw)
                        going = flag6
                    elif a == 8:
                        f, g, udar, speedx8, flag8, ww, hh, flagdraw = goal8(f, g, udar, speedx8, flag8, ww, hh, flagdraw)
                        going = flag8
                    elif a == 9:
                        f, g, udar, speedx9, flag9, ww, hh, flagdraw = goal9(f, g, udar, speedx9, flag9, ww, hh, flagdraw)
                        going = flag9
                if flago6:
                    if a == 0:
                        a = random.choice([1, 4, 7, 8])
                        if a == 1:
                            flag1 = True
                        elif a == 4:
                            flag4 = True
                        elif a == 7:
                            flag7 = True
                        elif a == 8:
                            flag8 = True
                    q, ff = vratar.vr6(q)
                    going = not ff
                    if a == 1:
                        f, udar, speedx1, flag1, ww, hh, flagdraw = goal1(f, udar, speedx1, flag1, ww, hh, flagdraw)
                        going = flag1
                    elif a == 4:
                        f, g, udar, speedx4, flag4, ww, hh, flagdraw = goal4(f, g, udar, speedx4, flag4, ww, hh,
                                                                             flagdraw)
                        going = flag4
                    elif a == 7:
                        f, g, udar, speedx7, flag7, ww, hh, flagdraw = goal7(f, g, udar, speedx7, flag7, ww, hh,
                                                                             flagdraw)
                        going = flag7
                    elif a == 8:
                        f, g, udar, speedx8, flag8, ww, hh, flagdraw = goal8(f, g, udar, speedx8, flag8, ww, hh,
                                                                             flagdraw)
                        going = flag8
                if flago7:
                    if a == 0:
                        a = random.choice([3,6,8,9])
                        if a == 3:
                            flag3 = True
                        elif a ==6:
                            flag6 = True
                        elif a ==8:
                            flag8 = True
                        elif a ==9:
                            flag9 = True
                    q, ff = vratar.vr7(q)
                    going = not ff
                    if a == 3:
                        f, udar, speedx3, flag3, ww, hh, flagdraw = goal3(f, udar, speedx3, flag3, ww, hh, flagdraw)
                        going = flag3
                    elif a == 6:
                        f, g, udar, speedx6, flag6, ww, hh, flagdraw = goal6(f, g, udar, speedx6, flag6, ww, hh, flagdraw)
                        going = flag6
                    elif a == 8:
                        f, g, udar, speedx8, flag8, ww, hh, flagdraw = goal8(f, g, udar, speedx8, flag8, ww, hh, flagdraw)
                        going = flag8
                    elif a == 9:
                        f, g, udar, speedx9, flag9, ww, hh, flagdraw = goal9(f, g, udar, speedx9, flag9, ww, hh, flagdraw)
                        going = flag9
                if flago9:
                    if a == 0:
                        a = random.choice([1, 4, 7, 8])
                        if a == 1:
                            flag1 = True
                        elif a == 4:
                            flag4 = True
                        elif a == 7:
                            flag7 = True
                        elif a == 8:
                            flag8 = True
                    q, ff = vratar.vr9(q)
                    going = not ff
                    if a == 1:
                        f, udar, speedx1, flag1, ww, hh, flagdraw = goal1(f, udar, speedx1, flag1, ww, hh, flagdraw)
                        going = flag1
                    elif a == 4:
                        f, g, udar, speedx4, flag4, ww, hh, flagdraw = goal4(f, g, udar, speedx4, flag4, ww, hh, flagdraw)
                        going = flag4
                    elif a == 7:
                        f, g, udar, speedx7, flag7, ww, hh, flagdraw = goal7(f, g, udar, speedx7, flag7, ww, hh,flagdraw)
                        going = flag7
                    elif a == 8:
                        f, g, udar, speedx8, flag8, ww, hh, flagdraw = goal8(f, g, udar, speedx8, flag8, ww, hh,flagdraw)
                        going = flag8
                if flago8:
                    if a == 0:
                        a = random.choice([1,3,4,6,7,9])
                        if a == 3:
                            flag3 = True
                        elif a ==1:
                            flag1 = True
                        elif a ==6:
                            flag6 = True
                        elif a ==7:
                            flag7 = True
                        elif a ==4:
                            flag4 = True
                        elif a ==9:
                            flag9 = True
                    q, ff = vratar.vr8(q)
                    if a == 3:
                        f,udar, speedx3, flag3,ww,hh, flagdraw = goal3(f,udar, speedx3, flag3,ww,hh, flagdraw)
                        going = flag3
                    elif a == 1:
                        f,udar, speedx1, flag1,ww,hh, flagdraw = goal1(f,udar, speedx1, flag1,ww,hh, flagdraw)
                        going = flag1
                    elif a == 6:
                        f, g, udar, speedx6, flag6, ww, hh, flagdraw = goal6(f, g, udar, speedx6, flag6, ww, hh, flagdraw)
                        going = flag6
                    elif a == 7:
                        f, g, udar, speedx7, flag7, ww, hh, flagdraw = goal7(f, g, udar, speedx7, flag7, ww, hh, flagdraw)
                        going = flag7
                    elif a == 4:
                        f,g,udar, speedx4, flag4,ww,hh, flagdraw = goal4(f, g, udar, speedx4, flag4,ww,hh, flagdraw)
                        going = flag4
                    elif a == 9:
                        f, g, udar, speedx9, flag9, ww, hh, flagdraw = goal9(f, g, udar, speedx9, flag9, ww, hh, flagdraw)
                        going = flag9

                goal = True
        if not going:
            if chit1:
                ball_img = ball1_img
            a = 0
            if goal:
                if ochered in [1,3,5,7,9]:
                    igrok += 1
                elif ochered in (2,4,6,8,10):
                    bot += 1
                elif ochered in [21,23,25,27,29]:
                    player1 += 1
                elif ochered in (22,24,26,28,30):
                    player2 += 1
            if ochered == 1 or ochered == 21:
                if goal:
                    kv1.zab()
                else: kv1.nezab()
            if ochered == 2 or ochered == 22:
                if goal:
                    kv2.zab()
                else: kv2.nezab()
            if ochered == 3 or ochered == 23:
                if goal:
                    kv3.zab()
                else: kv3.nezab()
            if ochered == 4 or ochered == 24:
                if goal:
                    kv4.zab()
                else: kv4.nezab()
            if ochered == 5 or ochered == 25:
                if goal:
                    kv5.zab()
                else: kv5.nezab()
            if ochered == 6 or ochered == 26:
                if goal:
                    kv6.zab()
                else: kv6.nezab()
            if ochered == 7 or ochered == 27:
                if goal:
                    kv7.zab()
                else: kv7.nezab()
            if ochered == 8 or ochered == 28:
                if goal:
                    kv8.zab()
                else: kv8.nezab()
            if ochered == 9 or ochered == 29:
                if goal:
                    kv9.zab()
                else: kv9.nezab()
            if ochered == 10 or ochered == 30:
                if goal:
                    kv10.zab()
                else: kv10.nezab()

            if ochered in (1,2,3,4,5,6,7,8,9,10):
                aa = max(igrok, bot)
                bb = min(igrok, bot)
                if bot < igrok:
                    cc = ochered // 2
                else:
                    cc = (ochered + 1) // 2
                if ochered == 10 and bot == igrok:
                    ochered = 9
                    kv1.pust()
                    kv2.pust()
                    kv3.pust()
                    kv4.pust()
                    kv5.pust()
                    kv6.pust()
                    kv7.pust()
                    kv8.pust()
                    kv9.__init__()
                    kv10.__init__()
                elif aa - bb > 5 - cc:
                    ochered = 11
                else:
                    ochered += 1

            if ochered in (21,22,23,24,25,26,27,28,29,30):
                aa = max(player1, player2)
                bb = min(player1, player2)
                if player2 < player1:
                    cc = (ochered - 20) // 2
                else:
                    cc = (ochered + 1 - 20) // 2
                if ochered == 30 and player1 == player2:
                    ochered = 29
                    kv1.pust()
                    kv2.pust()
                    kv3.pust()
                    kv4.pust()
                    kv5.pust()
                    kv6.pust()
                    kv7.pust()
                    kv8.pust()
                    kv9.__init__()
                    kv10.__init__()
                elif aa - bb > 5 - cc:
                    ochered = 19
                else:
                    ochered += 1

            save = random.randint(1, kofudara)
            save1 = random.randint(1, kofseiva)



    #Возврат в начальное положение:
    if (not going) and (not going1):

        ball.__init__()
        vratar.__init__()
        flagg1,flagg2, flagg3, flagg4, flagg5, flagg6, flagg7, flagg8, flagg9, flago1, flago2, flago3, flago4, flago5, flago6, flago7, flago8, flago9, = False,False,False,False,False,False,False,False,False, False,False,False,False,False,False,False,False,False
        flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9 = False,False,False,False,False,False,False,False,False
        speedx1, speedx2, speedx3, speedx4, speedx5, speedx6, speedx7, speedx8, speedx9, speedy = 20, 6, -20, 11, 11, 11, 11, 11, 11, 0
        speedotbgr, speedotbgl, speedotb2, speedotbv = 34, -30, 10, 25
        kof, f, g, q, udar, ww, hh = 0, 0, 0, 0, 0, 70, 70
        flagdraw = True
        FPS = 30
        going = False
        goal = False

    flagpobedi = igrok > bot
    # print(chit1)
    # print(s)

    stt = ' Игрок  ' + str(igrok) + ':' + str(bot) + contry
    stt1 = ' Игрок1  ' + str(player1) + ':' + str(player2) + '  Игрок2 '
    sttt1 = str(player1) + ':' + str(player2)
    sttt = str(igrok) + ':' + str(bot)
    if player1 > player2:
        winer = '  Игрок1 '
    else: winer = '  Игрок2 '
    textwiner = winer + 'победил  '
    follow = font.render(stt,1,WHITE, GREEN)
    follow1 = font.render(stt1, 1, WHITE, GREEN)
    follow2 = font3.render(sttt,1,WHITE, GREEN)
    follow11 = font3.render(sttt1, 1, WHITE, GREEN)
    Btext = font.render(contry[2],1,WHITE)
    # Looser = font.render('Поражение', 1, WHITE)
    Name = font.render(nazvanie, 1, WHITE)
    # Winner = font.render('Победа', 1, WHITE)
    # Wontext = font.render(textwiner, 1, WHITE)
    # Clickent = font1.render('Нажмите ENTER', 1, WHITE)
    # Clickspace = font1.render('Нажмите SPACE', 1, WHITE)
    startenter = font2.render('Нажмите ENTER для начала', 1, WHITE)
    # Clickente = font.render('Нажмите ENTER для продолжения', 1, WHITE)
    Ptext = font.render('И',1,WHITE)
    P1text = font.render('1', 1, WHITE)
    P2text = font.render('2', 1, WHITE)
    P11text = font.render('И1', 1, GREEN1)
    P21text = font.render('И2', 1, GREEN1)
    # Отрисовка
    sc.fill(WHITE)
    sc.blit(background, background_rect)
    proris(ochered, flagdraw)



    pygame.display.flip()
    clock.tick(FPS)