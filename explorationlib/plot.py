import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from explorationlib.util import load


def plot_experiment(name):
    pass


def plot_targets(env,
                 figsize=(3, 3),
                 boundary=(1, 1),
                 color="black",
                 alpha=1.0,
                 label=None,
                 title=None,
                 ax=None):

    vec = np.vstack(env.targets)

    # Create a fig obj?
    if ax is None:
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)

    # !
    ax.scatter(vec[:, 0], vec[:, 1], color=color, label=label, alpha=alpha)
    ax.set_xlim(-boundary[0], boundary[0])
    ax.set_ylim(-boundary[1], boundary[1])
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Labels, legends, titles?
    if title is not None:
        ax.set_title(title)
    if label is not None:
        ax.legend()

    return ax


def plot_position2d(exp_data,
                    var_name="state",
                    boundary=(1, 1),
                    figsize=(3, 3),
                    color="black",
                    alpha=1.0,
                    label=None,
                    title=None,
                    ax=None):
    # fmt
    state = np.vstack(exp_data[var_name])

    # Create a fig obj?
    if ax is None:
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)

    # !
    ax.plot(state[:, 0], state[:, 1], color=color, label=label, alpha=alpha)
    ax.set_xlim(-boundary[0], boundary[0])
    ax.set_ylim(-boundary[1], boundary[1])
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Labels, legends, titles?
    if title is not None:
        ax.set_title(title)
    if label is not None:
        ax.legend()

    return ax


def plot_hist(exp_data,
              loglog=True,
              var_name="agent_l",
              bins=20,
              figsize=(3, 3),
              color="black",
              alpha=1.0,
              density=False,
              label=None,
              title=None,
              ax=None):

    # fmt
    x = np.asarray(exp_data[var_name])

    # Create a fig obj?
    if ax is None:
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)

    if loglog:
        bins = np.geomspace(x.min(), x.max(), bins)
        ax.set_xscale('log')
        ax.set_yscale('log')

    ax.hist(x, bins=bins, color=color, alpha=alpha, density=density)
    ax.set_xlabel("Length")
    ax.set_ylabel("Count")

    # Labels, legends, titles?
    if title is not None:
        ax.set_title(title)
    if label is not None:
        ax.legend()

    return ax