import numpy as np

# metric
def d(x, y):
    return np.linalg.norm(x - y)

# interaction kernel
def K(r):
    return np.exp(-r)

# generic structure
def F(x, X):
    return sum(K(d(x, y)) for y in X)

# evolution map
def f(Fx, x):
    return x + 0.1 * (Fx - np.linalg.norm(x))

# one time step
def step(x, X):
    return f(F(x, X), x)

if __name__ == "__main__":
    # set X: random points in R^2
    X = np.random.randn(20, 2)

    # initial state
    x = np.array([0.0, 0.0])

    # iterate dynamics
    for t in range(50):
        x = step(x, X)
        print(t, x)
