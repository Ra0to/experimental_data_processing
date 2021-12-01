import math
import random

import numpy as np

from Models.plots import PlotData
from Modules.Analysis import stats


def shift(data: PlotData, value: float) -> PlotData:
    new_data = PlotData(data.xs, data.ys)
    new_data.ys = [y + value for y in data.ys]
    return new_data


def spikes(data: PlotData, count: int, value: float, d: float) -> PlotData:
    (min_, max_) = (value - d, value + d)
    positions = random.sample(range(len(data.xs)), count)
    values = [(1 if random.random() > 0.5 else -1) * random.uniform(min_, max_) for _ in range(count)]

    ys = list(data.ys)

    for i in range(count):
        pos = positions[i]
        val = values[i]
        ys[pos] = val

    return PlotData(data.xs, tuple(ys))


def antishift(data: PlotData) -> PlotData:
    mean = stats.expected_value(data.ys)
    return shift(data, -mean)


def antispike(data: PlotData, range_) -> PlotData:
    (min_, max_) = range_
    n = len(data)
    ys = []

    for i in range(n):
        elem = data.ys[i]

        if elem < min_ or elem > max_:
            if i == 0:
                ys.append(data.ys[i + 1])
                continue
            if i == n - 1:
                ys.append(data.ys[i - 1])
                continue

            ys.append((data.ys[i - 1] + data.ys[i + 1]) / 2)
        else:
            ys.append(elem)

    return PlotData(data.xs, tuple(ys))


def antiTrend(data: PlotData, remove_noise: bool = False) -> PlotData:
    n = len(data)
    l = int(n / 100)
    dt = data.xs[1] - data.xs[0]
    xs = []
    ys = []

    for m in range(0, n - l, dt):
        mean = stats.expected_value(data.ys[m: m + l])
        xs.append(m)
        ys.append(data.ys[m] - mean if not remove_noise else mean)

    return PlotData(xs, ys)


# Амплитудный спектр Фурье |X_n|
def amplitude_spectre_fourier(data: PlotData, dt: float) -> PlotData:
    N = len(data)

    # Частота дискретизации
    # fd = 1 / dt
    df = 1 / (N * dt)

    xs = []
    ys = []

    for n in range(int(N/2)):
        xs.append(df * n)
        re = 0
        im = 0
        for k in range(N):
            re += data.ys[k] * math.cos(2 * math.pi * k * n / N) / N
            im += data.ys[k] * math.sin(2 * math.pi * k * n / N) / N
        ys.append(math.sqrt(re ** 2 + im ** 2))

    return PlotData(xs, ys)


def phase_spectre_fourier(data:PlotData, dt: float) -> PlotData:
    N = len(data)

    # Частота дискретизации
    # fd = 1 / dt
    df = 1 / (N * dt)

    xs = []
    ys = []

    for n in range(int(N / 2)):
        xs.append(df * n)
        re = 0
        im = 0
        for k in range(N):
            re += data.ys[k] * math.cos(2 * math.pi * k * n / N) / N
            im += data.ys[k] * math.sin(2 * math.pi * k * n / N) / N
        ys.append(math.atan(im/re))

    return PlotData(xs, ys)

# Фазовый спектр Фурье arctg(im_n/re_n) \phi_n
# Спектр мощности Фурье Re_n^2 + Im_n^2 = |X_n|^2
# Теорема Винера-Хинчина |X_n|^2 = |F[R_{xx}]|


def convolution(data: PlotData, h: PlotData) -> PlotData:
    n = len(data)
    m = len(h)
    shift = int(m / 2)

    x = []
    y = []
    for k in range(shift, n + shift):
        x.append(k)
        yk = 0
        for j in range(m):
            # if (k - j) < 0:
            #     break
            # if (k - j) >= n:
            #     continue
            # yk += data.ys[k-j] * h.ys[j]
            yk += data.ys[(k-j) % n] * h.ys[j]
        y.append(yk)

    return PlotData(tuple(x), tuple(y))


def lpw(fc, dt, m) -> PlotData:
    d = [0.35577019, 0.2436983, 0.07211497, 0.00630165]
    fact = 2 * fc * dt
    lpw = [fact]
    arg = fact * math.pi
    for i in range(1, m + 1):
        lpw.append(math.sin(arg * i) / (i * math.pi))

    lpw[m] /= 2

    sumg = lpw[0]
    for i in range(1, m + 1):
        sum = d[0]
        arg = math.pi * i / m
        for k in range(1, 4):
            sum += 2 * d[k] * math.cos(arg * k)
        lpw[i] *= sum
        sumg += 2 * lpw[i]

    for i in range(len(lpw)):
        lpw[i] /= sumg

    return PlotData(np.arange(0, dt * (m + 1), dt), lpw)


def lpf(fc, dt, m) -> PlotData:
    w = lpw(fc, dt, m)
    ys = w.ys[:0:-1]
    ys += w.ys
    xs = np.arange(0, (2 * m + 1) * dt, dt)
    return PlotData(xs, ys)


def hpw(fc, dt, m) -> PlotData:
    return hpf(lpf(fc, dt, m))


def hpf(lpw: PlotData) -> PlotData:
    m = (len(lpw) - 1) // 2
    ys = []

    for i in range(len(lpw.ys)):
        if i == m:
            ys.append(1 - lpw.ys[i])
        else:
            ys.append(-lpw.ys[i])

    return PlotData(lpw.xs, ys)


def bpf(fc1, fc2, dt, m) -> PlotData:
    assert fc1 < fc2

    lpf1 = lpf(fc1, dt, m)
    lpf2 = lpf(fc2, dt, m)

    bpw = []

    for i in range(len(lpf1)):
        bpw.append(lpf2.ys[i] - lpf1.ys[i])

    return PlotData(lpf1.xs, bpw)


def bsf(fc1, fc2, dt, m) -> PlotData:
    return hpf(bpf(fc1, fc2, dt, m))
