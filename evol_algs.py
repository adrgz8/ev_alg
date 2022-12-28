import numpy as np
from numpy.random import binomial, random


def pbil(length, N, lr, mutation, shift, epochs, method, verbose=True):
    """_summary_

    Args:
        length (int): Vector length
        N (int): Number of samples
        lr (float): Learning rate
        mutation (float): Random mutation
        shift (float): For mutation
        epochs (int): Number of epochs to run
        method (func): Optimization problem to solve
        verbose (bool, optional): Show logs or not. Defaults to True.

    Returns:
        _type_: Maximum values found after epochs
    """
    probs = np.full(length, 0.5)
    pops = list()
    max_vals = list()
    for i in range(epochs):
        if verbose:
            if i % 10 == 0:
                print(f'Doing epoch {i}')
                print(probs)
                print('-' * 50)
        pop = [binomial(1, probs, length) for i in range(N)]
        pops.append(pop)
        loc_max, max_val = method(pop, length, N)
        max_vals.append(max_val)
        best_sample = pop[loc_max]
        probs += lr * (best_sample - probs)

        # Mutation
        mutate_prob = random(length) < mutation
        for v in range(length):
            if mutate_prob[v]:
                probs[v] = probs[v] * (1 - shift) + binomial(1, 0.5) * shift
    return max_vals


def umda(length, N, lr, mutation, shift, epochs, method, verbose=True):
    probs = np.full(length, 0.5)
    Ps = list()
    max_vals = list()
    for i in range(epochs):
        if verbose:
            if i % 10 == 0:
                print(f'Doing epoch {i}')
                print(probs)
                print('-' * 50)
        P = [binomial(1, probs, length) for _ in range(N)]
        P_copy = P.copy()
        P_sample = list()
        Ps.append(P)
        idx_sample = list()
        for _ in range(int(N * lr * 2)):
            loc_max, _ = method(P_copy, length, N)
            idx_sample.append(loc_max)
            P_copy.pop(idx_sample[-1])
            P_sample.append(P[loc_max])
        max_vals.append(method(P, length, N)[1])
        probs = np.mean(P_sample, axis=0).tolist()

        # Mutation
        mutate_prob = random(length) < mutation
        for v in range(length):
            if mutate_prob[v]:
                probs[v] = probs[v] * (1 - shift) + binomial(1, 0.5) * shift
    return max_vals


def cga(length, N, lr, mutation, shift, epochs, method, verbose=True):
    Ps = list()
    max_vals = list()
    theta = lr / 2
    probs = np.full(length, 0.5)
    for i in range(epochs):
        if verbose:
            if i % 10 == 0:
                print(f'Doing epoch {i}')
                print(probs)
                print('-' * 50)
        P_1 = binomial(1, probs, length)
        P_2 = binomial(1, probs, length)
        x_1, val_1 = method(P_1, length, N)
        x_2, val_2 = method(P_2, length, N)
        if x_1 >= x_2:
            x_best, x_worst = P_1, P_2
            max_vals.append(val_1)
        else:
            x_best, x_worst = P_2, P_1
            max_vals.append(val_2)
        Ps.append(x_best)
        probs = [probs[j] + theta if (
                x_best[j] != x_worst[j] and x_best[j] == 1
                ) else probs[j] - theta if (
                    x_best[j] != x_worst[j] and x_best[j] == 0
                    ) else probs[j] for j in range(length)]
        # Making sure probs are between 0 and 1
        probs = np.clip(probs, a_min=0.0, a_max=1.0)

        # Mutation
        mutate_prob = random(length) < mutation
        for v in range(length):
            if mutate_prob[v]:
                probs[v] = probs[v] * (1 - shift) + binomial(1, 0.5) * shift
    return max_vals
