from typing import Callable

from UI.MainWindow import MainWindow
from tkinter import Tk

from UI.Panels.GraphPanel import GraphPanel


root: Tk = None
window: MainWindow = None
lt_panel: GraphPanel = None
rt_panel: GraphPanel = None
lb_panel: GraphPanel = None
rb_panel: GraphPanel = None


def create():
    global root, window
    if not root:
        root = Tk()
    if not window:
        window = MainWindow(root)


def start(action: Callable = None) -> None:
    create()
    init_graph_panels()

    if action is not None:
        action()

    window.mainloop()


def init_graph_panels():
    global lt_panel, rt_panel, lb_panel, rb_panel
    lt_panel = GraphPanel(window.lt_frame)
    rt_panel = GraphPanel(window.rt_frame)
    lb_panel = GraphPanel(window.lb_frame)
    rb_panel = GraphPanel(window.rb_frame)


def get_panel(index: int) -> GraphPanel:
    if index == 0:
        return lt_panel
    if index == 1:
        return rt_panel
    if index == 2:
        return lb_panel
    if index == 3:
        return rb_panel


def clear() -> None:
    lt_panel.clear_graph()
    lb_panel.clear_graph()
    rt_panel.clear_graph()
    rb_panel.clear_graph()
