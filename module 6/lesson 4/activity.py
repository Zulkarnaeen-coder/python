import pygame 
import random

win_w,win_h = 500,400 
speed = 5
font =72

pygame.init()

bg = pygame.transform.scale(
    pygame.image.load(r"D:\Shahik Personal\coding\ \module 6\lesson 4\bg.jpg"), (win_w, win_h)
)

font = pygame.font.SysFont("times new roman",font)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("DodgerBlue"))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()

    def move(self, x_axis, y_axis):
        self.rect.x = max(min(self.rect.x + x_axis, win_w - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_axis, win_h - self.rect.height), 0)

win = pygame.display.set_mode((win_w,win_h))
pygame.display.set_caption("Sprite collision")
all_sprites = pygame.sprite.Group()

sp1 = Sprite(pygame.Color("black"), 50, 50)
all_sprites.add(sp1)

sp1.rect.x = random.randint(0, win_w - sp1.rect.width)
sp1.rect.y = random.randint(0, win_h - sp1.rect.height)

sp2 = Sprite(pygame.Color("red"), 50, 50)
all_sprites.add(sp2)

sp2.rect.x = random.randint(0, win_w - sp2.rect.width)
sp2.rect.y = random.randint(0, win_h - sp2.rect.height)

run , won = True, False
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False 

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed

        sp1.move(x_change, y_change)

        if sp1.rect.colliderect(sp2.rect):
            all_sprites.remove(sp2)
            won = True 

        win.blit(bg,(0,0))
        all_sprites.draw(win)

        if won :
            text = font.render("You won!", True, pygame.Color("black"))
            win.blit(text,(win_w//2 - text.get_width()//2, win_h//2 - text.get_height()//2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
