from datetime import *

from tkinter import *


class MainWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(expand=1, fill=BOTH)

        self.master.geometry('750x750')
        self.master.title(datetime.now())

        # TODO remove m_line and tm_line, bm_line
        self.top_frame = Frame(self)
        # self.m_line = Frame(self, bg='#000000', height=3)
        self.bottom_frame = Frame(self)

        self.lt_frame = Frame(self.top_frame, bg='#EEEEEE')
        # self.tm_line = Frame(self.top_frame, bg='#000000', width=3)
        self.rt_frame = Frame(self.top_frame, bg='#2B2B2B')

        self.lb_frame = Frame(self.bottom_frame, bg='#859198')
        # self.bm_line = Frame(self.bottom_frame, bg='#000000', width=3)
        self.rb_frame = Frame(self.bottom_frame, bg='#CCCCCC')

        self.repack()

    def repack(self):
        self.pack(expand=1, fill=BOTH)
        self.top_frame.pack(expand=1, fill=BOTH)
        # self.m_line.pack(fill=X)
        self.bottom_frame.pack(expand=1, fill=BOTH)
        self.lt_frame.pack(side=LEFT, expand=1, fill=BOTH)
        # self.tm_line.pack(side=LEFT, fill=Y)
        self.rt_frame.pack(side=LEFT, expand=1, fill=BOTH)
        self.lb_frame.pack(side=LEFT, expand=1, fill=BOTH)
        # self.bm_line.pack(side=LEFT, fill=Y)
        self.rb_frame.pack(side=LEFT, expand=1, fill=BOTH)

