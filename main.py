
from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed):
      super().__init__()
      self.image = transform.scale(image.load(player_image), (65, 65))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y

   def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   def update(self):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 5:
         self.rect.x -= self.speed  #! self.rect.x = self.rect.x - 1
      if keys[K_RIGHT] and self.rect.x < win_width- 80:
         self.rect.x += self.speed
      if keys[K_UP] and self.rect.y > 5:
         self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < win_height - 80:
         self.rect.y += self.speed


class Enemy(GameSprite):
   direction = "left"
   def update(self):
      if self.rect.x <= 500:
          self.direction = "right"
      if self.rect.x >= win_width-85:
          self.direction = "left"
      if self.direction == "left":
          self.rect.x -= self.speed
      else:
          self.rect.x += self.speed


class Enemy2(GameSprite):
   direction = "up"
   def update(self):
      if self.rect.y <= 0:
          self.direction = "down"
      if self.rect.y >= win_width-560:
          self.direction = "up"
      if self.direction == "up":
          self.rect.y -= self.speed
      else:
          self.rect.y += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
         super().__init__()
         self.color_1 = color_1
         self.color_2 = color_2
         self.color_3 = color_3
         self.width = wall_width
         self.height = wall_height
         self.image = Surface((self.width, self.height))
         self.image.fill((color_1, color_2, color_3))
         self.rect = self.image.get_rect()
         self.rect.x = wall_x
         self.rect.y = wall_y
    def draw_wall(self):
     window.blit(self.image, (self.rect.x, self.rect.y))


win_width = 700
win_height = 500

window = display.set_mode((700, 500))
display.set_caption("Лабіринт")


player = Player("hero.png", 5, win_height-80, 4)
monster = Enemy("cyborg.png", win_width-80, 280, 2)
final = GameSprite("treasure.png", win_width-120, win_height-80, 0)
monster2 = Enemy2("jennie.png", win_width-500, 80, 2)

w1 = Wall(0, 0, 139, 220, 200, 10, 380)
w2 = Wall(0, 0, 139, 100, 0, 10, 380)
w3 = Wall(0, 0, 139, 340, 0, 10, 380)
w4 = Wall(0, 0, 139, 460, 120, 10, 380)

background = transform.scale(image.load("background.jpg"), (700, 500))
speed = 10
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('ITZY_Cheshire.wav')
mixer.music.play()

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255, 215, 0))

lose = font.render('YOU LOSE!', True, (255, 215, 0))




finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()
        monster2.update()

        player.reset()
        monster.reset()
        monster2.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()

        if sprite.collide_rect(player, final):
            window.blit(win, (200, 200))
            finish = True
            money = mixer.Sound('money.ogg')
            money.play()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2)  or sprite.collide_rect(player, w4):
            window.blit(lose, (200, 200))
            finish = True
            kick = mixer.Sound('kick.ogg')
            kick.play()


    display.update()
    clock.tick(FPS)


