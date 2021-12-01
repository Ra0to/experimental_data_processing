from Models.trends import HarmonicTrend
from Modules import calculator, tools
from UI import ui_controller


def action():
    trend = HarmonicTrend(N=1000, dt=0.001, A=10, f=3)
    data = calculator.calculate_harmonic_trend(trend)
    ui_controller.lt_panel.plot_graph(data.xs, data.ys, 'Harmonic Signal')

    new_data = tools.shift(data, 10)
    ui_controller.rt_panel.plot_graph(new_data.xs, new_data.ys, 'Shifted')

    trend2 = HarmonicTrend(N=1000, dt=0.001, A=10, f=3)
    data2 = calculator.calculate_harmonic_trend(trend2)
    ui_controller.lb_panel.plot_graph(data2.xs, data2.ys, 'Harmonic Signal')

    new_data2 = tools.spikes(data2, 5, 500, 200)
    ui_controller.rb_panel.plot_graph(new_data2.xs, new_data2.ys, 'Spiked')

