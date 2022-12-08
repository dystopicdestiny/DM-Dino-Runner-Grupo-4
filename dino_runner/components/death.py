import pygame

from dino_runner.utils.constants import FONT_STYLE, DEATH, SCREEN_HEIGHT, SCREEN_WIDTH


class Death:
    def __init__(self):
        self. death_count = 0

    def death(self):
        self.death_count += 1

    def draw(self, screen):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        
        font = pygame.font.Font(FONT_STYLE, 30)
        message = font.render("Try again", True, (0, 0, 0))
        message_rect = message.get_rect()
        message_rect.center = (1000, 50)
        screen.blit(message, message_rect)
        screen.blit(DEATH[0], (half_screen_width - 30, half_screen_height - 140))
        message = font.render(f"You death: {self.death_count} times", True, (0, 0, 0))
        message_rect = message.get_rect()
        message_rect.midbottom = (half_screen_width, half_screen_height + 100)
        screen.blit(message, message_rect)

