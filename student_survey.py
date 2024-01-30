from tkinter import *
from tkinter import Tk,ttk
from tkinter import messagebox



root = Tk()


root.title("Centennial College")






mylabel = Label(root, text="ICET Student Survey",font=("Arial",25))
mylabel.grid()




Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)


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



# creating entry for label 1
fn = ttk.Entry(
    frame,
    textvariable=username
).grid(
    column=1,
    row=1,
    sticky=(W)
)

residency = StringVar()

#creating label 2
ttk.Label(frame,text='Residency:').grid(column=0,row=2,sticky=(W,E))
#creating panel for radio button
panel = ttk.Frame(frame)
panel.grid(column=1,row=2,sticky=(W,E))
panel['borderwidth'] = 3
residency = StringVar()

#creating radio buttons
ttk.Radiobutton(panel,text='Domestic',variable=residency,value='dom').grid(
    column=0, row=0, sticky=(W)
)
ttk.Radiobutton(panel,text='International',variable=residency,value='intl').grid(
    column=0, row=1, sticky=(W)
)

#combo box for programs
#AI, Gaming,Health and Software

ttk.Label(frame,text='Program:').grid(column=0,row=3,sticky=(W,E))

panel = ttk.Frame(frame)
panel.grid(column=1,row=3,sticky=(W,E))
panel['borderwidth'] = 3
program = StringVar()

combo = ttk.Combobox(frame,textvariable=program,values=['AI','Gaming','Health','Software'])
combo.grid(column=1, row=3,sticky=(W,E))









#creating label for courses

ttk.Label(frame,text='Courses:').grid(column=0,row=4,sticky=(W,E))

#creating panel for courses
panel = ttk.Frame(frame)
panel.grid(column=1,row=4,columnspan=4,sticky=(W,E))
panel['borderwidth'] = 3

comp100 = StringVar()
comp213 = StringVar()
comp120 = StringVar()



#checkbuttons

# check = ttk.Checkbutton(
#     text='Programming I',
#     variable=comp100,
#     #offvalue = 'imperial',
#     onvalue='comp100')
# check.grid(column=0,row=0,sticky=(W))

ttk.Checkbutton(panel, text='Web Page Design',variable=comp213,onvalue='comp213').grid(
column=0,row=1, sticky=(W))


ttk.Checkbutton(panel, text='Software Engineering Fundamentals',variable=comp120,onvalue='comp129').grid(
column=0,row=2, sticky=(W))

ttk.Checkbutton(panel, text='Programming I',variable=comp100,onvalue='comp100').grid(
column=0,row=0, sticky=(W))

        
#reset button
button = ttk.Button(frame,text='Reset',padding=20,command=lambda:m_reset())
button.grid(column=0,row=5,sticky=(W,E))


    

#ok button

#function
 
def read_form(*args):
    messagebox.showinfo(
        title='Form Info',
        message=f'\nFullname: {username.get()} \nResidency: {residency.get()} \nCourses: {comp100.get()} {comp120.get()} {comp213.get()} \nProgram: {program.get()}'
    )
ttk.Button(frame, text='Ok', command=read_form).grid(column=1, row=5, sticky=(W, E))


#exit button

ttk.Button(frame,text='Exit',
           command=root.quit).grid(
               
           column=2,row=5,sticky=(W,E))



def m_reset():
    for widget in frame.winfo_children():
        if isinstance(widget, ttk.Entry):
            widget.delete(0, 'end')
        elif isinstance(widget, ttk.Combobox):
            widget.delete(0,'end')  # Use 'set' to clear the selected value
        elif isinstance(widget, ttk.Checkbutton):
            widget.state(['!alternate'])
        elif isinstance(widget, ttk.Radiobutton):
            widget.state(['!selected'])

    residency.set(None)
    program.set('')
    



root.mainloop()
