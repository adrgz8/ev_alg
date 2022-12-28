import numpy as np


def one_max(pop, length=None, N=None):
    sums = np.sum(pop, axis=-1)
    loc_max = np.argmax(sums)
    val_max = np.max(sums)
    return loc_max, val_max


def dec_one_max(pop, length, N=None):
    sums = np.sum(pop, axis=-1)
    loc_max = np.argmax(sums)
    val_max = np.max(sums)
    loc_min = np.argmin(sums)
    val_min = np.min(sums)
    if val_min == 0:
        return loc_min, length + 1
    return loc_max, val_max


def k_dec_one_max(pop, length, N, k=5):
    sums_split = [np.sum(np.split(pop[i], k), axis=-1) for i in range(N)]
    sums = []
    for i in range(N):
        if 0 not in sums_split[i]:
            sums.append(np.sum(sums_split[i]))
        else:
            sums.append(np.sum(sums_split[i]) + k)
    sums = np.array(sums)
    loc_max = np.argmax(sums)
    val_max = np.max(sums)
    return loc_max, val_max
