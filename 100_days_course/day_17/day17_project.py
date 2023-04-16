from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(q_text=data['text'], q_answer=data['answer']) for data in question_data]

quiz = QuizBrain(question_bank=question_bank)
while quiz.still_have_question():
    quiz.next_question()
print("You have completed quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
