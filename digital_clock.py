from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title('My Clock')

def time():
    myTime = strftime('%H:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000, time)

clock = Label(myWindow, font = ('arial', 40, 'bold'),
                                background = 'dark blue',
                                foreground = 'white')
clock.grid(row=0, column=0, sticky='nsew')

myWindow.grid_rowconfigure(0, weight=1)
myWindow.grid_columnconfigure(0, weight=1)
#clock.pack(anchor = 'center')
time()

myWindow.mainloop()