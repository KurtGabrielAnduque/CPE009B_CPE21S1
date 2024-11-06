import sys
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QApplication


class GridExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # Button names for the calculator
        names = [
            '7', '8', '9', '/', '4',
            '5', '6', '*', '1', '2',
            '3', '-', '0', '.', '=', '+'
        ]

        # Text line for displaying input/output
        self.textline = QLineEdit(self)
        grid.addWidget(self.textline, 0, 0, 1, 5)

        # Using a loop to generate button positions
        positions = [(i, j) for i in range(1, 5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Grid Layout')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GridExample()
    sys.exit(app.exec_())
