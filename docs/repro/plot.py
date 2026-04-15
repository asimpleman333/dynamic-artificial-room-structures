import numpy as np
import matplotlib.pyplot as plt

from main import step

if __name__ == "__main__":
    # set X: random points in R^2
    X = np.random.randn(20, 2)

    # initial state
    x = np.array([0.0, 0.0])

    trajectory = [x.copy()]

    # iterate dynamics
    for t in range(50):
        x = step(x, X)
        trajectory.append(x.copy())

    trajectory = np.array(trajectory)

    # plot
    plt.figure(figsize=(5, 5))
    plt.scatter(X[:, 0], X[:, 1], s=20, label="X")
    plt.plot(trajectory[:, 0], trajectory[:, 1], "-o", markersize=3, label="trajectory")
    plt.axis("equal")
    plt.legend()
    plt.tight_layout()
    plt.show()
