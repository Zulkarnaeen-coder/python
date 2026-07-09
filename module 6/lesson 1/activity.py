import pygame

pygame.init()

win = pygame.display.set_mode((400, 300))
pygame.display.set_caption("My first game")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()

pygame.quit()
