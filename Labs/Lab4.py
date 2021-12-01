from Modules import calculator
from Modules.Analysis import correlation
from UI import ui_controller

n = 1000
m = 20
s = 5


def density_function():
    random_data = calculator.calculate_random_trend(n, -s, s)
    ui_controller.lt_panel.plot_graph(random_data.xs, random_data.ys, 'Standard Random')
    ui_controller.lb_panel.plot_hist(random_data.ys, m, (-s, s), 'Плотность вероятности (Standard Random)')

    custom_random_data = calculator.calculate_custom_random_trend(n, -s, s)
    ui_controller.rt_panel.plot_graph(custom_random_data.xs, custom_random_data.ys, 'Custom Random')
    ui_controller.rb_panel.plot_hist(custom_random_data.ys, m, (-s, s), 'Плотность вероятности (Custom Random)')


def autocorrelation():
    random_data = calculator.calculate_random_trend(n, -s, s)
    ui_controller.lt_panel.plot_graph(random_data.xs, random_data.ys, 'Standard Random')

    random_autocorrelation = correlation.autocorrelation(random_data)
    ui_controller.lb_panel.plot_graph(random_autocorrelation.xs, random_autocorrelation.ys, 'Автокорреляция (Standard Random)')

    custom_random_data = calculator.calculate_custom_random_trend(n, -s, s)
    ui_controller.rt_panel.plot_graph(custom_random_data.xs, custom_random_data.ys, 'Custom Random')

    custom_random_autocorrelation = correlation.autocorrelation(custom_random_data)
    ui_controller.rb_panel.plot_graph(custom_random_autocorrelation.xs, custom_random_autocorrelation.ys, 'Автокорреляция (Custom Random)')


def autocovariation():
    random_data = calculator.calculate_random_trend(n, -s, s)
    ui_controller.lt_panel.plot_graph(random_data.xs, random_data.ys, 'Standard Random')

    custom_random_data = calculator.calculate_custom_random_trend(n, -s, s)
    ui_controller.rt_panel.plot_graph(custom_random_data.xs, custom_random_data.ys, 'Custom Random')

    autocovariation = correlation.autocovariation(random_data, custom_random_data)
    ui_controller.lb_panel.plot_graph(autocovariation.xs, autocovariation.ys, 'Автоковариация (Standard/Custom)')

    ui_controller.rb_panel.clear_graph()
