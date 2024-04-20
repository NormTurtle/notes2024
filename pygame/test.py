import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((500,700))

while True:
    # update elemnet
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
