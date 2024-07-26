# Numpy-Neuron

A small, simple neural network framework built using only [numpy](https://numpy.org) and python (duh).

## Install

`pip install numpyneuron`


## Example

```py
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import numpy as np
from numpyneuron import (
    NN,
    Relu,
    Sigmoid,
    CrossEntropyWithLogits,
)


RANDOM_SEED = 2


def _preprocess_digits(
    seed: int,
) -> tuple[np.ndarray, ...]:
    digits = datasets.load_digits(as_frame=False)
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    y = OneHotEncoder().fit_transform(digits.target.reshape(-1, 1)).toarray()
    X_train, X_test, y_train, y_test = train_test_split(
        data,
        y,
        test_size=0.2,
        random_state=seed,
    )
    return X_train, X_test, y_train, y_test


def train_nn_classifier() -> None:
    X_train, X_test, y_train, y_test = _preprocess_digits(seed=RANDOM_SEED)

    nn_classifier = NN(
        epochs=2_000,
        hidden_size=16,
        batch_size=1,
        learning_rate=0.01,
        loss_fn=CrossEntropyWithLogits(),
        hidden_activation_fn=Relu(),
        output_activation_fn=Sigmoid(),
        input_size=64,  # 8x8 pixel grid images
        output_size=10,  # digits 0-9
        seed=2,
    )

    nn_classifier.train(
        X_train=X_train,
        y_train=y_train,
    )

    pred = nn_classifier.predict(X_test=X_test)

    pred = np.argmax(pred, axis=1)
    y_test = np.argmax(y_test, axis=1)

    accuracy = accuracy_score(y_true=y_test, y_pred=pred)

    print(f"accuracy on validation set: {accuracy:.4f}")


if __name__ == "__main__":
    train_nn_classifier()
```

## Roadmap

**Optimizers**

Currently the learning rate in a NN object is static during training. I would like 
to work on developing at least the functionality for the Adam optimizer at some point.
This would help prevent getting stuck in local minima of the loss function.
