from tkinter import *
import numpy as np

from Modules import calculator
from Modules.IO_System.Readers import trend_reader
from UI.MainWindow import MainWindow
from UI.Panels.GraphPanel import GraphPanel


def graphs():
    root = Tk()
    main_window = MainWindow(root)

    linearTrendFile1 = r'S:/TEMP/DataAnalyze/LinearTrend1.txt'
    linearTrendFile2 = r'S:/TEMP/DataAnalyze/LinearTrend2.txt'

    linear_trend1 = trend_reader.read_linear_trend_data(linearTrendFile1)
    linear_values1 = calculator.calculate_linear_trend(linear_trend1)

    linear_trend2 = trend_reader.read_linear_trend_data(linearTrendFile2)
    linear_values2 = calculator.calculate_linear_trend(linear_trend2)

    lt_panel = GraphPanel(main_window.lt_frame)
    lt_panel.plot_graph(np.arange(len(linear_values1)), linear_values1)
    rt_panel = GraphPanel(main_window.rt_frame)
    rt_panel.plot_graph(np.arange(len(linear_values2)), linear_values2)

    random_values1 = calculator.calculate_random_trend(len(linear_values1), -5, 5)
    random_values2 = calculator.calculate_random_trend(len(linear_values2), -5, 5)
    noise_values1 = tuple(linear_values1[i] + random_values1[i] for i in range(len(linear_values1)))
    noise_values2 = tuple(linear_values2[i] * random_values2[i] for i in range(len(linear_values2)))

    lb_panel = GraphPanel(main_window.lb_frame)
    lb_panel.plot_graph(np.arange(len(noise_values1)), noise_values1)
    rb_panel = GraphPanel(main_window.rb_frame)
    rb_panel.plot_graph(np.arange(len(noise_values2)), noise_values2)

    main_window.mainloop()


def random_values():
    root = Tk()
    main_window = MainWindow(root)

    random_values = calculator.calculate_random_trend(100, -5, 5)
    lt_panel = GraphPanel(main_window.lt_frame)
    lt_panel.plot_graph(np.arange(len(random_values)), random_values)

    random_values = calculator.calculate_custom_random_trend(100, -5, 5)
    rt_panel = GraphPanel(main_window.rt_frame)
    rt_panel.plot_graph(np.arange(len(random_values)), random_values)

    def key_pressed(e):
        lt_panel.plot_graph(np.arange(len(random_values)), calculator.calculate_random_trend(100, -5, 5))
        rt_panel.plot_graph(np.arange(len(random_values)), calculator.calculate_custom_random_trend(100, -5, 5))
        print(e)

    root.bind('<KeyPress>', key_pressed)
    main_window.mainloop()
