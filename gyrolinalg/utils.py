import numpy as np
import numpy.linalg as LA 

from gyrolinalg import GyroVec
from gyrolinalg.constant import *


def norm(v: GyroVec) -> float:
    return LA.norm(v.array)

def inner(x, a: np.ndarray, b: np.ndarray):
    g = g_euclid * (lam(x))**2
    return a @ g @ b

def dist(v: GyroVec, w: GyroVec) -> float:
    arr = norm(- v + w)
    return 2 / np.sqrt(C) * np.arctanh(np.sqrt(C) * arr)

def lam(x: GyroVec) -> float:
    return 2 / (1 - C * norm(x)**2)

def exp(x: GyroVec, v: np.ndarray):
    right = v / (np.sqrt(C) * LA.norm(v))
    right = np.tanh(lam(x) * np.sqrt(C) * LA.norm(v) / 2) * right

    return x + GyroVec(right)

def log(x: GyroVec, v: GyroVec):
    arr = - x + v
    nm = norm(arr)
    return (dist(x, v) / lam(x) * arr / nm).array
