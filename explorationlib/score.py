import numpy as np
from scipy import stats


def reward_summary(exp_data, var_name="reward"):
    return stats.describe(exp_data[var_name])
