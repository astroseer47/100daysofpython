class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        question = self.q_list[self.question_number]
        self.question_number += 1

        answer = input(f"Q{self.question_number}: {question.text} True / False ?:")
        if (answer == "true" or answer == 't') and question.answer == 'True':
            self.score += 1
        elif (answer == "false" or answer == 'f')and question.answer == 'False':
            self.score += 1


    def still_has_question(self):
        return len(self.q_list) != self.question_number


    def show_score(self):
        print(f"Score: {self.score}")