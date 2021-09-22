from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GraphPanel:
    def __init__(self, frame: Frame):
        self.figure = Figure(figsize=(0.3, 0.3), dpi=100)

        self.canvas = FigureCanvasTkAgg(self.figure, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=1, fill=BOTH)

    def plot_graph(self, xs, ys):
        self.figure.clear()
        self.figure.add_subplot().plot(xs, ys)
        self.canvas.draw()


class ButtonPanel:
    def __init__(self, frame: Frame, on_button_pressed):
        self.button = Button(frame, width=15, height=7, text='Refresh', command=on_button_pressed)
        self.button.pack()
