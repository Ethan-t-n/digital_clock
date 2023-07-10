from tkinter import *
from time import strftime

myWindow = Tk()
myWindow.title('My Clock')

def update_time(event=None):
    font_size = max(int(myWindow.winfo_height() / 4), 42)
    myTime = strftime('%H:%M:%S %p')
    clock.config(text=myTime, font=('arial', font_size, 'bold'))

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

time()
update_time()
myWindow.bind('<Configure>', update_time)

myWindow.mainloop()