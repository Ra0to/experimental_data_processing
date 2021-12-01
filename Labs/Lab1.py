from Modules.IO_System.Readers import trend_reader
from Modules import calculator
from UI import ui_controller

# Необходимо построить 4 графика, 2 линейных тренда, 2 экспоненциальных тренда (возрастающий и убывающий)
def action():
    linear_trend_file1 = r'S:/TEMP/DataAnalyze/LinearTrend1.txt'
    linear_trend_file2 = r'S:/TEMP/DataAnalyze/LinearTrend2.txt'
    exp_trend_file1 = r'S:/TEMP/DataAnalyze/ExpTrend1.txt'
    exp_trend_file2 = r'S:/TEMP/DataAnalyze/ExpTrend2.txt'

    linear_trend1 = trend_reader.read_linear_trend_data(linear_trend_file1)
    linear_values1 = calculator.calculate_linear_trend(linear_trend1)

    linear_trend2 = trend_reader.read_linear_trend_data(linear_trend_file2)
    linear_values2 = calculator.calculate_linear_trend(linear_trend2)

    exp_trend1 = trend_reader.read_exp_trend_data(exp_trend_file1)
    exp_values1 = calculator.calculate_exp_trend(exp_trend1)

    exp_trend2 = trend_reader.read_exp_trend_data(exp_trend_file2)
    exp_values2 = calculator.calculate_exp_trend(exp_trend2)

    ui_controller.lt_panel.plot_graph(linear_values1.xs, linear_values1.ys, 'Linear Trend 1')
    ui_controller.rt_panel.plot_graph(linear_values2.xs, linear_values2.ys, 'Linear Trend 2')
    ui_controller.lb_panel.plot_graph(exp_values1.xs, exp_values1.ys, 'Exp Trend 1')
    ui_controller.rb_panel.plot_graph(exp_values2.xs, exp_values2.ys, 'Exp Trend 2')
