from tkinter import *

def change():
    welcome.configure(text='Whatever it is that I want')
    

window = Tk()
window.title('My Awesome Software')
window.geometry('800x400')

welcome = Label(window, text='Welcome to my awesome super-fabulous software')
welcome.pack()

click = Button(window, text='Click Me', width=25, bg='green', fg='white', 
               command=change).pack()

mainloop()