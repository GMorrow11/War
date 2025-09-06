import pygameRunner
import pygame
screen = pygame.display.set_mode((1200, 1200))
running = True
while running == True:
    screen.fill((54, 89, 74)) # Green background
    #center of the screen is something like (550,350)
    screen.blit(pygameRunner.cardImg,(550,500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()