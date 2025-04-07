import arcade
from enum import Enum


class AttackType(Enum):
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2


class AttackAnimation(arcade.sprite):
    ATTACK_SCALE = 0.5
    ANIMATION_SPEED = 5

    def __init__(self, attack_type):
        super().__init__()
        self.animation_update_time = 1 / AttackAnimation.ANIMATION_SPEED
        self.time_since_last_swap = 0
        self.attack_type = attack_type
        if self.attack_type == AttackType.ROCK:
            self.textures = [
                arcade.load_texture("assets/srock.png"),
                arcade.load_texture("assets/srock-attack.png")
            ]
        elif self.attack_type == AttackType.PAPER:
            self.textures = [
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/spaper-attack.png")
            ]
        else:
            self.textures = [
                arcade.load_texture("assets/spaper.png"),
                arcade.load_texture("assets/spaper-attack.png")
                ]

            self.scale = self.Attack_Scale
            self.current_texture = 0
            self.set_texture(self.current_texture)

    def on_update(self, delta_time: float = 1 / 60):
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
