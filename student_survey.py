from tkinter import *
from tkinter import ttk


root = Tk()
root.title("ICET Student Survey")

frame = ttk.Frame(
    root,
    width = 360,
    height = 240,
    
)
frame.grid()

frame['padding'] = (5,10)
frame['borderwidth'] = 10


#creating label 1

lbl_full_name = ttk.Label(
    frame,
    text='Full name:').grid(
    column=0,
    row=1,
    sticky=(W,E))
    
username = StringVar()



root.mainloop()
