from sklearn.model_selection import train_test_split
import numpy as np

from neural_network.opts import activation
from neural_network.backprop import bp
from neural_network.model import Network
from neural_network.plot import loss_history_plt, save_plt


def init(X: np.array, hidden_size: int) -> dict:
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
        args,
) -> None:
    wb = init(X, args["hidden_size"])
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=8675309
    )

    # once we have these results we should test it against
    # the y_test data
    results, loss_history = bp(X_train, y_train, wb, args)
    final = results[args["epochs"] - 1]
    func = activation[args["activation_func"]]["main"]

    # initialize our final network
    fm = Network(final_wb=final, activation_func=func)

    # predict the x test data and compare it to y test data
    pred = fm.predict(X_test)
    mse = np.mean((pred - y_test) ** 2)
    print(f"mean squared error: {mse}")

    # plot predicted versus actual
    # also plot the training loss over epochs
    animated_loss_plt = loss_history_plt(loss_history)
    save_plt(animated_loss_plt, "plt.svg", animated=True, fps=30)
