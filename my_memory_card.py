from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from PyQt5.QtGui import * 

from random import shuffle
class Question(): 
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer) # ответ 
    show_question() 

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Неверно!')

def next_question():
    window.cur_question = window.cur_question + 1 # переходим к следующему вопросу
    if window.cur_question >= len(questions_list):
        window.cur_question = 0 # если список вопросов закончился - идем сначала
    q = questions_list[window.cur_question] # взяли вопрос
    ask(q) # спросили

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer() # проверка ответа
    else:
        next_question() # следующий вопрос

questions_list = [] 
questions_list.append(Question('Государственный язык Королёва', 'Московский', 'Армянский', 'Марсианский', 'Китайский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(600,400)

window.cur_question = -1  

lb_Question = QLabel('В каком году была основана Москва?') # текст вопроса
lb_Question.setStyleSheet('background-color: lightcyan')
lb_Question.setFont(QFont("Times", 20, QFont.Bold))

btn_OK = QPushButton('Ответить') # кнопка ответа
btn_OK.setStyleSheet('background-color: LightGreen')
btn_OK.setFont(QFont('Times', 20))
RadioGroupBox = QGroupBox("Варианты ответов") 

rbtn_1 = QRadioButton('1147')
rbtn_1.setStyleSheet('font: 14pt Arial')
rbtn_2 = QRadioButton('1242')
rbtn_2.setStyleSheet('font: 14pt Arial')
rbtn_3 = QRadioButton('1861')
rbtn_3.setStyleSheet('font: 14pt Arial')
rbtn_4 = QRadioButton('1943')
rbtn_4.setStyleSheet('font: 14pt Arial')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1)

# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=3) # кнопка должна быть большой
layout_line3.addStretch(1)

# Теперь созданные строки разместим друг под другом:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=7)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

window.setLayout(layout_card)

btn_OK.clicked.connect(click_OK)
next_question()
window.show()
app.exec_()


