from Models.trends import HarmonicTrend
from Modules import calculator
from Modules.Analysis import correlation
from UI import ui_controller


def action():
    trend = HarmonicTrend(N=1000, dt=0.001, A=10, f=3)
    data = calculator.calculate_harmonic_trend(trend)
    ui_controller.lt_panel.plot_graph(data.xs, data.ys, 'Harmonic Signal')

    trend = HarmonicTrend(N=1000, dt=0.001, A=10, f=503)
    data2 = calculator.calculate_harmonic_trend(trend)
    ui_controller.lb_panel.plot_graph(data2.xs, data2.ys, 'Harmonic Signal 2')

    poly_data = calculator.calculate_polyharmonic_trend((
        HarmonicTrend(N=1000, dt=0.001, A=10, f=3),
        HarmonicTrend(N=1000, dt=0.001, A=100, f=37),
        HarmonicTrend(N=1000, dt=0.001, A=15, f=173)))
    ui_controller.rt_panel.plot_graph(poly_data.xs, poly_data.ys, 'Polyharmonic Signal')

    autocovariation = correlation.autocovariation(data, poly_data)
    ui_controller.rb_panel.plot_graph(autocovariation.xs, autocovariation.ys, 'Автоковариация (Harm/Polyharm)')