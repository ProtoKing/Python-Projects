from tkinter import *
CONVERSION_FACTOR = 1.609
window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# Commands
def button_click():
    miles = float(input.get())
    km = miles * CONVERSION_FACTOR
    output_km_label.config(text=f"{km}")

# 1 Entry
input = Entry()
input.grid(row=0, column=1)

# 5 Labels
equal_label = Label(text="is equal to")
equal_label.grid(row=0, column=1)

output_km_label = Label(text="0")
output_km_label.grid(row=1, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text='Calculate', command=button_click)
button.grid(row=1, column=1)

window.mainloop()

# Add the Layout
# Title, 5 labels, 1 button,