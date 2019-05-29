import numpy as np

class DummyPredictor:
    def predict(self, X):
        n = X.shape[0]
        np.random.seed(123456)
        idx = np.random.choice(n)
        result = np.zeros(n, dtype=np.int)
        result[idx] = 1
        return result
