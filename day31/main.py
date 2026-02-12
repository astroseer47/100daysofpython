from tkinter import *
import pandas
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict("records")
else:
    to_learn = data.to_dict("records")

window = Tk()
window.title("Flash Cards")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

right_check_image = PhotoImage(file="images/right.png")
wrong_check_image = PhotoImage(file="images/wrong.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

current_card = {}
def next_card():
    global current_card, flip_action

    if len(to_learn) == 0:
        messagebox.showerror("Error", "No more words available")
    window.after_cancel(flip_action)
    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    flip_action = canvas.after(3000, func=reveal_card)

def reveal_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)

    df = pandas.DataFrame(to_learn)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()



canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400,263,image=card_front_image)

card_title = canvas.create_text(400, 150,fill=BACKGROUND_COLOR, text="", font=("Times New Roman", 40, "italic"))
card_text = canvas.create_text(400,263, fill=BACKGROUND_COLOR,text="", font=("Times New Roman", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

unknown_button = Button(image=wrong_check_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_button = Button(image=right_check_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

flip_action = canvas.after(3000, func=reveal_card)

next_card()




window.mainloop()