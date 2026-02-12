from tkinter import *
from tkinter import messagebox

from day34.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_breain: QuizBrain):
        self.quiz = quiz_breain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(self.window, text="Score:0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR, font=("Arial", 20))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right_image, highlightthickness=0, command=self.right_answer)
        self.right_button.grid(row=2, column=0)

        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong_answer)
        self.wrong_button.grid(row=2, column=1)


        self.show_question()

        self.window.mainloop()


    def show_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def right_answer(self):
        self.check_answer(True)

    def wrong_answer(self):
        self.check_answer(False)

    def check_answer(self, user_answer):
        self.quiz.check_answer(user_answer)
        self.show_score(self.quiz.score)
        if self.quiz.still_has_questions():
            self.show_question()
        else:
            messagebox.showinfo("Game Over", f"Your score is: {self.quiz.score}!")

    def show_score(self, score):
        self.score_label.config(text=f"Score: {score}")




