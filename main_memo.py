from memo_data import *
from memo_card_layout import *
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle

card_width, card_height = 600, 500
text_right = 'Правильно!'
text_wrong = "Неправильно!"

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)

frm = Question("Яблоко", "Apple", "Tomato", "Carrot", "Orange")
frm_card = QuestionView(frm, lb_question, radio_list[0], radio_list[1], radio_list[2], radio_list[3])


answer = radio_list[0]
wrong_ans1, wrong_ans2, wrong_ans3 = radio_list[1], radio_list[2], radio_list[3]


def show_data():
    lb_question.setText(frm.question)
    lb_Correct.setText(frm.answer)
    answer.setText(frm.answer)
    wrong_ans1.setText(frm.wrong_ans1)
    wrong_ans2.setText(frm.wrong_ans2)
    wrong_ans3.setText(frm.wrong_ans3)


def check_result():
    correct = frm_card.answer.isChecked()
    if correct:
        lb_Result.setText(text_right)
        show_result()
    else:
        not_correct = frm.wrong_ans1.isChecked() or frm.wrong_ans2.isChecked() or frm.wrong_ans3.isChecked()
        if not correct:
            lb_Result.setText(text_wrong)
            show_result()



def click():
    if btn_ok.text() != "Следующий вопрос":
        check_result()


win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle("Memory Card")

win_card.setLayout(layout_card)

show_data()
show_question() 
btn_ok.clicked.connect(click)

win_card.show()
app.exec_()
