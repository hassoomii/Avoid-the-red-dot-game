import pygame
import sys


class Screen:
    def __init__(self, width, height, x, y):
        self.screen_width = width
        self.screen_height = height
        self.screen_x = x
        self.screen_y = y


screen_width = 900
screen_height = screen_width * .75
pygame.init()
pygame.font.init()
pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WOOOOOOOO")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
