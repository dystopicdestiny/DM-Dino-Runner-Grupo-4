#from pygame.sprite import Sprite
#from pygame.surface import Surface
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    Y_POS_BIRD = 325

    def __init__(self, image):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.step_index = 0
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = self.Y_POS_BIRD

    def update(self, game_speed, obstacles: list):
        self.fly()
        super().update(game_speed, obstacles)

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1
        if self.step_index >= 10:
            self.step_index = 0
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))