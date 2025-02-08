from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
app = QApplication([])
menu_card = QWidget()
menu_card.resize(400, 300)
menu_card.move(760, 350)

mainmenu_layout=QVBoxLayout()
layout_textmain=QHBoxLayout()
layout_1=QVBoxLayout()
layout_2=QVBoxLayout()
layout_btn=QHBoxLayout()

ques=QLabel("Питання:")
ques_line=QLineEdit()
correct_ans=QLabel("Правильна відповідь:")
correct_ans_line=QLineEdit()
wrong_ans1=QLabel("Перша хибна відповідь:")
wrong_ans1_line=QLineEdit()
wrong_ans2=QLabel("Друга хибна відповідь:")
wrong_ans2_line=QLineEdit()
wrong_ans3=QLabel("Третя хибна відповідь:")
wrong_ans3_line=QLineEdit()

textstat=QLabel("Статистика")
textstat.setStyleSheet('font-size: 19px; font-weight: bold;')
stats=QLabel()


addques=QPushButton("Додати питання")
clear=QPushButton("Очистити")

layout_1.addWidget(ques)
layout_1.addWidget(correct_ans)
layout_1.addWidget(wrong_ans1)
layout_1.addWidget(wrong_ans2)
layout_1.addWidget(wrong_ans3)

layout_2.addWidget(ques_line)
layout_2.addWidget(correct_ans_line)
layout_2.addWidget(wrong_ans1_line)
layout_2.addWidget(wrong_ans2_line)
layout_2.addWidget(wrong_ans3_line)

layout_btn.addWidget(addques)
layout_btn.addWidget(clear)

layout_textmain.addLayout(layout_1)
layout_textmain.addLayout(layout_2)
mainmenu_layout.addLayout(layout_textmain)
mainmenu_layout.addLayout(layout_btn)
mainmenu_layout.addWidget(textstat)
mainmenu_layout.addWidget(stats)

menu_card.setLayout(mainmenu_layout)