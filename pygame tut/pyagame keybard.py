import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load("C:/Users/Kwaku/Documents/Uni Work/FINAL YEAR PROJECT/python code/pygame tut/images/racecar.png")


def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
		print(event)
            elif event.key == pygame.K_RIGHT:
                x_change = 5
		print(event)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
		print(event)
        ######################
    ##
    x += x_change
   ##         
    gameDisplay.fill(white)
    car(x,y)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()