from tkinter import messagebox, Frame, Button, BOTH

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Models.plots import PlotData
from Modules.Analysis import stats


class GraphPanel:
    def __init__(self, frame: Frame):
        self.figure = Figure(figsize=(0.3, 0.3), dpi=100)
        self._xs = tuple[float]()
        self._ys = tuple[float]()
        self._name = ""

        self.canvas = FigureCanvasTkAgg(self.figure, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=1, fill=BOTH)

    def plot(self, data: PlotData, name: str = '', xlims=None):
        self.plot_graph(data.xs, data.ys, name, xlims)

    def plot_graph(self, xs, ys, name: str = '', xlims=None):
        self.figure.clear()

        self._xs = xs
        self._ys = ys
        self._name = name

        subplot = self.figure.add_subplot()
        subplot.plot(self._xs, self._ys)

        if name != "":
            subplot.title.set_text(self._name)

        if xlims is not None:
            subplot.set_xlim(xlims)

        self.canvas.draw()

    def plot2(self, data, name):
        self.figure.clear()
        subplot = self.figure.add_subplot()
        subplot.plot(data)
        subplot.title.set_text(name)
        self.canvas.draw()

    def plot_hist(self, xs, bins, range_, name: str = ''):
        self.figure.clear()

        self._xs = xs
        self._name = name

        subplot = self.figure.add_subplot()
        subplot.hist(self._xs, bins, range_)

        if name != "":
            subplot.title.set_text(self._name)

        self.canvas.draw()

    def clear_graph(self):
        self.figure.clear()
        self.canvas.draw()

    def find_local_maxima(self):
        vals = []
        mean = sum(self._ys) / len(self._ys)
        for i in range(len(self._xs)):
            if self._ys[i] > mean:
                vals.append((self._xs[i], self._ys[i]))

        text = ''
        text += f'Values: \n'
        for (x, y) in vals:
            text += f'x = {round(x, 5)}; y = {round(y, 5)}\n'
        text += '\n\n'

        messagebox.showinfo(title='Min and Max', message=text)

    def print_graph_info(self):
        text = f'Graph Name: {self._name}\n\n'
        text += f'Points count: {len(self._xs)}\n'
        text += f'Min: {stats.min_value(self._ys):.5f}\n'
        text += f'Max: {stats.max_value(self._ys):.5f}\n'

        text += f'\nМат. ожидание: {stats.expected_value(self._ys):.5f}\n'
        text += f'Дисперсия: {stats.dispersion(self._ys):.5f}\n'
        text += f'Стандартное отклонение: {stats.standard_deviation(self._ys):.5f}\n'

        text += f'\nСредний квадрат: {stats.mean_square(self._ys):.5f}\n'
        text += f'Средне квадратичная ошибка: {stats.mean_square_error(self._ys):.5f}\n'
        text += f'\nАссиметрия: {stats.asymmetry(self._ys):.5f}\n'

        text += f'Коэффициент ассиметрии: {stats.asymmetry_coef(self._ys):.5f}\n'
        text += f'\nЭксцесс: {stats.excess(self._ys):.5f}\n'

        text += f'Коэффициент эксцесса: {stats.excess_coef(self._ys):.5f}\n'

        text += f'\n\nСтационарность функции: {stats.is_stationary_function(self._ys)}\n'
        # text += f': {stats.(self._ys)}\n'
        messagebox.showinfo(title='Graph stats', message=text)


class ButtonPanel:
    def __init__(self, frame: Frame, on_button_pressed):
        self.button = Button(frame, width=15, height=7, text='Refresh', command=on_button_pressed)
        self.button.pack()
