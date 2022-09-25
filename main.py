import PyQt6
from PyQt6 import QtDesigner, QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog
from PyQt6.QtGui import QPalette, QBrush, QPixmap, QPainter
from PyQt6 import QtGui
from PyQt6.QtCore import Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()


        self.setWindowTitle("Редактор текста")
        self.setGeometry(500, 250, 800, 500)



        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()



    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        fileMenu.addAction('Открыть', self.actions_clicked)
        fileMenu.addAction('Сохранить', self.actions_clicked)

    @QtCore.pyqtSlot()
    def actions_clicked(self):
        action = self.sender()
        if action.text() == 'Открыть':
            fname = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                print('No such file')
        elif action.text() == 'Сохранить':
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print('No such file')




def appliccation():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    appliccation()
