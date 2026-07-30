import math
import random
import pygame

win_wid ,win_hei = 800,500
player_start_X =384
player_start_Y = 420
enemy_Y_min = 50
enemy_Y_max = 150
enemy_speed_X = 4
enemy_speed_Y = 30
Bullet_speed_Y = 12
collision_distance = 20
spr_size = 32

pygame.init()
win = pygame.display.set_mode((win_wid,win_hei))
pygame.display.set_caption("Space Invaders")



try:
    bg = pygame.transform.scale(pygame.image.load('bg.jpg'),(win_wid,win_hei))
    playerimg = pygame.transform.scale(pygame.image.load('spaceship.png'),(spr_size,spr_size))
    bulletimg = pygame.transform.scale(pygame.image.load('bl.png'),(12,24))
    has_image = True
except:
    has_image = False


#player 
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
    if has_image:
        enemyimg.append(pygame.transform.scale(pygame.image.load('enemy.png'),(spr_size,spr_size)))
        enemyX.append(random.randint(0, win_wid-spr_size))
        enemyY.append(random.randint(enemy_Y_min, enemy_Y_max))
        enemy_X_change.append(enemy_speed_X)
        enemy_Y_change.append(enemy_speed_Y)

#Bullet 
bulletX = 0
bulletY = player_start_Y
bullet_state = "ready"  

#win text
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
fontX = 10
fontY = 10


#game over text
font_over = pygame.font.Font('freesansbold.ttf', 64)
game_over_flag = False

def show_score(x, y):
    score = font.render("Score : " + str(score), True, (255, 255, 255))
    win.blit(score,(x, y))

def game_over_text(x,y):
    over_text = font_over.render("GAME OVER", True, (255, 255, 255))
    win.blit(over_text, (x,y))

def player(x, y):
    if has_image:
        win.blit(playerimg, (x, y))
    else:
        pygame.draw.rect(win, (255, 0, 0), (x, y, spr_size, spr_size))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    if has_image:
        win.blit(bulletimg, (x + 10, y - 10))
    else:
        pygame.draw.rect(win, (255, 255, 0), (x + 13, y, 6, 16))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
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
                playerX = -6

            if event.key == pygame.K_RIGHT:
                playerY = 6

            if event.key == pygame.K_SPACE and bullet_state =="ready":
                bulletX = playerX
                fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT ,pygame.K_RIGHT]:
            player_X_change = 0

    playerX += player_X_change
    playerX = max(0,min(playerX,win_wid - spr_size))

    for i in range(enemy_number):
        if enemyY[i] >380:
            game_over_flag = True
            for j in range(enemy_number):
                enemyY[j] =2000
            break

        enemyX[i] +=enemy_X_change[i]
        if enemyX[i] <=0 or enemyX[i] >= win_wid - spr_size:
            enemy_X_change[i] *=-1

            if bullet_state =="fire" and iscollision(enemyX[i],enemyY[i],bulletX,bulletY):
                bulletY = player_start_Y
                bullet_state = "ready"
                score +=1
                enemyX[i] = random.randint(0,win_wid = spr_size)
                enemyY[i] = random.randint(enemy_Y_min,enemy_Y_max)

            enemy(enemyX[i],enemyY[i],i)


        if bullet_state == "fire":
            fire_bullet(bulletX,bulletY)
            bulletY -= Bullet_speed_Y

        if bulletY <= 0:
            bulletY = player_start_Y
            bullet_state = "ready"

        player(playerX,playerY)

        if game_over_flag:
            game_over_text()

        pygame.display.update()


pygame.quit()



    
