from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox
from memo___app import *
card_width, card_height = 600, 500

window_card = QWidget()

window_card.resize(card_width, card_height)

window_card.move(650, 250)


window_card.setWindowTitle("Memory card")
menu_card.setWindowTitle("Menu")

btn_menu = QPushButton("Меню")# меню
btn_next = QPushButton("Відповісти")# відповісти
btn_rest = QPushButton("Відпочити") # відпочити
sp_rest = QSpinBox() 

lb_Question = QLabel('Яблуко') # текст питання

#Панель з варіантами:
RadioGroupBox = QGroupBox("Варіанти відповіді") #група на екрані для перемикачів із відповідями
RadioGroup = QButtonGroup() #а це для угруповання перемикачів, щоб керувати їхньою поведінкою


rbtn_1 = QRadioButton('caterpillar')
rbtn_2 = QRadioButton('apple')
rbtn_3 = QRadioButton('application')
rbtn_4 = QRadioButton('building')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


#Панель із результатом:
AnsGroupBox = QGroupBox("Результат тесту")
lb_Result = QLabel('Правильно: ') #тут розміщується напис "правильно" або "неправильно"
lb_Correct = QLabel('apple') #тут буде написано текст правильної відповіді

# Тепер займаємося розміщенням:
# Розміщуємо варіанти відповідей у два стовпці всередині групи:
layout_ans1 = QHBoxLayout()  
layout_ans2 = QVBoxLayout() # вертикальні будуть усередині горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # дві відповіді у перший стовпець
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # дві відповіді у другий стовпець
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # розмістили стовпці в одному рядку
RadioGroupBox.setLayout(layout_ans1) # готова "панель" з варіантами відповідей 

# розміщуємо результат:
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# розміщуємо всі віджети у вікні, вони розташовані в чотири рядки:
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1) # розрив між кнопками робимо по можливості довшим
layout_line1.addWidget(btn_rest)
layout_line1.addWidget(sp_rest)
layout_line1.addWidget(QLabel('хвилин')) # нам не потрібна змінна для цього напису

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_next, stretch=2) # кнопка має бути великою
layout_line4.addStretch(1)

# Тепер створені 4 рядки розмістимо один під одним:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # прогалини між вмістом

window_card.setLayout(layout_card)
window_card.show()