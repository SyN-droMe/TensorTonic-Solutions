import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X = np.asarray(X, dtype=float)
    centered = X - np.mean(X, axis=0)
    cov = centered.T @ centered / (X.shape[0] - 1)
    std_dev = np.sqrt(np.diag(cov))
    deno = np.outer(std_dev, std_dev)
    with np.errstate(divide="ignore", invalid="ignore"):
        return cov / deno