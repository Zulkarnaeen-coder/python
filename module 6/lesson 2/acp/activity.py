import pygame

pygame.init()

win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My Game")
green = (0, 255, 0)
blue = (0, 0, 255)

win.fill((255, 255, 255))

pygame.draw.rect(win, green, pygame.Rect(30, 30, 60, 60))
pygame.draw.rect(win, blue, pygame.Rect(100, 205, 60, 60))

pygame.display.update()
done = True
while done:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            done = False

pygame.quit()
