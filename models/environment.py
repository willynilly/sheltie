
from __future__ import annotations

import math
from models.agent import Agent


class Environment:
    agents: list[Agent] = []

    def closest_agent(self, target_agent: Agent) -> Agent:
        closest_agent: Agent = self.agents[0]
        for agent in self.agents:
            if self.distance_between_agents(agent, target_agent) < self.distance_between_agents(closest_agent, target_agent):
                closest_agent = agent
        return closest_agent

    def distance_between_agents(self, agent_a: Agent, agent_b: Agent) -> float:
        return math.sqrt(math.pow(agent_a.x - agent_b.x, 2) + math.pow(agent_a.y - agent_b.y, 2))

    def update(self, time_steps: int):
        for i in range(time_steps):
            for agent in self.agents:
                agent.update(environment=self)
