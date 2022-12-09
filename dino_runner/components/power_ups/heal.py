from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HEAL, HEAL_TYPE

class Heal(PowerUp):
    def __init__(self):
        self.image = HEAL
        self.type = HEAL_TYPE
        super().__init__(self.image, self.type)
