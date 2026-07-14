import pygame 

pygame.init()

win = pygame.display.set_mode((500, 500))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(win,(0,125,222) ,pygame.Rect(30,30,60,60))

    pygame.display.flip()