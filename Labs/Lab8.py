import numpy as np

from Models.plots import PlotData
from Models.trends import HarmonicTrend, ExpTrendData, LinearTrendData
from Modules import calculator, tools
from Modules.Analysis import stats
from UI import ui_controller

N = 1000
a = -0.005
b = 5
min_ = -50
max_ = 50

trendData = ExpTrendData(N=N, a=a, b=b)
trend = calculator.calculate_exp_trend(trendData)
noise = calculator.calculate_random_trend(n=N, min_=min_, max_=max_)

data = PlotData(tuple(np.arange(N)), tuple(trend.ys[i] + noise.ys[i] for i in range(N)))


def action():
    ui_controller.lt_panel.plot_graph(np.arange(N), trend.ys, 'Trend')
    ui_controller.lb_panel.plot_graph(np.arange(N), noise.ys, 'Noise')
    ui_controller.rt_panel.plot_graph(np.arange(N), data.ys, 'Input')

    fixed_data = tools.antiTrend(data)
    ui_controller.rb_panel.plot_graph(fixed_data.xs, fixed_data.ys, 'Anti Trend')


def showTrend():
    ui_controller.lt_panel.plot_graph(np.arange(N), trend.ys, 'Trend')
    ui_controller.lb_panel.plot_graph(np.arange(N), noise.ys, 'Noise')
    ui_controller.rt_panel.plot_graph(np.arange(N), data.ys, 'Input')

    fixed_data = tools.antiTrend(data, remove_noise=True)
    ui_controller.rb_panel.plot_graph(fixed_data.xs, fixed_data.ys, 'Anti Noise')


def sum_mean_method():
    def rand_trend() -> PlotData:
        return calculator.calculate_random_trend(N, 2 * min_, 2 * max_)

    M = 10000

    rand = rand_trend()
    ui_controller.lt_panel.plot_graph(rand.xs, rand.ys, 'First Random')

    xs = []
    ys = []
    sigma_1 = stats.dispersion(rand.ys)
    # xs.append(0)
    # ys.append(sigma_1 / sigma_1)

    for iter in range(1, M):
        new_rand = rand_trend()
        rand.ys = tuple(new_rand.ys[i] + rand.ys[i] for i in range(N))

        if iter % 10 == 0:
            xs.append(iter)
            ys.append(stats.dispersion(tuple(x / iter for x in rand.ys)) / sigma_1)

    rand.ys = tuple(rand.ys[i] / M for i in range(N))
    ui_controller.rt_panel.plot_graph(rand.xs, rand.ys, f'{M} Random')
    ui_controller.lb_panel.plot_graph(xs, ys, 'Dispersion correlation')


def sum_remove_noise():
    trend = HarmonicTrend(N=N, dt=0.001, A=10, f=3)
    harm = calculator.calculate_harmonic_trend(trend)

    def rand_trend() -> PlotData:
        noise = calculator.calculate_random_trend(N, 2 * min_, 2 * max_)
        return PlotData(noise.xs, tuple(harm.ys[i] + noise.ys[i] for i in range(N)))

    M = 10005

    rand = rand_trend()
    ui_controller.lt_panel.plot_graph(rand.xs, rand.ys, 'Iteration 1 (Input)')

    for iter in range(1, M):
        new_rand = rand_trend()
        rand.ys = tuple(new_rand.ys[i] + rand.ys[i] for i in range(N))

        if iter == 10:
            ui_controller.rt_panel.plot_graph(rand.xs, tuple(rand.ys[i] / iter for i in range(N)), f'Iteration {iter}')

        if iter == 100:
            ui_controller.lb_panel.plot_graph(rand.xs, tuple(rand.ys[i] / iter for i in range(N)), f'Iteration {iter}')

        if iter == 10000:
            ui_controller.rb_panel.plot_graph(rand.xs, tuple(rand.ys[i] / iter for i in range(N)), f'Iteration {iter}')