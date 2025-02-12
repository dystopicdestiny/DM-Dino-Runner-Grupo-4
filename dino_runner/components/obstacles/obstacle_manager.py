import random
import pygame

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        
        if len(self.obstacles) == 0:
            obstacle_random = random.randint(0,2)
            if obstacle_random == 0:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacle_random == 1:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if not (game.player.shield or game.player.hammer):
                if game.player.dino_rect.colliderect(obstacle.rect):
                    game.player_heart_manager.reduce_heart_count()
                    if game.player_heart_manager.heart_count > 0:
                        self.obstacles.pop()
                    else:
                        pygame.time.delay(1000)
                        game.playing = False
                        game.death_count += 1
            
            if game.player.hammer:
                if game.player.dino_rect.colliderect(obstacle.rect):
                    if game.player_heart_manager.heart_count > 0:
                        self.obstacles.pop()


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
