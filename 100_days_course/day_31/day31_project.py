from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
prev_card = {}

try:
    raw_data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_to_learn = pd.DataFrame.to_dict(original_data, orient="records")
else:
    data_to_learn = pd.DataFrame.to_dict(raw_data, orient="records")


def correct_answer():
    try:
        data_to_learn.remove(current_card)
        data = pd.DataFrame(data_to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
    except ValueError:
        canvas.itemconfig(card_canvas, image=card_front_img)
        canvas.itemconfig(language_text, text='', fill='black')
        canvas.itemconfig(word_text, text='You got all', fill='black')
        os.remove("data/words_to_learn.csv")
    else:
        if len(data_to_learn) > 0:
            new_random_card()


def new_random_card():
    global current_card, flip_timer, prev_card
    window.after_cancel(flip_timer)
    if len(data_to_learn) == 1:
        current_card = random.choice(data_to_learn)
    else:
        while current_card == prev_card:
            current_card = random.choice(data_to_learn)
    canvas.itemconfig(card_canvas, image=card_front_img)
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, flip_card)
    prev_card = current_card


def flip_card():
    canvas.itemconfig(card_canvas, image=card_back_img)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_canvas = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, command=new_random_card)
wrong_button.grid(column=0, row=1)

correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, border=0, command=correct_answer)
correct_button.grid(column=1, row=1)

new_random_card()

window.mainloop()
