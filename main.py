from tkinter import *
from time import strftime

screen=Tk()
screen.title("clock")




def digitalClockTime():
    timer = strftime('%H:%M:%S')
    timeLabel.config(text=timer)
    timeLabel.after(1000,digitalClockTime)

timeLabel = Label(screen,font=100)


timeLabel.pack()
digitalClockTime()

screen.mainloop()