class Question:
    def __init__(self, q, a, w1, w2, w3):
        self.question = q
        self.answer = a
        self.wrong_ans1 = w1
        self.wrong_ans2 = w2
        self.wrong_ans3 = w3

        self.attempts = 0
        self.correct = 0
        
    def got_right(self):
        print("Правильно!")
        self.correct += 1
        self.attempts += 1

    def got_wrong(self):
        print("Неправильно!")
        self.attempts += 1

class QuestionView:
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.frm_model = frm_model
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3


    def change(self, frm_model):
        self.frm_model = frm_model

    def show(self):
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)
