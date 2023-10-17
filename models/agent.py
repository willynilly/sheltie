from __future__ import annotations

import math

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.environment import Environment


class Agent:

    name: str
    weight: float

    annoyance: float
    excitement: float
    fear: float

    energy: float
    energy_lost_per_weight_per_unit_movement: float

    x: float
    y: float

    def __init__(self):
        self.name = ''
        self.weight = 1
        self.energy = 1000
        self.energy_lost_per_weight_per_unit_movement = 1
        self.x = 0
        self.y = 0
        self.fear = 0
        self.annoyance = 0
        self.excitement = 0

    def move(self, x_change, y_change):
        self.x = self.x + x_change
        self.y = self.y + y_change
        self.energy -= self.energy_lost_per_weight_per_unit_movement * \
            self.weight * \
            math.sqrt(math.pow(x_change, 2) + math.pow(y_change, 2))

    def move_away(self, target_agent: Agent):
        if (self.x > target_agent.x):
            self.move(x_change=1, y_change=0)
        else:
            self.move(x_change=-1, y_change=0)

        if (self.y > target_agent.y):
            self.move(x_change=0, y_change=1)
        else:
            self.move(x_change=0, y_change=-1)

    def move_toward(self, target_agent: Agent):
        if (self.x > target_agent.x):
            self.move(x_change=-1, y_change=0)
        else:
            self.move(x_change=1, y_change=0)

        if (self.y > target_agent.y):
            self.move(x_change=0, y_change=-1)
        else:
            self.move(x_change=0, y_change=1)

    def update(self, environment: Environment):
        print('Name' + self.name)
        print(str(self.x) + ', ' + str(self.y))
        print('')
