from tkinter import *
from tkinter import ttk


root = Tk()
root.title("ICET Student Survey")

frame = ttk.Frame(
    root,
    width = 360,
    height = 240
)
frame.grid()

frame['padding'] = (5,10)
frame['borderwidth'] = 10

root.mainloop()
