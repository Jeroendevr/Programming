__author__ = 'jeroendevries'
from tkinter import *
from tkinter.messagebox import showinfo

def antwoord(text):
    showinfo(title='popup', message='Hoi ' + text)

window = Tk()
label = Label(window, text='Hello World')
label.pack()

naam = Entry(window)
naam.pack()
## intergeren lukt hier niet

button = Button(window, text='Druk Hier',
                command=(lambda: antwoord(naam.get())))
button.pack()

window.mainloop()
