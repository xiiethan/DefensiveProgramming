#
# from tkinter import *
# window = Tk()
# window.title("Welcome to the System Crash Shopping app")
# window.geometry('350x200')
# lbl = Label(window, text="Don't Click That Button")
# lbl.grid(column=0, row=0)
# btn = Button(window, text="Click Me")
# btn.grid(column=1, row=0)
# window.mainloop()



import tkinter as tk

window = tk.Tk()

window.title("Welcome to the System Crash Shopping app")

window.geometry('350x200')
menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label='Hint')

new_item.add_separator()


new_item.add_command(label='Hint 2')
menu.add_cascade(label='File', menu=new_item)

window.config(menu=menu)
lbl = Label(window, text="Don't Click That Button")

lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="You Clicked It!")
def clickedMe():
    lbl.configure(text="You Shoudld've clicked me quicker.")

btn = Button(window, text="Click Me", command=clicked)
btn2 = Button(window, text = "No Click Me", command=clickedMe)
btn.pack(fill=tk.X, padx=10)
btn2.grid(column=1, row=3)

window.mainloop()
