__author__ = 'jeroendevries'
from tkinter import *
import LoopTreinen


def uitvoer():
    LoopTreinen.eind_bestemming()


window = Tk()
label = Label(window, text='Gewenste eindbestemming vanuit Utrecht')
label.pack()

naam = Entry(window)
naam.pack()

button = Button(window, text='Zoek',
                command=(lambda: uitvoer(naam.get())))
button.pack()

w = Text(window)
w.pack()


window.mainloop()