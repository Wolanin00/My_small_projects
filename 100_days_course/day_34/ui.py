from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            fill=THEME_COLOR,
            font=("Arial", 18, "italic"),
            width=280,
            text='Some question text')
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, background=THEME_COLOR, command=self.true_button)
        self.right_button.grid(column=0, row=2)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, background=THEME_COLOR, command=self.wrong_button)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        self.right_button.config(state="normal")
        self.wrong_button.config(state="normal")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, justify='center')
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz.\n"
                                        f"You got {self.quiz.score}/{len(self.quiz.question_list)} points",
                                   justify='center')
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")
        self.window.after(1000, self.get_next_question)
