from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QMessageBox)

app = QApplication([])
main_win = QWidget()
main_win.resize(400, 400)
main_win.setWindowTitle('Crazy People')

def box():
    win2 = QMessageBox()
    win2.setWindowTitle('!')
    win2.setText('Only numbers')
    win2.exec()

#main_win.show()
#app.exec_()
