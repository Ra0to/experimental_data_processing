from datetime import *

from tkinter import *

from UI.MainMenu import MainMenu


class MainWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        menu = MainMenu(master)
        master.config(menu=menu)

        self.pack(expand=1, fill=BOTH)

        self.master.geometry('750x750')
        self.master.title(datetime.now())

        self.top_frame = Frame(self)
        self.bottom_frame = Frame(self)

        self.lt_frame = Frame(self.top_frame, bg='#EEEEEE')
        self.rt_frame = Frame(self.top_frame, bg='#2B2B2B')

        self.lb_frame = Frame(self.bottom_frame, bg='#859198')
        self.rb_frame = Frame(self.bottom_frame, bg='#CCCCCC')

        self.repack()

    def repack(self):
        self.pack(expand=1, fill=BOTH)

        self.top_frame.pack(expand=1, fill=BOTH)
        self.bottom_frame.pack(expand=1, fill=BOTH)

        self.lt_frame.pack(side=LEFT, expand=1, fill=BOTH)
        self.rt_frame.pack(side=LEFT, expand=1, fill=BOTH)
        self.lb_frame.pack(side=LEFT, expand=1, fill=BOTH)
        self.rb_frame.pack(side=LEFT, expand=1, fill=BOTH)

