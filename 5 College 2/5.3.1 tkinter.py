__author__ = 'jeroendevries'
from tkinter import *
from tkinter.messagebox import showinfo


def links():
    showinfo(title="Links", message='Links!')


def rechts():
    showinfo(title='Rechts',message='Rechts!')


window = Tk()
label = Label(window, text='Kies uw richting')
label.pack()

buttonl = Button(window, text='Links', command=(lambda: links()))
buttonl.pack(padx=5, pady=10, side=LEFT)

buttonr = Button(window, text='Rechts', command=(lambda: rechts()))
buttonr.pack(padx=5, pady=10, side=RIGHT)

window.mainloop()