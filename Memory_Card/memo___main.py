from memo___card_layout import *
from PyQt5.QtWidgets import QApplication, QWidget
from time import sleep
from random import * # будем перемешивать ответы в карточке вопроса
rbtn_list=[rbtn_1, rbtn_2, rbtn_3, rbtn_4]
class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question=question
        self.answer=answer
        self.wrong_answer1=wrong_answer1
        self.wrong_answer2=wrong_answer2
        self.wrong_answer3=wrong_answer3
        self.count_right = 0
        self.tries = 0
    def got_right(self):
        self.tries+=1
        self.count_right+=1
        print("Правильна відповідь!")
    def got_wrong(self):
        self.tries+=1
        print("Неправильна відповідь.")


def rest():
    window_card.hide()
    sleep(sp_rest.value()*60)
    window_card.show()

def new_question():
    global cur_q
    shuffle(qs_list)
    cur_q=choice(qs_list)
    answers = [cur_q.answer, cur_q.wrong_answer1, cur_q.wrong_answer2, cur_q.wrong_answer3]
    shuffle(answers)
    lb_Correct.setText(cur_q.answer)
    lb_Question.setText(cur_q.question)
    rbtn_1.setText(answers[0])
    rbtn_2.setText(answers[1])
    rbtn_3.setText(answers[2])
    rbtn_4.setText(answers[3])

def check_result():
    for rbtn in rbtn_list:
        if rbtn.isChecked():
            if rbtn.text() == lb_Correct.text():
                cur_q.got_right()
                lb_Result.setText("Правильно!")
                rbtn.setChecked(False)
            else:
                cur_q.got_wrong()
                lb_Result.setText("Неправильно! Правильна відповідь:")
                rbtn.setChecked(False)

def switchscreen():
    if btn_next.text() == "Відповісти":
        RadioGroupBox.hide()
        AnsGroupBox.show()
        check_result()
        btn_next.setText("Наступне питання")
    else:
        RadioGroupBox.show()
        AnsGroupBox.hide()
        new_question()
        btn_next.setText("Відповісти")

def menu_generation():
    if cur_q.tries != 0:
        percent_result=(cur_q.count_right/cur_q.tries) * 100
    else: 
        percent_result=0
    text=f'Разів відповили: {cur_q.tries}\n'\
         f'Правильних відповідей: {cur_q.count_right}\n'\
         f'Успішність: {round(percent_result, 2)}%'
    stats.setText(text)
    menu_card.show()

def add_question():
    q=Question(ques_line.text(), correct_ans_line.text(), wrong_ans1_line.text(), wrong_ans2_line.text(), wrong_ans3_line.text())
    qs_list.append(q)
    ques_line.clear()
    correct_ans_line.clear()
    wrong_ans1_line.clear()
    wrong_ans2_line.clear()
    wrong_ans3_line.clear()

def clear_action():
    ques_line.clear()
    correct_ans_line.clear()
    wrong_ans1_line.clear()
    wrong_ans2_line.clear()
    wrong_ans3_line.clear()

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')
qs_list=[q1, q2, q3, q4]

new_question()
btn_next.clicked.connect(switchscreen)
btn_menu.clicked.connect(menu_generation)
addques.clicked.connect(add_question)
clear.clicked.connect(clear_action)
btn_rest.clicked.connect(rest)
app.exec_()