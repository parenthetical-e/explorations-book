import numpy as np

from copy import deepcopy
from scipy.stats import powerlaw
from collections import defaultdict


class Agent2d:
    """API stub - do not use."""
    def __init__(self):
        self.seed()
        self.history = defaultdict(list)

    def seed(self, seed=None):
        self.np_random = np.random.RandomState(seed)
        return [seed]

    def _angle(self, state):
        return self.np_random.uniform(0, 2 * np.pi)

    def _convert(self, angle, l):
        dx = l * np.cos(angle)
        dy = l * np.sin(angle)
        action = np.array([dx, dy])
        return action

    def forward(self, state):
        pass

    def __call__(self, state):
        return self.forward(state)

    def reset(self):
        self.agent_step = 0
        self.history = defaultdict(list)


class Uniform2d(Agent2d):
    """Uniform (maxent) search"""
    def __init__(self, scale=1):
        super().__init__()
        self.scale = scale

    def forward(self, state):
        angle = self._angle(state)
        l = self.np_random.uniform(0, self.scale)
        action = self._convert(angle, l)

        self.agent_step += 1
        self.history["agent_step"].append(deepcopy(self.agent_step))
        self.history["agent_angle"].append(angle)
        self.history["agent_l"].append(l)
        self.history["agent_action"].append(action)

        return action


class Diffusion2d(Agent2d):
    """Diffusion search"""
    def __init__(self, scale=1):
        super().__init__()
        self.scale = scale

    def forward(self, state):
        angle = self._angle(state)
        l = self.np_random.exponential(self.scale)
        action = self._convert(angle, l)

        self.agent_step += 1
        self.history["agent_step"].append(deepcopy(self.agent_step))
        self.history["agent_angle"].append(angle)
        self.history["agent_l"].append(l)
        self.history["agent_action"].append(action)

        return action


class Levy2d(Agent2d):
    """Levy search"""
    def __init__(self, exponent=2, norm=1):
        super().__init__()
        self.exponent = exponent
        self.norm = norm

    def forward(self, state):
        # Sample move
        angle = self._angle(state)
        l = np.power(self.np_random.uniform(), (-1 / self.exponent))
        action = self._convert(angle, l * self.norm)
        # Log
        self.agent_step += 1
        self.history["agent_step"].append(deepcopy(self.agent_step))
        self.history["agent_angle"].append(angle)
        self.history["agent_l"].append(l)
        self.history["agent_action"].append(action)

        return action


class TruncatedLevy2d(Agent2d):
    """Levy search, with a max l"""
    def __init__(self, exponent=2, norm=1, max_l=10):
        super().__init__()
        self.exponent = exponent
        self.norm = norm
        self.max_l = max_l

    def forward(self, state):
        # Sample move
        angle = self._angle(state)
        l = np.power(self.np_random.uniform(), (-1 / self.exponent))
        # Truncate?
        if l > self.max_l:
            l = self.max_l
        # Convert
        action = self._convert(angle, l * self.norm)
        # Log
        self.agent_step += 1
        self.history["agent_step"].append(deepcopy(self.agent_step))
        self.history["agent_angle"].append(angle)
        self.history["agent_l"].append(l)
        self.history["agent_action"].append(action)

        return action
