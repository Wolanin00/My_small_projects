class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").capitalize()
        while answer not in ['True', 'False']:
            print('Wrong answer. Try again.')
            answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").capitalize()
        self.check_answer(answer=answer, correct_answer=current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.capitalize() == correct_answer.capitalize():
            print('You got it right!')
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Te correct answer was: {correct_answer}")
        print(f"your current score is: {self.score}/{self.question_number}\n")
