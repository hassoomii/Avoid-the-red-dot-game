import pygame
import sys
import random


class Screen:
    def __init__(self, width, height, x, y, r, g, b, alpha):
        self.screen_width = width
        self.screen_height = height
        self.screen_x = x
        self.screen_y = y
        self.screen_r = r
        self.screen_g = g
        self.screen_b = b
        self.screen_alpha = alpha

    def draw(self, screen):
        screen_surface = pygame.Surface((self.screen_width, self.screen_height))
        screen_surface_rect = screen_surface.get_rect(topleft=(self.screen_x, self.screen_y))
        screen_surface.fill(color=(self.screen_r, self.screen_g, self.screen_b, self.screen_alpha))
        screen.blit(screen_surface, screen_surface_rect.topleft)


class Font:
    def __init__(self, string, size, name, color, x, y):
        self.font_string = string
        self.font_size = size
        self.font_name = name
        self.font_color = color
        self.font_x = x
        self.font_y = y


    def draw(self, screen):
        font_set = pygame.font.Font(self.font_name, self.font_size)
        font_text = font_set.render(self.font_string, True, self.font_color)
        screen.blit(font_text, (self.font_x, self.font_y))


screen_width = 900
screen_height = screen_width * .75
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WOOOOOOOO")
clock = pygame.time.Clock()

game_over = False
game_started = False
start_screen = True

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if start_screen:
                start_screen = False
                game_started = True
            elif game_started:
                game_started = False
                game_over = True
            elif game_over:
                game_over = False
                start_screen = True

    if game_over:
        game_over_screen = Screen(screen_width / 2, screen_width / 2, screen_width / 4, screen_height / 5, 100, 50, 50, 0)
        game_over_screen.draw(screen)
    elif game_started:
        started_screen = Screen(screen_width, screen_height, 0, 0, 20, 100, 100, 0)
        started_screen.draw(screen)
    elif start_screen:
        start_screen_screen = Screen(screen_width, screen_height, 0, 0, 100, 50, 100, 255)
        start_screen_screen.draw(screen)
        start_screen_text = Font('Press space to start game!', 50, 'pokemonGBFONT.ttf', 'white', 0,0)
        start_screen_text.draw(screen)
