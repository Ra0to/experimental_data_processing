import datetime
import math
import random
import time
from ctypes import Union, c_uint64, c_float

from Models.trends import *


def calculate_linear_trend(trend: LinearTrendData) -> tuple[float]:
    return tuple(trend.a * i + trend.b for i in range(trend.N))


def calculate_exp_trend(trend: ExpTrendData) -> tuple[float]:
    return tuple(trend.b * math.exp(-trend.a * i) for i in range(trend.N))


def calculate_random_trend(n: int, min_: float, max_: float) -> tuple[float]:
    return tuple(random.uniform(min_, max_) for _ in range(n))


class IntFloatUnion(Union):
    _fields_ = ('int', c_uint64), ('float', c_float)


def custom_random(min_: float, max_: float) -> float:
    # date = datetime.datetime.now()
    #
    # tp = IntFloatUnion()
    # x = time.perf_counter_ns()
    # tp.int = int(x % 10000000 / 100)
    # print(f'{x} {int(x % 100000 / 100)} {tp.int} {tp.float}')
    return (math.sin(1/13 * int(str(time.perf_counter_ns())[-5:-1])) + 1) / 2 * (max_ - min_) + min_
    # return tp.float


def calculate_custom_random_trend(n: int, min_: float, max_: float) -> tuple[float]:
    return tuple(custom_random(min_, max_) for _ in range(n))
