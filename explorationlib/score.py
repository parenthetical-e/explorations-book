import numpy as np
from scipy import stats


def summary2d(exp_data,
              target_name="reward",
              length_name="agent_l",
              angle_name="agent_angle"):
    """2d search summary, as a dict"""

    rew = average_reward(exp_data, target_name=target_name)
    eta = search_efficient(exp_data,
                           length_name=length_name,
                           target_name=target_name)
    rat = turn_ratio(exp_data, length_name=length_name, angle_name=angle_name)

    return {"average_reward": rew, "search_efficient": eta, "turn_ratio": rat}


def average_reward(exp_data, target_name="reward"):
    """Average targets found"""
    reward = np.asarray(exp_data[target_name])
    return np.mean(reward)


def search_efficient(exp_data, length_name="agent_l", target_name="reward"):
    """Search efficiency - total N / total l

    Citation
    --------
    Viswanathan, G. M. et al. Optimizing the success of random searches. Nature 401, 911–914 (1999).
    """

    # Fmt
    rewards = exp_data[target_name]
    lengths = exp_data[length_name]

    # Short circuit of no targets seen
    if np.isclose(np.sum(rewards), 0.0):
        return 0.0

    total_l = 0
    total_N = 0
    for r, l in zip(rewards, lengths):
        # Not a target!
        if np.isclose(r, 0.0):
            total_l += l
        # Target!
        else:
            # log l and steps
            total_l += l
            total_N += 1

    return total_N / total_l


def turn_ratio(exp_data, length_name="agent_l", angle_name="agent_angle"):
    """Ratio of l / angle"""
    l = np.asarray(exp_data[length_name])
    angle = np.asarray(exp_data[angle_name])
    return np.mean(l / angle)
