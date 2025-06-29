from tkinter import *
from time import *

def update():
    time_label.config(text=strftime("%I:%M:%S %p"))
    day_label.config(text=strftime("%A"))
    date_label.config(text=strftime("%B %d, %Y"))
    window.after(1000, update)

window = Tk()

window.title("Digital Clock")

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25))
day_label.pack()

date_label = Label(window, font=("Ink Free", 30))
date_label.pack()

update()

window.mainloop()