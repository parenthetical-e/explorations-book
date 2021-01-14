#! /usr/bin/env python
import numpy as np
import gym

from copy import deepcopy
from gym import spaces
from gym.utils import seeding
from itertools import cycle
from collections import defaultdict

# Gym is annoying these days...
import warnings
warnings.filterwarnings("ignore")


class Field(gym.Env):
    def __init__(self):
        self.info = {}
        self.reward = 0
        self.done = False

        self.targets = None
        self.values = None

        self.reset()

    def step(self, action):
        self.state += action

    def last(self):
        """Return the last transition: 
        (state, reward, done, info)
        """
        return (self.state, self.reward, self.done, self.info)

    def add_targets(self, targets, values):
        """Add targets and their values"""

        if len(targets) != len(values):
            raise ValueError("targets and values must match.")
        self.targets = targets
        self.values = values

    def check_targets(self, radius, d_func=None):
        """Check for targets, and update self.reward if
        some are found in the given radius.

        Note: the deault d_func is the euclidian distance. 
        To override provide a func(x, y) -> distance.
        """

        if d_func is None:
            d_func = lambda x, y: np.sqrt(np.sum(np.power(y - x, 2)))

        # Check for targets, build up 'reward' value
        reward = 0
        for i, l in enumerate(self.targets):
            distance = d_func(l, self.state)
            if distance <= radius:
                reward += self.values[i]

        # Set reward
        self.reward = reward

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        self.state = np.zeros(2)
        self.last()

    def render(self, mode='human', close=False):
        pass


class Grid(Field):
    def __init__(self):
        super().__init__()

    def step(self, action):
        if not isinstance(action[0], int):
            raise ValueError("action must contain int")
        if not isinstance(action[1], int):
            raise ValueError("action must contain int")

        super().step(action)

    def reset(self):
        self.state = np.zeros(2, dtype=int)
        self.last()


class Bounded(Field):
    def __init__(self, shape, mode="stopping"):
        self.shape = shape
        self.mode = mode

        # Sanity testing
        for s in shape:
            if s < 0:
                raise ValueError("shape must be positive")
            elif not np.isfinite(s):
                raise ValueError("shape must be finite")

        valid = ("stopping", "absorbing", "periodic")
        if self.mode not in valid:
            raise ValueError(f"mode must be {valid}")

    def step(self, action):
        # step
        super().step(action)

        # check bounds. clipping and stopping
        # in a mode dependent way
        for i, s in enumerate(self.state):
            if s > self.shape[i]:
                if self.mode == "stopping":
                    self.state[i] = self.shape[i]
                elif self.mode == "absorbing":
                    self.state[i] = self.shape[i]
                    self.done = True
                elif self.mode == "periodic":
                    raise NotImplementedError("[TODO]")
                else:
                    raise ValueError("Invalid mode")
