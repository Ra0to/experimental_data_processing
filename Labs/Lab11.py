import math

import numpy as np
from numpy import dtype

from Models.plots import PlotData
from Models.trends import HarmonicTrend, ExpTrendData, LinearTrendData
from Modules import calculator, tools
from Modules.Analysis import stats
from Modules.IO_System.Readers import trend_reader
from UI import ui_controller


N = 1000

data_file_path = r'S:/TEMP/DataAnalyze/pgp_float4_1000_2ms.dat'
file_N = 1000
file_dt = 0.002

data_ys = trend_reader.read_float_byte_array_file(data_file_path, file_N)
data_xs = np.arange(0, file_N * file_dt, file_dt)
data = PlotData(tuple(data_xs), data_ys)


# m = 32 используем это , m = 16
# для отображения частотной хар-ки умножаем на N чтобы было 1
# отображаем частотную хар-ку фильтра, отражаем спектр отфильрованного сигнала, отфильтрованный сигнал,
# импульсную реакцию фильтра
# 4 фильтра пробуем, низкочастотный, высокочастотный, типо окно с 0 остальное 1, типо окно с 1 остальное 0
def action():
    ui_controller.lt_panel.plot_graph(data.xs, data.ys, 'Input')
    spectre = tools.amplitude_spectre_fourier(data, file_dt)
    ui_controller.rt_panel.plot_graph(spectre.xs, spectre.ys, 'Spectre')

    fc = 15
    fc2 = 200
    m = 64
    dt = file_dt
    lpf = tools.lpf(fc, dt, m)

    lpf_spectre = tools.amplitude_spectre_fourier(lpf, dt)
    # ui_controller.lb_panel.plot_graph(lpf.xs, lpf.ys, 'LPF')
    # ui_controller.rb_panel.plot_graph(lpf_spectre.xs, tuple(i * (2 * m + 1) for i in lpf_spectre.ys), 'LPF Spectre')

    svertka = tools.convolution(data, lpf)
    svertka_spectre = tools.amplitude_spectre_fourier(svertka, file_dt)
    # ui_controller.lb_panel.plot_graph(svertka.xs, svertka.ys, 'Filtered input')
    # ui_controller.rb_panel.plot_graph(svertka_spectre.xs, svertka_spectre.ys, 'Spectre')

    hpw = tools.hpf(lpf)
    hpw_spectre = tools.amplitude_spectre_fourier(hpw, dt)
    # ui_controller.lb_panel.plot_graph(hpw.xs, hpw.ys, 'HPF')
    # ui_controller.rb_panel.plot_graph(hpw_spectre.xs, tuple(i * (2 * m + 1) for i in hpw_spectre.ys), 'HPF Spectre')

    svertka = tools.convolution(data, hpw)
    svertka_spectre = tools.amplitude_spectre_fourier(svertka, file_dt)
    # ui_controller.lb_panel.plot_graph(svertka.xs, svertka.ys, 'Filtered input')
    # ui_controller.rb_panel.plot_graph(svertka_spectre.xs, svertka_spectre.ys, 'Spectre')

    bpf = tools.bpf(fc, fc2, dt, m)
    bpf_spectre = tools.amplitude_spectre_fourier(bpf, dt)

    # ui_controller.lb_panel.plot(bpf, 'BPF')
    # ui_controller.rb_panel.plot_graph(bpf_spectre.xs, tuple(i * (2 * m + 1) for i in bpf_spectre.ys), 'BPF Spectre')

    svertka = tools.convolution(data, bpf)
    svertka_spectre = tools.amplitude_spectre_fourier(svertka, file_dt)
    # ui_controller.lb_panel.plot_graph(svertka.xs, svertka.ys, 'Filtered input')
    # ui_controller.rb_panel.plot_graph(svertka_spectre.xs, svertka_spectre.ys, 'Spectre')

    bsf = tools.bsf(fc, fc2, dt, m)
    bsf_spectre = tools.amplitude_spectre_fourier(bsf, dt)

    # ui_controller.lb_panel.plot(bsf, 'BSF')
    # ui_controller.rb_panel.plot_graph(bsf_spectre.xs, tuple(i * (2 * m + 1) for i in bsf_spectre.ys), 'BSF Spectre')

    svertka = tools.convolution(data, bsf)

    svertka_spectre = tools.amplitude_spectre_fourier(svertka, file_dt)
    # ui_controller.lb_panel.plot(svertka, 'Filtered Input')
    # ui_controller.rb_panel.plot(svertka_spectre, 'Spectre')



