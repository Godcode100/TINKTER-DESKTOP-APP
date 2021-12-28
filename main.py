from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('DESKTOP CLOCK')

def show_the_time():
    string = strftime('%H:%M:%S %p')
    Label.config(text = string)
    Label.after(1000, show_the_time)

Label = Label(root, font = ('calibri',70,'italic'), background = 'black',foreground ='gold')
Label.pack(anchor ='n')

show_the_time()

mainloop()
