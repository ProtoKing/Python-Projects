from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)

# ---------------------------- SEARCH ------------------------------- #
def find_password():

    website = website_entry.get()
    user_email = email_entry.get()

    try:
        with open('data.json', "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error!", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Use Login Data:", message=f"Email: {email}\n"
                                                                 f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(message="Fill out all fields")
    else:
        try:
            with open('data.json', "r") as data_file:
                # Read old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        # data.write(f"{website} | {email} | {password}\n")     ## this is for txt file.
        website_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=password_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:', font=('Arial', 11,'bold'))
website_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:', font=('Arial', 11,'bold'))
email_label.grid(row=2, column=0)

password_label = Label(text='Password:', font=('Arial', 11, 'bold'))
password_label.grid(row=3, column=0)

# Buttons
search_button = Button(text='Search', font=('Arial', 9, 'bold'), command=find_password, width=16)
search_button.grid(row=1, column=2)

gen_pass_button = Button(text='Generate Password', font=('Arial', 9, 'bold'), command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text='Add', font=('Arial', 11, 'bold'), width=35, command=add)
add_button.grid(row=4, column=1, columnspan=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0,"steveanthonynalos@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

window.mainloop()