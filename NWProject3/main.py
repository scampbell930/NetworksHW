import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt


def propaganda(a: np.array, x_init: np.array, lam: np.array, node: int, time_step: int) -> int:
    # Calculate propaganda for node being influenced
    a[node] = [n/2 for n in a[node]]
    a[node][10] = 0.5

    n = a.shape[0]
    iden = np.eye(n)
    x = np.zeros((n, time_step + 1))
    x[:, 0] = x_init

    # Perform time-steps
    for i in range(1, time_step + 1):
        x[:, i] = lam @ a @ x[:, i-1] + (iden - lam) @ x_init

    # Return total of all opinions except that of the fake node
    return sum(x[:len(x)-1, len(x[0])-1])


def simulate_dynamics(time_step: int):
    # List for end opinions
    total_opinion = []

    # Propaganda calculation for each node
    for n in range(10):
        # Initialize adjacency matrix and graph (including fake node)
        A = np.array([[0, 0.9, 0, 0.1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0.2, 0.1, 0.4, 0.3, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0.9, 0, 0.1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                      [0.4, 0, 0, 0.2, 0, 0, 0, 0.4, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0.8, 0, 0.1, 0, 0, 0, 0.1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])

        # Initialize opinions including fake node
        X = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        lam = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0])
        Lam = np.diag(lam)

        p_value = propaganda(A, X, Lam, n, time_step)
        total_opinion.append([n, p_value])
    # Display propaganda for t = 1
    print(tabulate(total_opinion, headers=["Node Influenced", "Total Opinion"]))


if __name__ == '__main__':
    print("Total Opinions after 1 timestep")
    simulate_dynamics(1)
    print("\n\n")
    print("Total Opinions after 1000 timesteps")
    simulate_dynamics(1000)
