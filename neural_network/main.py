import numpy as np

from neural_network.forwardprop import fp


def init(X: np.array, y: np.array, hidden_size: int) -> dict:
    """
    returns a dictionary containing randomly initialized
    weights and biases to start off the neural_network
    """
    return {
        "W1": np.random.randn(X.shape[1], hidden_size),
        "b1": np.zeros((1, hidden_size)),
        "W2": np.random.randn(hidden_size, 1),
        "b2": np.zeros((1, 1)),
    }


def main(
    X: np.array, 
    y: np.array, 
    epochs: int, 
    hidden_size: int, 
    learning_rate: float,
    activation_func: str,
) -> None:
    wb = init(X, y, hidden_size) 

    for e in range(epochs):

        fp()
        bp()

        # update weights and biases

