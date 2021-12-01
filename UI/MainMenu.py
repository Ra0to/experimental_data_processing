from collections import Callable
from tkinter import *
from Labs import LabsController
from UI import ui_controller


class MainMenu(Menu):
    def __init__(self, frame: Frame):
        super().__init__()

        self._last_action = None

        def create_menu(parent: Menu, actions: dict) -> Menu:
            def command_generator(action: Callable) -> Callable:
                return lambda: self.execute(action)

            menu = Menu(parent, tearoff=0)
            for element in actions:
                if type(actions[element]) is dict:
                    sub_menu = create_menu(menu, actions[element])
                    menu.add_cascade(label=element, menu=sub_menu)
                else:
                    menu.add_command(label=element, command=command_generator(actions[element]))
            return menu

        self._labs_menu = create_menu(self, LabsController.actions)

        self._stats_menu = Menu(self, tearoff=0)
        self._stats_menu.add_command(label='Stats LT Graph', command=lambda: ui_controller.lt_panel.print_graph_info())
        self._stats_menu.add_command(label='Stats RT Graph', command=lambda: ui_controller.rt_panel.print_graph_info())
        self._stats_menu.add_command(label='Stats LB Graph', command=lambda: ui_controller.lb_panel.print_graph_info())
        self._stats_menu.add_command(label='Stats RB Graph', command=lambda: ui_controller.rb_panel.print_graph_info())
        self._stats_menu.add_command(label='Calculate local maximums', command=lambda: ui_controller.rt_panel.find_local_maxima())

        self.add_cascade(label='Labs', menu=self._labs_menu)
        self.add_cascade(label='Tools', menu=self._stats_menu)
        self.add_command(label='Refresh', command=self.refresh)
        self.add_command(label='Clear', command=ui_controller.clear)

        frame.bind('<Key>', self.on_key_pressed)

    def on_key_pressed(self, event):
        # F5 pressed
        if event.keycode == 116:
            self.refresh()

    def execute(self, action: Callable):
        ui_controller.clear()

        self._last_action = action
        action()

    def refresh(self):
        if self._last_action is None:
            return

        self._last_action()
