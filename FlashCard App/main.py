from tkinter import *
import pandas as pd
from random import *

# ---------------------------- CONSTANT ------------------------------- #


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
data_file = {}
random_word = {}

# ---------------------------- FUNCTIONS ------------------------------- #
try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')
    data_file = df.to_dict(orient='records')
else:
    data_file = df.to_dict(orient='records')


def generate_word():
    global random_word, flip
    window.after_cancel(flip)
    random_word = choice(data_file)
    canvas.itemconfig(canvas_current_img, image=card_front_img)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=random_word['French'], fill='black')
    flip = window.after(ms=3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_current_img, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=random_word['English'], fill='white')


def is_known():
    data_file.remove(random_word)
    new_data = pd.DataFrame(data_file)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR, padx=58, pady=58)
flip = window.after(ms=3000, func=flip_card)

# Flash Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas_current_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='', font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text='', font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# Flip Card

generate_word()
flip = window.after(ms=3000, func=flip_card)
window.after_cancel(id=flip)

window.mainloop()
