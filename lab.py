# Разработай свою игру в этом файле!
# твой код здесь

from pygame import*

font.init()
font1 = font.SysFont('',50).render('again?',True, (0,0,0))
font2 = font.SysFont('',50).render('Victory',True, (250,250,250))
font3 = font.SysFont('',50).render('Game over',True, (250,30,240))
font4 = font.SysFont('',50).render('finish',True, (0,0,0))
font5 = font.SysFont('',50).render('points:3/',True, (200,170,0))
font6 = font.SysFont('',50).render('you do not have 3 points',True, (200,170,0))
font7 = font.SysFont('',50).render('',True, (200,170,0))

window = display.set_mode((800,600))
display.set_caption('pacman')
run = True
final = display.set_mode((800,700))
font.init()
font = font.SysFont('Arial',40).render('Win',True,(0,0,0))
class Gamesprite(sprite.Sprite):

    def __init__(self,w,h,x,y,picture):
         super().__init__()
         self.image = transform.scale(image.load(picture),(w,h))
         self.rect = Rect(x,y,w,h)
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y

    def picture(self):
        window.blit(self.image,self.rect)
    def collidepoint(self):
        return collidepoint(self.x,self.y)
    def kill_you(self):
        self.kill()
bullets = sprite.Group()
class Player(Gamesprite):
    def __init__(self, w, h, x, y, picture, x_speed, y_speed):
        super().__init__(w, h, x, y, picture)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        # сначала движение по горизонтали
        if self.rect.x <= 720 and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
        # если зашли за стенку, то встанем вплотную к стене
        touch = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:  # идем направо, правый край персонажа - вплотную к левому краю стены
            for i in touch:
                # если коснулись сразу нескольких, то правый край - минимальный из возможных
                self.rect.right = min(self.rect.right, i.rect.left)
        elif self.x_speed < 0:  # идем налево, ставим левый край персонажа вплотную к правому краю стены
            for i in touch:
                # если коснулись нескольких стен, то левый край - максимальный
                self.rect.left = max(self.rect.left, i.rect.right)
        if self.rect.y <= 520 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        # если зашли за стенку, то встанем вплотную к стене
        touch = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:  # идем вниз
            for i in touch:
                self.y_speed = 0
        # Проверяем, какая из платформ снизу самая высокая, выравниваемся по ней, запоминаем её как свою опору:
                if i.rect.top < self.rect.bottom:
                    self.rect.bottom = i.rect.top
        elif self.y_speed < 0:  # идем вверх
            for i in touch:
                self.y_speed = 0  # при столкновении со стеной вертикальная скорость гасится
                # выравниваем верхний край по нижним краям стенок, на которые наехали
                self.rect.top = max(self.rect.top, i.rect.bottom)

        
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top,'bullet.png',20,40,10)
        bullets.add(bullet)
    def shoot2(self):
        bullet2 = Bullet2(self.rect.centerx, self.rect.top,'bullet.png',20,40,10)
        bullets.add(bullet2)

            
            

        



class Enemy(Gamesprite):
    def __init__(self,w,h,x,y,picture,speed):
        super().__init__(w,h,x,y,picture)
        self.speed = speed
        self.direction = True
    def update(self):
        if self.rect.x <= 99 :
            self.direction = True
            self.image = transform.flip(self.image,True,False)
        elif self.rect.x>= 500:
            self.direction = False
            self.image = transform.flip(self.image,True,False)
        if self.direction == True:
            self.rect.x+=self.speed
        elif self.direction == False:
            self.rect.x-=self.speed

            

# class Bullet(Gamesprite):
#     def __init__(self,w,h,x,y,picture,speed):
#         super().__init__(w,h,x,y,picture)
#         self.speed = speed
        
#     def update(self):
#         self.rect.x += self.speed
# group = sprite.Group()
class Bullet(sprite.Sprite):
    def __init__(self,x,y,picture,h,w,speed):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = Rect(x,y,w,h)
        # self.rect = self.image.get_rect()

        self.h = h
        self.w = w
        self.rect.y = y
        self.rect.x = x
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.x >760:
            self.kill()
    

class Bullet2(sprite.Sprite):
    def __init__(self,x,y,picture,h,w,speed):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))
        self.rect = Rect(x,y,w,h)
        # self.rect = self.image.get_rect()

        self.h = h
        self.w = w
        self.rect.y = y
        self.rect.x = x
        self.speed = speed
        self.image = transform.flip(self.image,True,False)
    def update(self):
        self.rect.x -= self.speed
        
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.x >760:
            self.kill()
   


ex1 = Gamesprite(500,20,400,120,'wall.png')
ex2 = Gamesprite(280,20,0,120,'wall.png')
ex3 = Gamesprite(20,350,400,120,'wall.png')
ex5 = Gamesprite(20,220,120,250,'wall.png')
ex7 = Gamesprite(20,720,0,0,'wall.png')
ex8 = Gamesprite(20,720,780,0,'wall.png')
ex4 = Gamesprite(280,20,130,250,'wall.png')
ex9 = Gamesprite(280,20,130,250,'wall.png')
ex6 = Gamesprite(790,20,0,0,'wall.png')
ex10 = Gamesprite(790,20,0,580,'wall.png')
ex11 = Gamesprite(340,20,300,450,'wall.png')
bitoc = Gamesprite(80,80,20,30,'bitoc.png')
bitoc2 = Gamesprite(80,80,300,300,'bitoc.png')
bitoc3 = Gamesprite(80,80,440,160,'bitoc.png')
bitcoins = sprite.Group()
bitcoins.add(bitoc,bitoc2,bitoc3)
# heart1 = Gamesprite(50,50,570,630,'heart.png')
# heart2 = Gamesprite(50,50,640,630,'heart.png')
# heart3 = Gamesprite(50,50,710,630,'heart.png')
# hearts = sprite.Group(heart1,heart2,heart3)
barriers = sprite.Group(ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11)
again = Gamesprite(340,130,220,350,'wall.png')
fin_sprite = Gamesprite(150,100,600,150,'wall.png')
player = Player(80,80,640,25,'kisspng-pac-man-games-ghosts-blue-ghost-cliparts-5a8481acd9bdc4.6128817115186333888919.png',0,0)
grou = sprite.Group(player)
enemy = Enemy(90,90,100,480,'kisspng-pac-man-world-3-pixel-art-pacman-world-3-5b2c87cfdaf1e7.6678387715296450078968.png',10)
enemy2 = Enemy(90,90,100,18,'kisspng-pac-man-world-3-pixel-art-pacman-world-3-5b2c87cfdaf1e7.6678387715296450078968.png',10)
finish = 1
enemies = sprite.Group(enemy,enemy2)
index = 0
# def time ():
#     import time
#     import pygame
#     for i in range(5, 0, -1):
#         font7 = pygame.font.SysFont('',50).render(str(i),True, (200,170,0))
#         time.sleep(1)
# time()
while run:
    from pygame import*
    
    if finish == 1:
        window.fill((0,0,0))
        
        time.delay(50)
        
        bullets.update()
        bullets.draw(window)
        barriers.draw(window)
        bitcoins.draw(window)
        # hearts.draw(window)
        enemies.draw(window)
        enemies.update()
        player.picture()  
        player.update()
        fin_sprite.picture()
        window.blit(font4,(630,180))
        window.blit(font5,(50,630))    
        
        if sprite.spritecollide(player,bitcoins,False):
            index += 1
            res = 'points:3/'+str(index)
            font5 = font.SysFont('',50).render((res),True, (200,170,0))
            window.blit(font5,(50,630))
        bitcoin_touched = sprite.spritecollide(player,bitcoins,False)
        for b in bitcoin_touched:
            b.kill() 
        bitcoins.update()
        

        if sprite.groupcollide(bullets,enemies,False,True):
            finish = 1
        sprite.groupcollide(bullets,barriers,True,False)
        
        # sprite.groupcollide(bullets,enemies,False,True)
        
    for i in event.get():
        if i.type == QUIT:
            run = False
        if sprite.collide_rect(player,fin_sprite):
            if index == 3: 
                finish = 2
            elif index != 3:
                finish = 3
        if sprite.spritecollide(player,enemies,True):
            finish = 0
            
        
        elif i.type == KEYDOWN:
            if i.key == K_LEFT:
                player.x_speed = -9
            elif i.key == K_RIGHT:
                player.x_speed = 9
            elif i.key == K_UP:
                player.y_speed = -9
            elif i.key == K_DOWN:
                player.y_speed = 9
            elif i.key == K_d:               
                player.shoot()
            elif i.key == K_a:
                player.shoot2()
                
              
                
        elif i.type == KEYUP:
            player.x_speed = 0
            player.y_speed = 0
        if finish == 2 or finish == 0 or finish == 3:
            window.fill((0,0,0))
            again.picture()
            window.blit(font1,(again.rect.x+110,again.rect.y+40))
            if finish == 3:               
                window.blit(font6,(170,250))
                window.blit(font3,(285,160))

            elif finish == 2:
                window.blit(font2,(300,250))
            else:
                window.blit(font3,(285,250))
            if i.type == MOUSEBUTTONDOWN:        
                x,y = i.pos
                if again.rect.collidepoint(x,y):
                    player = Player(80,80,640,25,'kisspng-pac-man-games-ghosts-blue-ghost-cliparts-5a8481acd9bdc4.6128817115186333888919.png',0,0)
                    finish = 1
                    enemies = sprite.Group(enemy,enemy2)
        
        
                    

                        
    display.update()



        


        

