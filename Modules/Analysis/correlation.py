import numpy as np

from Models.plots import PlotData
from Modules.Analysis import stats


def autocorrelation(data: PlotData) -> PlotData:
    xs = []
    ys = []
    mean = stats.expected_value(data.ys)

    denominator = sum([(y - mean) ** 2 for y in data.ys])

    for l in range(len(data.xs)):
        sum_ = 0
        for i in range(len(data.xs) - l):
            sum_ += (data.ys[i] - mean) * (data.ys[i + l] - mean)
        xs.append(l)
        ys.append(sum_ / denominator)

    return PlotData(tuple(xs), tuple(ys))


def autocovariation(first: PlotData, second: PlotData) -> PlotData:
    assert len(first.xs) == len(second.xs), 'Plots should be same size'
    xs = []
    ys = []

    first_mean = stats.expected_value(first.ys)
    second_mean = stats.expected_value(second.ys)

    n = len(first.xs)

    for l in range(n):
        sum_ = 0
        for i in range(n - l):
            sum_ += (first.ys[i] - first_mean) * (second.ys[i + l] - second_mean)

        xs.append(l)
        ys.append(sum_ / n)

    return PlotData(tuple(xs), tuple(ys))
