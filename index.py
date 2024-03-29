import pygame
import sys

pygame.init()
pygame.font.init()
pygame.display.set_mode((800, 900))
pygame.display.set_caption("WOOOOOOOO")
clock = pygame.time.Clock()

class Screen:
    def __init__(self):
        self.screen_width = 8700
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

