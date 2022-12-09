import random
import pygame
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.heal import Heal
from dino_runner.components.player_hearts.player_heart_manager import  PlayerHeartManager
from dino_runner.utils.constants import HAMMER_TYPE, HEAL_TYPE, SHIELD_TYPE

class PowerUpManager:
    def __init__(self, heart_manager):
        self.power_ups = []
        self.when_appears = 0
        self.heart = heart_manager

    def generate_power_up(self, current_score):
        if len(self.power_ups) == 0:
            power_random = random.randint(0,2)
            if self.when_appears == current_score:
                if power_random == 0:
                    self.when_appears = random.randint(self.when_appears + 100, self.when_appears + 200)
                    self.power_ups.append(Shield())
                elif power_random == 1:
                    self.when_appears = random.randint(self.when_appears + 100, self.when_appears + 200)
                    self.power_ups.append(Hammer())
                elif power_random == 2:
                    self.when_appears = random.randint(self.when_appears + 100, self.when_appears + 200)
                    self.power_ups.append(Heal())

    def update(self, current_score, game_speed, player, screen):
        self.generate_power_up(current_score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up.type == SHIELD_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    player.shield = True
                    player.show_text = True
                    player.type = power_up.type
                    time_random = random.randint(5, 7)
                    player.shield_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                if power_up.type == HAMMER_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    player.hammer = True
                    player.show_text = True
                    player.type = power_up.type
                    time_random = random.randint(5, 7)
                    player.hammer_time_up = power_up.start_time + (time_random * 1000)
                    self.power_ups.remove(power_up)
                if power_up.type == HEAL_TYPE:
                    power_up.start_time = pygame.time.get_ticks()
                    self.heart.increase_count_heart()
                    self.heart.update(screen)
                    self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(100, 200)












