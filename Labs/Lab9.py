import numpy as np

from Models.plots import PlotData
from Models.trends import HarmonicTrend, ExpTrendData, LinearTrendData
from Modules import calculator, tools
from Modules.Analysis import stats
from Modules.IO_System.Readers import trend_reader
from UI import ui_controller

N = 1000
dt = 0.001
harm = calculator.calculate_harmonic_trend(HarmonicTrend(N=N, dt=dt, A=10, f=3))
poly_data = calculator.calculate_polyharmonic_trend((
    HarmonicTrend(N=N, dt=dt, A=10, f=3),
    HarmonicTrend(N=N, dt=dt, A=100, f=37),
    HarmonicTrend(N=N, dt=dt, A=15, f=173)))
const_data = calculator.calculate_linear_trend(LinearTrendData(N=N, a=0, b=10))
const_wide_data = PlotData(xs=const_data.xs, ys=tuple(float(const_data.ys[i] if i < (0.8 * N) else 0) for i in range(len(const_data))))
const_narrow_data = PlotData(xs=const_data.xs, ys=tuple(float(const_data.ys[i] if i < (0.2 * N) else 0) for i in range(len(const_data))))

polyharm_wide_data = PlotData(xs=const_data.xs, ys=tuple(float(poly_data.ys[i] if i < (0.6 * N) else 0) for i in range(len(poly_data))))
random_data = calculator.calculate_random_trend(n=N, min_=-10, max_=10)
custom_random_data = calculator.calculate_custom_random_trend(n=N, min_=-10, max_=10)

linear_data = calculator.calculate_linear_trend(LinearTrendData(N=N, a=1, b=10))
exp_data = calculator.calculate_exp_trend(ExpTrendData(N=N, a=-0.005, b=5))
spike_data = tools.spikes(calculator.calculate_linear_trend(LinearTrendData(N=N, a=0, b=0)), 1, 1000, 100)

data_file_path = r'S:/TEMP/DataAnalyze/pgp_float4_1000_2ms.dat'
file_N = 1000
file_dt = 0.002

data_ys = trend_reader.read_float_byte_array_file(data_file_path, file_N)
data_xs = np.arange(0, file_N * file_dt, file_dt)
data = PlotData(tuple(data_xs), data_ys)


def plot_spectres(data_: PlotData, dt_: float):
    ui_controller.lt_panel.plot_graph(data_.xs, data_.ys, 'Input data')

    fourier = tools.amplitude_spectre_fourier(data_, dt_)
    ui_controller.rt_panel.plot_graph(fourier.xs, fourier.ys, 'Amplitude Spectre Fourier')

    phase_spectre = tools.phase_spectre_fourier(data_, dt_)
    ui_controller.rb_panel.plot_graph(phase_spectre.xs, phase_spectre.ys, 'Phase Spectre Fourier')


def harm_fourier():
    plot_spectres(harm, dt)


def polyharm_fourier():
    plot_spectres(poly_data, dt)


def const_fourier():
    plot_spectres(const_data, dt)


def const_wide_window_fourier():
    plot_spectres(const_wide_data, dt)


def const_narrow_window_fourier():
    plot_spectres(const_narrow_data, dt)


def polyharm_wide_window_fourier():
    plot_spectres(polyharm_wide_data, dt)


def random_spectre():
    plot_spectres(random_data, dt)


def custom_random_spectre():
    plot_spectres(random_data, dt)


def linear_spectre():
    plot_spectres(linear_data, dt)


def exp_spectre():
    plot_spectres(exp_data, dt)


def spike_spectre():
    plot_spectres(spike_data, dt)


def file_spectre():
    plot_spectres(data, file_dt)
