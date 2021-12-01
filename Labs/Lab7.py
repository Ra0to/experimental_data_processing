from Models.trends import HarmonicTrend
from Modules import calculator, tools
from Modules.Analysis import stats
from UI import ui_controller


def action():
    shift = 10
    trend = HarmonicTrend(N=1000, dt=0.001, A=10, f=3)
    data = calculator.calculate_harmonic_trend(trend)
    ui_controller.lt_panel.plot_graph(data.xs, data.ys, 'Harmonic Signal')

    shifted_data = tools.shift(data, shift)
    ui_controller.rt_panel.plot_graph(shifted_data.xs, shifted_data.ys, 'Shifted')

    corrected_data = tools.antishift(shifted_data)
    ui_controller.lb_panel.plot_graph(corrected_data.xs, corrected_data.ys, 'Corrected')


def remove_spikes():
    trend = HarmonicTrend(N=1000, dt=0.001, A=10, f=3)
    data = calculator.calculate_harmonic_trend(trend)
    ui_controller.lt_panel.plot_graph(data.xs, data.ys, 'Harmonic Signal')

    spiked_data = tools.spikes(data, 10, 500, 200)
    ui_controller.rt_panel.plot_graph(spiked_data.xs, spiked_data.ys, 'Spiked')

    corrected_data = tools.antispike(spiked_data, (-trend.A, trend.A))
    ui_controller.lb_panel.plot_graph(corrected_data.xs, corrected_data.ys, 'Corrected')

