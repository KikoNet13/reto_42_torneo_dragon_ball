import reflex as rx

from enum import Enum
from random import random

DODGE_CHANCE = 0.2
MIN_DAMAGE_RATIO = 0.1


class ActionType(Enum):
    ATTACK = "attack"
    DEFENSE = "defense"
    DODGE = "dodge"
    NONE = "none"


class Action(rx.Base):
    action_type: ActionType = ActionType.NONE
    value: int = 0

    def create_attack(self, attack: int):
        self.action_type = ActionType.ATTACK
        self.value = attack

    def create_defense(self, defense: int):
        if random() < DODGE_CHANCE:
            self.action_type = ActionType.DODGE
            self.value = 0
        else:
            self.action_type = ActionType.DEFENSE
            self.value = defense
