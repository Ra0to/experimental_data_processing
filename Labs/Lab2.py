import numpy as np

from Modules import calculator
from Modules.IO_System.Readers import trend_reader
from UI import ui_controller


linear_trend_file1 = r'S:/TEMP/DataAnalyze/LinearTrend1.txt'
linear_trend_file2 = r'S:/TEMP/DataAnalyze/LinearTrend2.txt'

linear_trend1 = trend_reader.read_linear_trend_data(linear_trend_file1)
linear_values1 = calculator.calculate_linear_trend(linear_trend1)

linear_trend2 = trend_reader.read_linear_trend_data(linear_trend_file2)
linear_values2 = calculator.calculate_linear_trend(linear_trend2)


def action():
    ui_controller.lt_panel.plot_graph(linear_values1.xs, linear_values1.ys, 'Linear trend 1')
    ui_controller.rt_panel.plot_graph(linear_values2.xs, linear_values2.ys, 'Linear trend 2')
    random_values1 = calculator.calculate_random_trend(len(linear_values1.xs), -5, 5)
    random_values2 = calculator.calculate_random_trend(len(linear_values2.xs), -5, 5)
    noise_values1 = tuple(map(lambda x, y: x + y, linear_values1.ys, random_values1.ys))
    noise_values2 = tuple(map(lambda x, y: x * y, linear_values2.ys, random_values2.ys))

    ui_controller.lb_panel.plot_graph(np.arange(len(noise_values1)), noise_values1, 'Addictive noise')
    ui_controller.rb_panel.plot_graph(np.arange(len(noise_values2)), noise_values2, 'Multiplicative noise')


def action_custom_random():
    ui_controller.lt_panel.plot_graph(linear_values1.xs, linear_values1.ys, 'Linear trend 1')
    ui_controller.rt_panel.plot_graph(linear_values2.xs, linear_values2.ys, 'Linear trend 2')
    random_values1 = calculator.calculate_custom_random_trend(len(linear_values1.xs), -5, 5)
    random_values2 = calculator.calculate_custom_random_trend(len(linear_values2.xs), -5, 5)
    noise_values1 = tuple(map(lambda x, y: x + y, linear_values1.ys, random_values1.ys))
    noise_values2 = tuple(map(lambda x, y: x * y, linear_values2.ys, random_values2.ys))

    ui_controller.lb_panel.plot_graph(np.arange(len(noise_values1)), noise_values1, 'Addictive noise (custom random)')
    ui_controller.rb_panel.plot_graph(np.arange(len(noise_values2)), noise_values2, 'Multiplicative noise (custom random)')


def random_values():
    random_values = calculator.calculate_random_trend(100, -5, 5)
    ui_controller.lt_panel.plot_graph(random_values.xs, random_values.ys, 'Standard random [-5, 5]')

    random_values = calculator.calculate_custom_random_trend(100, -5, 5)
    ui_controller.rt_panel.plot_graph(random_values.xs, random_values.ys, 'Custom random [-5, 5]')

    ui_controller.lb_panel.clear_graph()
    ui_controller.rb_panel.clear_graph()

