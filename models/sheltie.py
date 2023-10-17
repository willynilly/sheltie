from models.agent import Agent

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.sheep import Sheep


class Sheltie(Agent):

    def __init__(self):
        Agent.__init__(self)
        self.weight = 20
        self.energy = 2500
        self.annoyance = 0

    def bark(self, target_agent: Agent):

        if isinstance(target_agent, Sheep):
            target_agent.fear += 1
            if (target_agent.fear > 10):

                # move away from the sheltie
                target_agent.move_away(self)

        elif isinstance(target_agent, Sheltie):
            target_agent.excitement += 1

            # move away from the sheltie
            target_agent.move_toward(self)

        else:
            target_agent.annoyance += 1
