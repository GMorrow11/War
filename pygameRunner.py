import pygame
import random

pygame.init()
cards = [
    'AceH', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13',
    'AceD', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13',
    'AceC', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13',
    'AceS', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'
]

activeCard = cards[random.randint(0, len(cards) - 1)]

screen = pygame.display.set_mode((1200, 1200))
cardImg = pygame.image.load('/Users/Gavin/Documents/Python/Swoop/Cards Copy/' + str(activeCard) + '.png').convert_alpha()
cardImg = pygame.transform.scale(cardImg, (cardImg.get_width() * 0.4, cardImg.get_height() * 0.4))

running = True
while running == True:
    screen.fill((54, 89, 74)) # Green background
    #center of the screen is something like (550,350)
    screen.blit(cardImg,(550,500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()