from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
learn = []
to_learn = {}
# ---------------------------------- DATA CONVERSION -------------------------------------
try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------------- FLASH CARDS --------------------------------------
def new_card():
    global current_card, answer_timer
    window.after_cancel(answer_timer)
    canvas.itemconfig(canvas_image, image=front_png)
    current_card = choice(to_learn)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=current_card["French"], fill="black")
    answer_timer = window.after(1000, answer)


def answer():
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_png)


def remove_word():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# ---------------------------------- UI SETUP --------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

answer_timer = window.after(1000, answer)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_png = PhotoImage(file=".\\images\\card_front.png")
back_png = PhotoImage(file=".\\images\\card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_png)
canvas.grid(column=0, row=0, columnspan=2)

# Labels --------------------------------------------------

language_label = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))

word_label = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Buttons -------------------------------------------------

right_png = PhotoImage(file=".\\images\\right.png")
known_button = Button(image=right_png, highlightthickness=0, bd=0, command=lambda: remove_word())
known_button.grid(column=1, row=1)

wrong_png = PhotoImage(file=".\\images\\wrong.png")
unknown_button = Button(image=wrong_png, highlightthickness=0, bd=0, command=lambda: new_card())
unknown_button.grid(column=0, row=1)

flashy_on = True

new_card()

window.mainloop()
