import math
import random
import pygame

win_wid , win_hei = 800, 500
player_str_X = 370
player_str_Y = 380
enemy_Y_min = 50
enemy_Y_max = 150
enemy_speed_X = 4
enemy_speed_Y = 40
Bullet_speed = 10
collision_distance = 27


pygame.init()
win = pygame.display.set_mode((win_wid, win_hei))
bg = pygame.image.load('bg.jpg')
pygame.display.set_caption("Battle field")


#player

playerimg = pygame.image.load('army.png')
playerX = player_str_X
playerY = player_str_Y
player_X_change = 0

#enemy

enemyimg = []
enemyX = []
enemyY = []
enemy_X_change = []
enemy_Y_change = []
num_of_enemies = 7


for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, win_wid-64))
    enemyY.append(random.randint(enemy_Y_min, enemy_Y_max))
    enemy_X_change.append(enemy_speed_X)
    enemy_Y_change.append(enemy_speed_Y)


#Score

score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
fontX = 10
fontY = 10

#GAME OVER  

font_over = pygame.font.Font("freesansbold.ttf", 64)