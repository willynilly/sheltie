from models.agent import Agent
from models.sheep import Sheep
from models.sheltie import Sheltie


class Human(Agent):

    def __init__(self):
        Agent.__init__(self)
        self.weight = 100
        self.energy = 1000
        self.annoyance = 100

    def whistle(self, target_agent: Agent):

        if isinstance(target_agent, Sheltie):
            target_agent.excitement += 1
            # move away from the sheltie
            target_agent.move_toward(self)
        else:
            target_agent.annoyance += 1
