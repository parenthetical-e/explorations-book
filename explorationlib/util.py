import cloudpickle


def save(log, filename='checkpoint.pkl'):
    data = cloudpickle.dumps(log)
    with open(filename, 'wb') as fi:
        fi.write(data)


def load(filename='checkpoint.pkl'):
    with open(filename, 'rb') as fi:
        return cloudpickle.load(fi)