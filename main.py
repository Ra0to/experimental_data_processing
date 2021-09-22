from tkinter import *

import Lab1
import Lab2

if __name__ == '__main__':
    Lab2.random_values()

def tests():
    root = Tk()
    root.geometry('750x750')
    root.title('Test')

    COLUMNS = 2
    ROWS = 2
    root.columnconfigure(tuple(range(COLUMNS)), weight=1)
    root.rowconfigure(tuple(range(ROWS)), weight=1)

    lt_frame = Frame(root, bg='red')
    rt_frame = Frame(root, bg='orange')

    lb_frame = Frame(root, bg='green')
    rb_frame = Frame(root, bg='yellow')

    button = Button(lt_frame, text='This is a BIG Button!')
    # button2 = Button(rt_frame, text='Yet another a Big BUTTON!')

    lt_frame.grid(row=0, column=0, sticky='news')
    rt_frame.grid(row=0, column=1, sticky='news')
    lb_frame.grid(row=1, column=0, sticky='news')
    rb_frame.grid(row=1, column=1, sticky='news')

    button.pack()
    # button2.grid()

    root.mainloop()
