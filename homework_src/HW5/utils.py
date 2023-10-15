import pickle


def load_bin(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load_bin('dv.bin')
model = load_bin('model1.bin')
