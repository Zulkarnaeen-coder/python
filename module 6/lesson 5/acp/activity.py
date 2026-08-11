import math
import random
import pygame

win_wid, win_hei = 800, 500

player_start_X = 384
player_start_Y = 420
enemy_Y_min = 50
enemy_Y_max = 150
enemy_speed_X = 4
enemy_speed_Y = 30
Bullet_speed_Y = 12
collision_distance = 20
spr_size = 32

pygame.init()
win = pygame.display.set_mode((win_wid, win_hei))
pygame.display.set_caption("Battle Field")

try:
    bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (win_wid, win_hei))
    playerimg = pygame.transform.scale(
        pygame.image.load("army.png"), (spr_size, spr_size)
    )
    bulletimg = pygame.transform.scale(pygame.image.load("bl.png"), (12, 24))
    has_image = True
except Exception:
    has_image = False


playerX = player_start_X
playerY = player_start_Y
player_X_change = 0


enemyimg = []
enemyX = []
enemyY = []
enemy_X_change = []
enemy_Y_change = []
enemy_number = 6

for i in range(enemy_number):
    if has_image:
        enemyimg.append(
            pygame.transform.scale(pygame.image.load("enemy.png"), (spr_size, spr_size))
        )
    enemyX.append(random.randint(0, win_wid - spr_size))
    enemyY.append(random.randint(enemy_Y_min, enemy_Y_max))
    enemy_X_change.append(enemy_speed_X)
    enemy_Y_change.append(enemy_speed_Y)


bulletX = 0
bulletY = player_start_Y
bullet_state = "ready"


score_vl = 0
font = pygame.font.Font("freesansbold.ttf", 32)
fontX = 10
fontY = 10


font_over = pygame.font.Font("freesansbold.ttf", 64)
game_over_flag = False


def show_score(x, y):
    score_render = font.render("Score : " + str(score_vl), True, (255, 255, 255))
    win.blit(score_render, (x, y))


def game_over_text(x, y):
    over_text = font_over.render("GAME OVER", True, (255, 255, 255))
    win.blit(over_text, (x, y))


def player(x, y):
    if has_image:
        win.blit(playerimg, (x, y))
    else:
        
        pygame.draw.rect(win, (50, 255, 205), (x, y, spr_size, spr_size))


def enemy(x, y, i):
    if has_image:
        win.blit(enemyimg[i], (x, y))
    else:
        
        pygame.draw.rect(win, (255, 42, 12), (x, y, spr_size, spr_size))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    if has_image:
        win.blit(bulletimg, (x + 10, y - 10))
    else:
        pygame.draw.rect(win, (255, 255, 0), (x + 13, y, 6, 16))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < collision_distance


clock = pygame.time.Clock()
run = True

while run:
    clock.tick(60)
    win.fill((0, 0, 0))

    if has_image:
        win.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_X_change = -6
            if event.key == pygame.K_RIGHT:
                player_X_change = 6
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            player_X_change = 0

    playerX += player_X_change
    playerX = max(0, min(playerX, win_wid - spr_size))

    
    for i in range(enemy_number):
        if enemyY[i] > 380:
            game_over_flag = True
            for j in range(enemy_number):
                enemyY[j] = 2000
            break

        enemyX[i] += enemy_X_change[i]

        
        if enemyX[i] <= 0:
            enemy_X_change[i] = enemy_speed_X
            enemyY[i] += enemy_Y_change[i]
        elif enemyX[i] >= win_wid - spr_size:
            enemy_X_change[i] = -enemy_speed_X
            enemyY[i] += enemy_Y_change[i]

        
        if bullet_state == "fire" and iscollision(
            enemyX[i], enemyY[i], bulletX, bulletY
        ):
            bulletY = player_start_Y
            bullet_state = "ready"
            score_vl += 1
            enemyX[i] = random.randint(0, win_wid - spr_size)
            enemyY[i] = random.randint(enemy_Y_min, enemy_Y_max)

        enemy(enemyX[i], enemyY[i], i)

 
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= Bullet_speed_Y

    if bulletY <= 0:
        bulletY = player_start_Y
        bullet_state = "ready"

    player(playerX, playerY)
    show_score(fontX, fontY)

    if game_over_flag:
        game_over_text(200, 200)

    pygame.display.update()

pygame.quit()
