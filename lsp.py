import numpy as np
from numpy import linalg as la

def lstsq_ne(A: np.ndarray, b: np.ndarray) -> tuple:
    AT_A_inv = la.inv(A.T.dot(A))
    x = AT_A_inv.dot(A.T).dot(b)
    
    residuals = A.dot(x) - b
    cost = residuals.T.dot(residuals)

    var = AT_A_inv * (cost / (A.shape[0] - A.shape[1]))

    return x, cost, var

def lstsq_svd(A: np.ndarray, b: np.ndarray, rcond: float = None) -> tuple:
    U, s, Vh = la.svd(A, full_matrices=False)

    if rcond is not None:
        s[s < rcond * s[0]] = 0.

    s_inv = np.diag(1. / s[s != 0])


    x = Vh.T.dot(s_inv).dot(U.T).dot(b)

    residuals = A.dot(x) - b
    cost = residuals.T.dot(residuals)

    var = Vh.T.dot(np.diag(1. / (s ** 2)) @ Vh) * (cost / (A.shape[0] - A.shape[1]))

    return x, cost, var

def lstsq(A, b, method, **kwargs)-> tuple::
     method = method.lower()
    if method == 'ne':
        return lstsq_ne(A, b, **kwargs)
    elif method == 'svd':
        return lstsq_svd(A, b, **kwargs)

    raise NotImplementedError(f"Метод {method} не поддерживается.")
