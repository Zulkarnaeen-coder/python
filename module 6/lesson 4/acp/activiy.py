import random
import pygame

win_w, win_h = 500, 400
speed = 5
font_size = 72


COLORS = [
    pygame.Color("yellow"),
    pygame.Color("magenta"),
    pygame.Color("orange"),
    pygame.Color("white"),
    pygame.Color("blue"),
    pygame.Color("lightblue"),
    pygame.Color("darkblue"),
    pygame.Color("red"),
    pygame.Color("green"),
]

pygame.init()
font = pygame.font.SysFont("times new roman", font_size)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(color)

    def move(self, x_axis, y_axis):
        self.rect.x = max(min(self.rect.x + x_axis, win_w - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_axis, win_h - self.rect.height), 0)


win = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Sprite Collision")


bg_color, sp1_color, sp2_color = random.sample(COLORS, 3)


sp1_width, sp1_height = random.randint(30, 80), random.randint(30, 80)
sp2_width, sp2_height = random.randint(30, 80), random.randint(30, 80)


sp1 = Sprite(sp1_color, sp1_width, sp1_height)
sp1.rect.x = random.randint(0, win_w - sp1.rect.width)
sp1.rect.y = random.randint(0, win_h - sp1.rect.height)

sp2 = Sprite(sp2_color, sp2_width, sp2_height)
sp2.rect.x = random.randint(0, win_w - sp2.rect.width)
sp2.rect.y = random.randint(0, win_h - sp2.rect.height)

all_sprites = pygame.sprite.Group()
all_sprites.add(sp1, sp2)

run, won = True, False
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            run = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * speed

        sp1.move(x_change, y_change)

        if sp1.rect.colliderect(sp2.rect):
            all_sprites.remove(sp2)
            won = True

    
    win.fill(bg_color)
    all_sprites.draw(win)

    if won:
        text = font.render("You won!", True, pygame.Color("black"))
        win.blit(
            text,
            (
                win_w // 2 - text.get_width() // 2,
                win_h // 2 - text.get_height() // 2,
            ),
        )

    pygame.display.flip()
    clock.tick(90)

pygame.quit()

