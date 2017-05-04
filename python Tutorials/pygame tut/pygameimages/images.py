import pygame

pygame.init()

window = pygame.display.set_mode((800,600))

pygame.display.set_caption("Window")

black = (0,0,0)

white = (255,255,255)

image=pygame.image.load("C:/Users/Kwaku/Documents/Uni Work/FINAL YEAR PROJECT/python code/pygame tut/pygameimages/images/python_logo.png").convert_alpha()

gameLoop=True
while gameLoop:

    for event in pygame.event.get():

        if (event.type==pygame.QUIT):

            gameLoop=False

    window.fill(white)

    window.blit(image, (0,0))

    pygame.display.flip()

pygame.quit()
