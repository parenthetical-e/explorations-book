# -*- coding: utf-8 -*-
# %% [markdown]
# Walk around/run around/fly around
#
# In this chapter we dill discuss the simplest method of exploration -- random searching. In some circumstance's we'll see random exploration is the best we can do, leading to some optimality claims. We decsribe what is optimal when, and review how animals actually behave. Examples both inline with, and contrary to, what the math says is best. 
#
# # Diffusion, Lévy flights, and patches. 
# %%
from explorationlib.run import experiment
from explorationlib import gym
from explorationlib import agent
from explorationlib.util import load
from explorationlib.util import save

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# %matplotlib inline
# %load_ext nb_black

# %%
env = gym.Field()
brown = agent.Diffusion2d(scale=1 / 2)
levy = agent.Levy2d(exponent=2)

# %%
experiment("levy.pkl", levy, env, num_steps=100, num_repeats=1)
experiment("brown.pkl", brown, env, num_steps=100, num_repeats=1)

levy_exp = load("levy.pkl")
brown_exp = load("brown.pkl")

levy_l = np.asarray(levy_exp["agent_history"]["l"])
levy_state = np.vstack(levy_exp["state"])

brown_l = np.asarray(brown_exp["agent_history"]["l"])
brown_state = np.vstack(brown_exp["state"])

# %%
np.random.uniform()

# %%
domain = 50

plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.title("Levy")
plt.plot(levy_state[:, 0], levy_state[:, 1], color="black")
plt.xlim(-domain, domain)
plt.ylim(-domain, domain)

plt.subplot(122)
plt.title("Brownian")
plt.plot(brown_state[:, 0], brown_state[:, 1], color="black")
plt.xlim(-domain, domain)
plt.ylim(-domain, domain)

# %%
plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.title("Levy")
_ = plt.hist(levy_l, color="black")
# plt.gca().set_xscale("log")

plt.subplot(122)
plt.title("Brownian")
_ = plt.hist(brown_l, color="black")
# plt.gca().set_xscale("log")

# %%

# %%

# %%
