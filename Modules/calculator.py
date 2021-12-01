import math
import random
import time
from typing import Sequence

import numpy as np

from Models.plots import PlotData
from Models.trends import *


def calculate_linear_trend(trend: LinearTrendData) -> PlotData:
    xs = tuple(np.arange(trend.N))
    return PlotData(xs=xs, ys=tuple(trend.a * float(i) + trend.b for i in xs))


def calculate_exp_trend(trend: ExpTrendData) -> PlotData:
    xs = tuple(np.arange(trend.N))
    return PlotData(xs=xs, ys=tuple(trend.b * math.exp(-trend.a * i) for i in range(trend.N)))


def calculate_random_trend(n: int, min_: float, max_: float) -> PlotData:
    xs = tuple(np.arange(n))
    return PlotData(xs=xs, ys=tuple(random.uniform(min_, max_) for _ in range(n)))


def custom_random(min_: float, max_: float) -> float:
    return (math.sin(1 / 13 * int(str(time.perf_counter_ns())[-5:-1])) + 1) / 2 * (max_ - min_) + min_


def calculate_custom_random_trend(n: int, min_: float, max_: float) -> PlotData:
    xs = tuple(np.arange(n))
    return PlotData(xs=xs, ys=tuple(custom_random(min_, max_) for _ in range(n)))


def calculate_harmonic_trend(trend: HarmonicTrend) -> PlotData:
    xs = []
    ys = []
    for i in range(trend.N):
        value = trend.A * math.sin(2 * math.pi * trend.f * i * trend.dt)

        xs.append(i * trend.dt)
        ys.append(value)

    return PlotData(xs=tuple(xs), ys=tuple(ys))


def calculate_polyharmonic_trend(trends: Sequence[HarmonicTrend]) -> PlotData:
    xs = []
    ys = []
    graphs = []
    for trend in trends:
        data = calculate_harmonic_trend(trend)
        xs = data.xs
        graphs.append(data)

    for i in range(len(xs)):
        sum_ = 0.0
        for plot in graphs:
            sum_ += plot.ys[i]
        ys.append(sum_)

    return PlotData(xs=tuple(xs), ys=tuple(ys))
