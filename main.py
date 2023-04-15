from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QLineEdit, QLineEdit, QPushButton, QWidget, QApplication,
QHBoxLayout, QVBoxLayout, QLabel, QMainWindow)
from random import randint

app = QApplication([])
window = QWidget()
QMainWindow.setWindowTitle(window, 'Рандомайзер') #установил название окна



int_label = QLabel('Введите числа в строки ниже')
int_from = QLineEdit()
int_from.setPlaceholderText('Введите число от')
int_before = QLineEdit()                            #добавил виджеты
int_before.setPlaceholderText('Введите число до')
button_gen = QPushButton('сгенерировать')



main_layout = QVBoxLayout()
second_layout = QHBoxLayout()
button_layout = QHBoxLayout()
label_layout = QHBoxLayout()

label_layout.addWidget(button_gen)
button_layout.addWidget(int_label)
label_layout.addLayout(button_layout)
second_layout.addLayout(label_layout)           #работа с лайаутами

main_layout.addLayout(second_layout)

main_layout.addWidget(int_from)
main_layout.addWidget(int_before)

window.setLayout(main_layout)



def generation(self):

    fromm = int_from.text()
    before = int_before.text()                                      #метод генерации чисел
    int_label.setText(str(randint(int(fromm), int(before))))
    
    

button_gen.clicked.connect(generation)

window.show()
app.exec()
