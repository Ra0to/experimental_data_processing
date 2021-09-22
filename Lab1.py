from tkinter import *
import numpy as np

from Modules.IO_System.Readers import trend_reader, raw_data_reader
from Modules import calculator
from UI.MainWindow import MainWindow
from UI.Panels.GraphPanel import GraphPanel, ButtonPanel


def graphs():
    root = Tk()
    main_window = MainWindow(root)

    file = r'S:/TEMP/DataAnalyze/1.txt'
    linearTrendFile1 = r'S:/TEMP/DataAnalyze/LinearTrend1.txt'
    linearTrendFile2 = r'S:/TEMP/DataAnalyze/LinearTrend2.txt'
    expTrendFile1 = r'S:/TEMP/DataAnalyze/ExpTrend1.txt'
    expTrendFile2 = r'S:/TEMP/DataAnalyze/ExpTrend2.txt'

    array_data = raw_data_reader.read_array_data(file)

    linear_trend1 = trend_reader.read_linear_trend_data(linearTrendFile1)
    linear_values1 = calculator.calculate_linear_trend(linear_trend1)

    linear_trend2 = trend_reader.read_linear_trend_data(linearTrendFile2)
    linear_values2 = calculator.calculate_linear_trend(linear_trend2)

    exp_trend1 = trend_reader.read_exp_trend_data(expTrendFile1)
    exp_values1 = calculator.calculate_exp_trend(exp_trend1)

    exp_trend2 = trend_reader.read_exp_trend_data(expTrendFile2)
    exp_values2 = calculator.calculate_exp_trend(exp_trend2)

    lt_panel = GraphPanel(main_window.lt_frame)
    lt_panel.plot_graph(np.arange(len(linear_values1)), linear_values1)
    rt_panel = GraphPanel(main_window.rt_frame)
    rt_panel.plot_graph(np.arange(len(linear_values2)), linear_values2)
    lb_panel = GraphPanel(main_window.lb_frame)
    lb_panel.plot_graph(np.arange(len(exp_values1)), exp_values1)
    rb_panel = GraphPanel(main_window.rb_frame)
    rb_panel.plot_graph(np.arange(len(exp_values2)), exp_values2)

    # rb_panel = ButtonPanel(main_window.rb_frame, update_plots)

    main_window.mainloop()
