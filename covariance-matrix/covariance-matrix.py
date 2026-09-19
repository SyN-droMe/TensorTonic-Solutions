import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    x = np.asarray(X, dtype=float)
    centered = x - np.mean(x, axis=0)
    return centered.T @ centered / (x.shape[0] - 1)