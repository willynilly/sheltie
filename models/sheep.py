from models.agent import Agent
from models.environment import Environment
from models.sheltie import Sheltie


class Sheep(Agent):

    def __init__(self):
        Agent.__init__(self)
        self.weight = 100
        self.energy = 500

    def update(self, environment: Environment):

        nearest_agent: Agent = environment.closest_agent(self)
        if isinstance(nearest_agent, Sheep):
            # move towards other sheep
            self.move_toward(nearest_agent)
        elif isinstance(nearest_agent, Sheltie):
            # move away from shelties
            self.move_away(nearest_agent)
        else:
            pass

        super().update(environment=environment)
