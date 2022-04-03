from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height = 300)
window.config(padx=20, pady=20)

my_label = Label(text="Egalitarian", font=('Arial', 24,"bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.grid(row=0, column=0)

def button_click():
    my_label["text"] = input.get()

#  New Button
new_button = Button(text='Reserve', command=button_click)
new_button.grid(row=0, column=2)
# new_button.pack() # no need to insert this.

#Button
button = Button(text='Press Me', command=button_click)
button.grid(row=1, column=1)
# button.pack()

# Entry
input = Entry(width=10)
input.grid(row=2, column=3)
# input.pack()







window.mainloop()
