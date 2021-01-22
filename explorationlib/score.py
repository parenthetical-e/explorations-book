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
    """Search efficiency"""
    # mean_l = np.mean(exp_data[length_name])
    # N = np.sum(exp_data[target_name])
    # return 1 / (mean_l * N)

    # Fmt
    rewards = exp_data[target_name]
    lengths = exp_data[length_name]

    # Short circuit of no targets seen
    if np.isclose(np.sum(rewards), 0.0):
        return 0.0

    total_l = 0
    total_step = 1
    total_N = 0
    ls = []
    for r, l in zip(rewards, lengths):
        if np.isclose(r, 0.0):
            # Not a target!
            # log: l and steps
            total_l += l
            total_step += 1
        else:
            # Target!
            total_N += 1
            ls.append(total_l / total_step)
            # Reset
            total_step = 1
            total_l = 0

    return 1 / (np.mean(ls) * total_N)


def turn_ratio(exp_data, length_name="agent_l", angle_name="agent_angle"):
    """Ratio of l / angle"""
    l = np.asarray(exp_data[length_name])
    angle = np.asarray(exp_data[angle_name])
    return np.mean(l / angle)
