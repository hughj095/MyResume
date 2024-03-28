


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.current_score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        total_questions = self.question_number
        if user_answer.lower() == correct_answer.lower():
            print(user_answer)
            self.current_score += 1
        else:
            print("that's wrong")
        print(f"the correct answer is {correct_answer}")
        print(f"total score is {self.current_score} / {total_questions}")