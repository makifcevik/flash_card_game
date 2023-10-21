from tkinter import *
import pandas as pd
from random import randint, choice

# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_SMALL = ("Ariel", 25, "italic")
FONT_BIG = ("Ariel", 60, "bold")

data = pd.read_csv("./data/formatted_words.txt")
data_dict = data.to_dict()


def format_def(text: str):
    output = ""
    count = 0
    for char in text:
        if char == " ":
            count += 1
        if count == 5:
            char = "\n"
            count = 0
        output += char
    return output


def next_word():
    random_index = randint(0, len(data_dict["Word"]))
    random_word = data_dict["Word"][random_index]
    word_def = format_def(data_dict["Definition"][random_index])

    canvas.itemconfig(item_title, text=random_word)
    canvas.itemconfig(item_def, text=word_def)


# ---------------------- UI

# Window Configuration
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Image Registration
img_card_front = PhotoImage(file="./images/card_front.png")
img_card_back = PhotoImage(file="./images/card_back.png")
img_wrong = PhotoImage(file="./images/wrong.png")
img_right = PhotoImage(file="./images/right.png")

# Canvas Configuration
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.create_image(0, 0, anchor=NW, image=img_card_front)
item_title = canvas.create_text(400, 150, text="Title", font=FONT_BIG)
item_def = canvas.create_text(400, 320, text="Definition Text Will Go Here \nAs It Should Be.", font=FONT_SMALL)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

# Button Wrong
button_wrong = Button(image=img_wrong, highlightthickness=0, borderwidth=0, command=next_word)
button_wrong.grid(column=0, row=1)

# Button Right
button_right = Button(image=img_right, highlightthickness=0, borderwidth=0, command=next_word)
button_right.grid(column=1, row=1)

window.mainloop()
