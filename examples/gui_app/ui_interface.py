import sys

from PyQt5 import QtWidgets, uic

from average.using_function import average


class MyWindow(QtWidgets.QMainWindow):
    """
    Sample Window
    """

    def __init__(self):
        """
        constructor
        """
        super(MyWindow, self).__init__()
        uic.loadUi('sample.ui', self)
        self.values = self.findChild(QtWidgets.QTextEdit, 'valueBox')
        self.output = self.findChild(QtWidgets.QTextEdit, 'outputBox')
        self.calculate = self.findChild(QtWidgets.QPushButton, 'caculateButtom')
        self.calculate.clicked.connect(self.on_calculate)
        self.show()

    def on_calculate(self):
        """
        calculate average
        :return:
        """
        values = self.values.toPlainText().split(',')
        values = [int(value.strip()) for value in values]
        output = str(average(values))
        self.output.setPlainText(output)


def display_ui():
    """
    display gui
    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    app.exec_()

display_ui()
