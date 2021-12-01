import math

import statistics

import numpy as np

from Models.plots import PlotData


def expected_value(arr: tuple[float]) -> float:
    return statistics.mean(arr)


def min_value(arr: tuple[float]) -> float:
    return min(arr)


def max_value(arr: tuple[float]) -> float:
    return max(arr)


def dispersion(arr: tuple[float]) -> float:
    mean = expected_value(arr)
    return statistics.mean([(x - mean) ** 2 for x in arr])


def standard_deviation(arr: tuple[float]) -> float:
    return math.sqrt(dispersion(arr))


def mean_square(arr: tuple[float]) -> float:
    return statistics.mean([x ** 2 for x in arr])


def mean_square_error(arr: tuple[float]) -> float:
    return math.sqrt(mean_square(arr))


def asymmetry(arr: tuple[float]) -> float:
    mean = expected_value(arr)
    return statistics.mean([(x - mean) ** 3 for x in arr])


def asymmetry_coef(arr: tuple[float]) -> float:
    return asymmetry(arr) / (standard_deviation(arr) ** 3)


def excess(arr: tuple[float]) -> float:
    mean = expected_value(arr)
    return statistics.mean([(x - mean) ** 4 for x in arr])


def excess_coef(arr: tuple[float]) -> float:
    return excess(arr) / (standard_deviation(arr) ** 4) - 3


def is_stationary_function(arr: tuple[float], m: int = 10) -> bool:
    i = 0
    epsilon = 10
    parts = list(map(lambda x: tuple(x), np.array_split(arr, m)))

    previous_mo = expected_value(parts[0])
    previous_disp = dispersion(parts[0])

    print(f'{i}) ExpValue: {previous_mo:.5f}; Dispersion:{previous_disp:.5f};')
    i += 1

    for part in parts[1:]:
        current_mo = expected_value(part)
        current_disp = dispersion(part)

        print(f'{i}) ExpValue: {current_mo:.5f}; Dispersion:{current_disp:.5f};')

        expected_value_percent = (previous_mo - current_mo) / previous_mo * 100
        dispersion_percent = (previous_disp - current_disp) / previous_disp * 100
        print(f'{i}%) ExpValue: {expected_value_percent:.5f}; Dispersion:{dispersion_percent:.5f};')
        i += 1

        if abs(expected_value_percent) > epsilon or abs(dispersion_percent) > epsilon:
            return False

        previous_mo = current_mo
        previous_disp = current_disp

    return True

