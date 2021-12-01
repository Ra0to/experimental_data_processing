import math

import numpy as np

from Models.plots import PlotData
from Models.trends import HarmonicTrend, ExpTrendData, LinearTrendData
from Modules import calculator, tools
from Modules.Analysis import stats
from Modules.IO_System.Readers import trend_reader
from UI import ui_controller

N = 1000
M = 200
dt = 0.001
harm = calculator.calculate_harmonic_trend(HarmonicTrend(N=N, dt=dt, A=10, f=3))
poly_data = calculator.calculate_polyharmonic_trend((
    HarmonicTrend(N=N, dt=dt, A=10, f=3),
    HarmonicTrend(N=N, dt=dt, A=100, f=37),
    HarmonicTrend(N=N, dt=dt, A=15, f=173)))
const_data = calculator.calculate_linear_trend(LinearTrendData(N=N, a=0, b=10))
const_wide_data = PlotData(xs=const_data.xs, ys=tuple(float(const_data.ys[i] if i < (0.8 * N) else 0) for i in range(len(const_data))))
const_narrow_data = PlotData(xs=const_data.xs, ys=tuple(float(const_data.ys[i] if i < (0.2 * N) else 0) for i in range(len(const_data))))

polyharm_wide_data = PlotData(xs=const_data.xs, ys=tuple(float(poly_data.ys[i] if i < (0.6 * N) else 0) for i in range(len(poly_data))))
random_data = calculator.calculate_random_trend(n=N, min_=-10, max_=10)
custom_random_data = calculator.calculate_custom_random_trend(n=N, min_=-10, max_=10)

linear_data = calculator.calculate_linear_trend(LinearTrendData(N=N, a=1, b=10))
exp_data = calculator.calculate_exp_trend(ExpTrendData(N=N, a=-0.005, b=5))
spike_data = tools.spikes(calculator.calculate_linear_trend(LinearTrendData(N=N, a=0, b=0)), 1, 1000, 100)


def action():
    lin_trend = calculator.calculate_linear_trend(LinearTrendData(N=N, a=0, b=0))
    inp = list(lin_trend.ys)
    inp[200] = 120
    inp[400] = 130
    inp[600] = 110
    data = PlotData(lin_trend.xs, inp)


    # h = calculator.calculate_harmonic_trend(HarmonicTrend(N=100, dt=0.01,  A=10, f=3))
    dt = 0.005
    h_xs = np.arange(0, M * dt, dt)
    f = 4
    a = 10
    h_ys = (math.sin(2 * math.pi * f * t) * math.exp(-a * t) for t in h_xs)
    h = PlotData(tuple(h_xs), tuple(h_ys))

    svertka = tools.convolution(data, h)

    ui_controller.lt_panel.plot_graph(data.xs, data.ys, 'Rythm')
    ui_controller.rt_panel.plot_graph(h.xs, h.ys, 'H')
    ui_controller.lb_panel.plot_graph(svertka.xs, svertka.ys)
