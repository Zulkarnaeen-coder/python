import math
import random
import pygame

win_wid ,win_hei = 800,500
player_start_X =370
player_start_Y = 380
enemy_Y_min = 50
enemy_Y_max = 150
enemy_speed_X = 4
enemy_speed_Y = 40
Bullet_speed = 10
collision_distance = 27

pygame.init()
win = pygame.display.set_mode((win_wid,win_hei))
bg = pygame.image.load('bg.jpg')
pygame.display.set_caption("Space Invaders")

#player 

playerimg = pygame.image.load('space.png')
playerX = player_start_X
playerY = player_start_Y
player_X_change = 0

#enemy

enemyimg = []
enemyX = []
enemyY = []
enemy_X_change = []
enemy_Y_change = []
enemy_number = 6

for i in range(enemy_number):
    enemyimg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, win_wid-64))
    enemyY.append(random.randint(enemy_Y_min, enemy_Y_max))
    enemy_X_change.append(enemy_speed_X)
    enemy_Y_change.append(enemy_speed_Y)

#Bullet 

bulletimg = pygame.image.load('bl.png')
bulletX = 0
bulletY = player_start_Y
bullet_X_change = 0
bullet_Y_change = Bullet_speed

#win text
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
fontX = 10
fontY = 10


#game over text
font_over = pygame.font.Font('freesansbold.ttf', 64)






