from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.ones(shape=shape, dtype="float32")
    res[:, int(shape[1]/2):] = -1.0
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    res = np.ones(shape=shape, dtype="float32")
    res[:, :int(shape[1]/2)] = -1.0
    return res
