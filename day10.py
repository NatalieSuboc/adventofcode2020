import numpy as np

def find_jolt_diff(file):
    with open(file) as txt:
        vals = txt.read().split('\n')
        vals = sorted([int(val) for val in vals])
        difs = list(np.diff(np.array(vals)))
        return (difs.count(1) + 1) * (difs.count(3) + 1)
