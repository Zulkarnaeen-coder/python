import pygame 

pygame.init()

win = pygame.display.set_mode((500,500))

green = (0,255,0)

pygame.draw.circle(win,green,(300,300),50)

pygame.draw.circle(win,green,(100,100),50,3)

pygame.display.update()
done = True
while done:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            done = False

pygame.quit()