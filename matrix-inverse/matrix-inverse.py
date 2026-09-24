import numpy as np

def matrix_inverse(A: list) -> np.ndarray | None:
    """
    Returns the inverse as a NumPy array, or None.
    """
    m = np.asarray(A, dtype=float)
    size = m.shape[0]
    aug = np.concatenate((m.copy(), np.eye(size)), axis=1)

    for c in range(size):
        pivot = c + np.argmax(np.abs(aug[c:, c]))
        if abs(aug[pivot, c]) < 1e-12:
            return None
            
        aug[[c, pivot]] = aug[[pivot, c]]
        aug[c] /= aug[c,c]

        for row in range(size):
            if row != c:
                aug[row] -= aug[row,c] * aug[c]

    return aug[:, size:]