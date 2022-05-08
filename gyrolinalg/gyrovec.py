from __future__ import annotations

import numpy as np
import numpy.linalg as LA

from gyrolinalg.constant import *

class GyroVec:
    def __init__(self, array: np.ndarray) -> None:
        self.array = array
        assert self._check_on_disk()

    def _check_on_disk(self) -> bool:
        return len(self.array) == N_DIM and C * LA.norm(self.array) < 1

    @staticmethod
    def zero():
        return GyroVec(np.zeros(N_DIM,))

    def __add__(self, other: GyroVec):
        x2 = LA.norm(self.array)**2
        y2 = LA.norm(other.array)**2
        xy = self.array @ other.array

        num = (1 + 2*C*xy + C*y2) * self.array + (1 - C*x2) * other.array
        denom = 1 + 2*C*xy + (C**2)*x2*y2

        return GyroVec(num / denom)

    def __sub__(self, other: GyroVec):
        return self + GyroVec(- other.array)

    def __mul__(self, other: float):
        coef = 1 / np.sqrt(C) * np.tanh(other * np.arctanh(np.sqrt(C)* LA.norm(self.array)))
        array = self.array / LA.norm(self.array)
        return GyroVec(coef * array)

    def __rmul__(self, other: float):
        return self * other

    def __truediv__(self, other: float):
        return self * (1 / other)

    def __neg__(self):
        return GyroVec(-1. * self.array)

    def __repr__(self):
        return self.array.__repr__()