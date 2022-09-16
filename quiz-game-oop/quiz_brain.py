class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q_index = self.question_number
        q_current = self.question_list[q_index]
        q_index += 1
        q_text = q_current.text
        q_answer = q_current.answer

        user_answer = input(f"Q.{q_index}: {q_text}. True / False: ")
        self.check_answer(user_answer, q_answer)

    def check_answer(self, user_answer, q_answer):
        if user_answer.lower() == q_answer.lower():
            self.score += 1
            print("You got it right!")
            # print(f"Next: {self.question_list[q_index].text}")
        else:
            self.score -= 1
            print("You got it wrong!.")

        print(f"The correct answer is: {q_answer}")
