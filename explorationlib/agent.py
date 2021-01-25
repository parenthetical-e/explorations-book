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

    def _l(self, state):
        pass

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

    def update(self, *args):
        pass


class Uniform2d(Agent2d):
    """Uniform (maxent) search"""
    def __init__(self, min_l=0.1, max_l=1000, detection_radius=1):
        super().__init__()
        self.min_l = min_l
        self.max_l = max_l

        self.detection_radius = detection_radius

        self.l = 0
        self.delta = 0
        self.step = 0
        self.num_step = 0
        self.angle = 0

    def _l(self, state):
        l = self.np_random.uniform(self.min_l, self.max_l)
        return l

    def _delta(self, state):
        """delta - r * 4 steps for each l"""
        div = int(self.l / self.detection_radius) * 4
        if div > 1:
            delta = np.linspace(0, self.l, num=div)[1]
        else:
            delta = self.l
        return delta

    def forward(self, state):
        """Step the agent forward"""
        # -- Just go? --
        if self.l < self.step:
            turn = False
            self.step += self.delta
            self.num_step += 1
        # Or sample a turn?
        else:
            turn = True
            self.l = self._l(state)
            self.angle = self._angle(state)
            self.delta = self._delta(state)

            self.num_step += 0
            self.step = self.delta

        # !
        action = self._convert(self.angle, self.delta)

        # -- Log --
        self.history["agent_turn"].append(deepcopy(turn))
        self.history["agent_angle"].append(deepcopy(self.angle))
        self.history["agent_l"].append(deepcopy(self.l))
        self.history["agent_num_step"].append(deepcopy(self.num_step))
        self.history["agent_step"].append(deepcopy(self.step))
        self.history["agent_action"].append(deepcopy(action))

        return action


class Levy2d(Agent2d):
    """Levy search"""
    def __init__(self, min_l=0.1, exponent=2, detection_radius=1):
        super().__init__()
        self.min_l = min_l

        self.exponent = exponent
        self.detection_radius = detection_radius

        self.l = 0
        self.delta = 0
        self.step = 0
        self.num_step = 0
        self.angle = 0

    def _l(self, state):
        i = 0
        while True and i < 10000:
            i += 1
            l = np.power(self.np_random.uniform(), (-1 / self.exponent))
            if l > self.min_l:
                return l

    def _delta(self, state):
        """delta - r * 4 steps for each l"""
        div = int(self.l / self.detection_radius) * 4
        if div > 1:
            delta = np.linspace(0, self.l, num=div)[1]
        else:
            delta = self.l
        return delta

    def forward(self, state):
        """Step the agent forward"""
        # -- Just go? --
        if self.l < self.step:
            turn = False
            self.step += self.delta
            self.num_step += 1
        # Or sample a turn?
        else:
            turn = True
            self.l = self._l(state)
            self.angle = self._angle(state)
            self.delta = self._delta(state)

            self.num_step += 0
            self.step = self.delta

        # !
        action = self._convert(self.angle, self.delta)

        # -- Log --
        self.history["agent_turn"].append(deepcopy(turn))
        self.history["agent_angle"].append(deepcopy(self.angle))
        self.history["agent_l"].append(deepcopy(self.l))
        self.history["agent_num_step"].append(deepcopy(self.num_step))
        self.history["agent_step"].append(deepcopy(self.step))
        self.history["agent_action"].append(deepcopy(action))

        return action


class Diffusion2d(Agent2d):
    """Diffusion search"""
    def __init__(self, min_l=0.1, scale=2, detection_radius=1):
        super().__init__()
        self.min_l = min_l

        self.scale = scale
        self.detection_radius = detection_radius

        self.l = 0
        self.delta = 0
        self.step = 0
        self.num_step = 0
        self.angle = 0

    def _l(self, state):
        i = 0
        while True and i < 10000:
            i += 1
            l = self.np_random.exponential(self.scale)
            if l > self.min_l:
                return l

    def _delta(self, state):
        """delta - r * 4 steps for each l"""
        div = int(self.l / self.detection_radius) * 4
        if div > 1:
            delta = np.linspace(0, self.l, num=div)[1]
        else:
            delta = self.l
        return delta

    def forward(self, state):
        """Step the agent forward"""
        # -- Just go? --
        if self.l < self.step:
            turn = False
            self.step += self.delta
            self.num_step += 1
        # Or sample a turn?
        else:
            turn = True
            self.l = self._l(state)
            self.angle = self._angle(state)
            self.delta = self._delta(state)

            self.num_step += 0
            self.step = self.delta

        # !
        action = self._convert(self.angle, self.delta)

        # -- Log --
        self.history["agent_turn"].append(deepcopy(turn))
        self.history["agent_angle"].append(deepcopy(self.angle))
        self.history["agent_l"].append(deepcopy(self.l))
        self.history["agent_num_step"].append(deepcopy(self.num_step))
        self.history["agent_step"].append(deepcopy(self.step))
        self.history["agent_action"].append(deepcopy(action))

        return action


# class Diffusion2d(Agent2d):
#     """Diffusion search"""
#     def __init__(self, scale=1, detection_radius=1):
#         super().__init__()
#         self.scale = scale

#         self.num_turns = 0.0
#         self.num_step = 0.0

#         self.step_l = 0.0
#         self.turn_l = 0.0
#         self.delta_l = 0.0

#     def _l(self, state):
#         l = self.np_random.exponential(self.scale)
#         return l

#     def forward(self, state):
#         angle = self._angle(state)
#         l = self._l(state)
#         action = self._convert(angle, l)

#         self.agent_step += 1
#         self.history["agent_step"].append(deepcopy(self.agent_step))
#         self.history["agent_angle"].append(angle)
#         self.history["agent_l"].append(l)
#         self.history["agent_action"].append(action)

#         return action

# class Levy2d(Agent2d):
#     """Levy search"""
#     def __init__(self, exponent=2, detection_radius=1):
#         super().__init__()
#         self.exponent = exponent
#         self.detection_radius = detection_radius

#         self.num_turns = 0.0
#         self.num_step = 0.0

#         self.step_l = 0.0
#         self.turn_l = 0.0
#         self.delta_l = 0.0

#     def _l(self, state):
#         l = np.power(self.np_random.uniform(), (-1 / self.exponent))
#         return l

#     def forward(self, state):
#         # Keep going for this turn?
#         if self.step_l < self.turn_l:
#             self.step_l += self.delta_l
#         # Or make a new draw?
#         else:
#             # Reset
#             self.step_l = 0.0
#             self.delta_l = 0.0
#             # Draw
#             self.turn_angle = self._angle(state)
#             self.turn_l = self._l(state)
#             # Set delta_l
#             num_steps = self.turn_l / (self.detection_radius / 4)
#             self.delta_l = self.turn_l / num_steps

#             # Log this turn's data
#             self.num_turns += 1
#             self.history["agent_num_turns"].append(deepcopy(self.num_turns))
#             self.history["agent_angle"].append(deepcopy(self.turn_angle))
#             self.history["agent_l"].append(deepcopy(self.turn_l))

#         # Step
#         action = self._convert(self.step_l, self.turn_angle)

#         # Log step data
#         self.num_step += 1
#         self.history["agent_step"].append(deepcopy(self.agent_step))
#         self.history["agent_step_l"].append(deepcopy(self.step_l))
#         self.history["agent_step_angle"].append(deepcopy(self.turn_angle))
#         self.history["agent_step_action"].append(deepcopy(action))

#         return action

# class TruncatedLevy2d(Agent2d):
#     """Levy search, with a max l"""
#     def __init__(self, exponent=2, norm=1 max_l=10):
#         super().__init__()
#         self.exponent = exponent
#         self.norm = norm
#         self.max_l = max_l

#     def forward(self, state):
#         # Sample move
#         angle = self._angle(state)
#         l = np.power(self.np_random.uniform(), (-1 / self.exponent))
#         # Truncate?
#         if l > self.max_l:
#             l = self.max_l
#         # Convert
#         action = self._convert(angle, l * self.norm)
#         # Log
#         self.agent_step += 1
#         self.history["agent_step"].append(deepcopy(self.agent_step))
#         self.history["agent_angle"].append(angle)
#         self.history["agent_l"].append(l)
#         self.history["agent_action"].append(action)

#         return action

#     def update(self, *args):
#         pass
