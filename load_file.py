import pickle


def load_pickle(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data
