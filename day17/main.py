from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(text=question["text"], answer=question["answer"]))

quiz_brain = QuizBrain(question_bank)


print(quiz_brain.still_has_question())
while quiz_brain.still_has_question():
    quiz_brain.next_question()

quiz_brain.show_score()