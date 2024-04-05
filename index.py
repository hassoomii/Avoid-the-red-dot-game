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

    def reset(self, width, height, x, y, r, g, b, alpha):
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
    def __init__(self, string, size, color, x, y):
        self.font_string = string
        self.font_size = size
        self.font_color = color
        self.font_x = x
        self.font_y = y
        self.font_score = 0
        self.font_top_score = 0

    def draw(self, screen):
        font_set = pygame.font.Font('pokemonGBFONT.ttf', self.font_size)
        font_text = font_set.render(self.font_string, True, self.font_color)
        screen.blit(font_text, (self.font_x, self.font_y))

    def add_score(self):
        self.font_score += 1

    def save_score(self):
        self.font_top_score = self.font_score
        self.font_score = 0


# regular variables
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
score = 0
high_score = 0


def init_player_values():
    player_1_x = screen_width / 40
    player_1_y = screen_height / 1.19
    player_1_width = screen_width / 10
    player_1_height = screen_width / 10
    player_1_r = random.randint(0, 10)
    player_1_g = random.randint(50, 60)
    player_1_b = random.randint(50, 60)
    player_1_alpha = 255
    moving_speed_x = 0
    moving_speed_y = 0
    return player_1_x, player_1_y, player_1_width, player_1_height, player_1_r, player_1_g, player_1_b, player_1_alpha, moving_speed_x, moving_speed_y


def init_dot_values():
    dot_x = screen_width / 1.2
    dot_y = screen_height / 10
    dot_width = screen_width / 30
    dot_height = screen_width / 30
    dot_r = random.randint(60, 120)
    dot_g = random.randint( 20, 50)
    dot_b = random.randint(20, 50)
    dot_alpha = 255
    dot_speed_x = 3
    dot_speed_y = 3
    return dot_x, dot_y, dot_width, dot_height, dot_r, dot_g, dot_b, dot_alpha, dot_speed_x, dot_speed_y


player_1_x, player_1_y, player_1_width, player_1_height, player_1_r, player_1_g, player_1_b, player_1_alpha, moving_speed_x, moving_speed_y = init_player_values()

dot_x, dot_y, dot_width, dot_height, dot_r, dot_g, dot_b, dot_alpha, dot_speed_x, dot_speed_y = init_dot_values()

# game loop
while True:
    pygame.display.update()
    game_over_screen = Screen(screen_width / 2, screen_width / 2, screen_width / 4, screen_height / 5, 100, 50, 50, 100)
    game_over_text_1 = Font(f'Game over with {score} points', 15, 'white', screen_width / 3.5, screen_width / 3)
    game_over_text_2 = Font('Press space to restart', 15, 'white', screen_width / 3.5, screen_width / 2.5)
    started_screen = Screen(screen_width, screen_height, 0, 0, 20, 100, 100, 255)
    started_screen_rect = pygame.Rect(0, 0, screen_width, screen_height)
    started_text = Font(f'Score: {score} High score: {high_score} Press space to end game', 15, 'white',
                        screen_width / 35, screen_width / 35)
    start_screen_screen = Screen(screen_width, screen_height, 0, 0, 100, 50, 100, 255)
    start_screen_text = Font('Press space to start game', 25, 'white', screen_width / 6.5, screen_width / 3)
    player_1 = Screen(player_1_width, player_1_height, player_1_x, player_1_y, player_1_r, player_1_g, player_1_b,
                      player_1_alpha)
    player_1_rect = pygame.Rect(player_1.screen_x, player_1.screen_y, player_1.screen_width, player_1.screen_height)
    red_dot = Screen(dot_width, dot_height, dot_x, dot_y, dot_r, dot_g, dot_b, dot_alpha)
    red_dot_rect = pygame.Rect(red_dot.screen_x, red_dot.screen_y, red_dot.screen_width, red_dot.screen_height)
    player_1_x += moving_speed_x
    player_1_y -= moving_speed_y


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start_screen:
                    start_screen = False
                    game_started = True
                elif game_started:
                    game_started = False
                    game_over = True
                elif game_over:
                    game_over = False
                    start_screen = True
            elif event.key == pygame.K_UP:
                moving_speed_y = 5
            elif event.key == pygame.K_DOWN:
                moving_speed_y = -5
            elif event.key == pygame.K_RIGHT:
                moving_speed_x = 5
            elif event.key == pygame.K_LEFT:
                moving_speed_x = -5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                moving_speed_y = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                moving_speed_x = 0
    if player_1_rect.left > screen_width:
        player_1_x = 0 - player_1_width
    elif player_1_rect.right < 0:
        player_1_x = screen_width
    elif player_1_rect.top > screen_height:
        player_1_y = 0 - player_1_width
    elif player_1_rect.bottom < 0:
        player_1_y = screen_height
    elif red_dot_rect.top <= 0 or red_dot_rect.bottom >= screen_height:
        dot_speed_y *= -1

    if game_over:
        player_1_x, player_1_y, player_1_width, player_1_height, player_1_r, player_1_g, player_1_b, player_1_alpha, moving_speed_x, moving_speed_y = init_player_values()
        dot_x, dot_y, dot_width, dot_height, dot_r, dot_g, dot_b, dot_alpha, dot_speed_x, dot_speed_y = init_dot_values()
        game_over_screen.draw(screen)
        game_over_text_1.draw(screen)
        game_over_text_2.draw(screen)
    elif game_started:
        dot_x -= dot_speed_x
        dot_y += dot_speed_y
        started_screen.draw(screen)
        red_dot.draw(screen)
        player_1.draw(screen)
        started_text.draw(screen)
    elif start_screen:
        start_screen_screen.draw(screen)
        start_screen_text.draw(screen)

    pygame.display.flip()
    clock.tick(60)
