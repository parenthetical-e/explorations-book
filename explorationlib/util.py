import cloudpickle
import numpy as np

from collections import defaultdict


def save(log, filename='checkpoint.pkl'):
    data = cloudpickle.dumps(log)
    with open(filename, 'wb') as fi:
        fi.write(data)


def load(filename='checkpoint.pkl'):
    with open(filename, 'rb') as fi:
        return cloudpickle.load(fi)


def select_exp(exp_data, n, var_name="experiment"):
    """Select all data for a single experiment `n`"""

    # Get index for n
    mask = np.asarray(exp_data[var_name]) == n
    mask = mask.tolist()

    selected = defaultdict(list)
    for k in exp_data.keys():
        for i, m in enumerate(mask):
            if m:
                selected[k].append(exp_data[k][i])

    return selected
