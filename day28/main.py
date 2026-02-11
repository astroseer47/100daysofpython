from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text=f"Long Break")
    elif reps % 2== 0:
        label.config(text=f"Short Break")
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text=f"Work")
        count_down(WORK_MIN * 60)

def reset_timer():
    global reps

    reps = 0
    window.after_cancel(timer)
    check_mark.config(text="✅")
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minute = count // 60
    sec = count % 60

    if sec < 10:
        sec = "0" + str(sec)
    if minute < 10:
        minute = "0" + str(minute)



    if count > 0:
        global timer
        timer = window.after(100, count_down, count-1)
        canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark = mark + "✅"
        check_mark.config(text=mark)



# ----------------- ----------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50))
label.grid(row=0, column=1)

canvas = Canvas(window, width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


start_button = Button(text="Start", command=start_timer, highlightthickness=0,highlightbackground=YELLOW,)
start_button.grid(row=2, column=0)


reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)


check_mark = Label(text="✅", highlightthickness=0, bg=YELLOW, activebackground=YELLOW,)
check_mark.grid(row=3, column=1)


window.mainloop()