from tkinter import Tk, Label
import time

window=Tk()
window.title("Digital Clock")
window.geometry("420x150")
window.resizable(1,1)

tfont=("Boulder", 68, "bold")
bgc="red"
color="#363529"
width=25

label=Label(window, font=tfont, bg=bgc, fg=color, bd=width)
label.grid(row=0,column=0)

def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
window.mainloop()