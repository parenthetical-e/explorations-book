import numpy as np
from scipy.stats import powerlaw


class Agent2d:
    """API stub - do not use."""
    def __init__(self):
        self.seed()
        self.history = {}

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
        self.forward(state)


class Diffusion2d(Agent2d):
    def __init__(self, scale=1):
        super().__init__()
        self.scale = scale

    def forward(self, state):
        angle = self._angle(state)
        l = self.np_random.exponential(self.scale)

        action = self._convert(angle, l)
        self.history["action"].append(action)

        return action


class Levy2d(Agent2d):
    def __init__(self, exponent=3):
        super().__init__()
        self.exponent = exponent

    def forward(self, state):
        angle = self._angle(state)
        l = powerlaw.rvs(self.exponent, size=1, random_state=self.np_random)

        action = self._convert(angle, l)
        self.history["action"].append(action)

        return action
