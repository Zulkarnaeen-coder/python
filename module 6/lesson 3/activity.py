import pygame
import random

sprite_color_change_event = pygame.USEREVENT + 1
bg_color_change_event = pygame.USEREVENT + 2

#Colors = sp

blue  = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
magenta = (255, 0, 255)

#color = bg

light_blue = (173, 216, 230)
light_green = (144, 238, 144)
dark_gray = (169, 169, 169)
white = (255, 255, 255)


class sprite(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.Surface([500,400])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = (random.randint(-5, 5), random.randint(-5, 5))
        
        def update(self):
            self.rect.move_ip(self.speed)
            if self.rect.left <= 0 or self.rect.right >= 500:
                self.speed[0] =-self.speed[0]
            if self.rect.top <= 0 or self.rect.bottom >= 400:
                self.speed[1] =-self.speed[1]

            