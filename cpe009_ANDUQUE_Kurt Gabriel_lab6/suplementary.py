import sys
import math
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QWidget, QGridLayout, QLineEdit,
    QPushButton, QAction, QMessageBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.setGeometry(300, 300, 400, 400)
        self.initUI()
        self.history_file = "calculator_history.txt"

    def initUI(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.grid = QGridLayout(self.central_widget)
        self.central_widget.setLayout(self.grid)

        self.textLine = QLineEdit(self)
        self.textLine.setReadOnly(False)
        self.textLine.setFont(QFont('Arial', 20))
        self.grid.addWidget(self.textLine, 0, 0, 1, 0)

        names = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sin',
            '1', '2', '3', '-', 'cos',
            '0', '.', '=', '+', 'exp'
        ]

        positions = [(i, j) for i in range(1, 6) for j in range(5)]
        for position, name in zip(positions, names):
            button = QPushButton(name)
            button.setFont(QFont('Arial', 14))
            button.setFixedSize(QSize(60, 40))
            button.clicked.connect(self.on_button_clicked)
            self.grid.addWidget(button, *position)

        self.load_menu()

    def load_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')

        clear_history_action = QAction('Clear History', self)
        clear_history_action.triggered.connect(self.clear_history)
        fileMenu.addAction(clear_history_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')  # Set shortcut for exiting
        fileMenu.addAction(exit_action)

    def on_button_clicked(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == 'C':
            self.textLine.clear()
        elif button_text == '=':
            self.calculate_result()
        elif button_text in ['sin', 'cos', 'exp']:
            self.perform_trig_or_exp(button_text)
        else:
            current_text = self.textLine.text()
            new_text = current_text + button_text
            self.textLine.setText(new_text)

    def calculate_result(self):
        expression = self.textLine.text()
        try:
            result = eval(expression)
            self.textLine.setText(str(result))
            self.save_to_history(f"{expression} = {result}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid Expression: {str(e)}")

    def perform_trig_or_exp(self, operation):
        try:
            value = float(self.textLine.text())
            if operation == 'sin':
                result = math.sin(math.radians(value))
            elif operation == 'cos':
                result = math.cos(math.radians(value))
            elif operation == 'exp':
                result = math.exp(value)
            self.textLine.setText(str(result))
            self.save_to_history(f"{operation}({value}) = {result}")
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter a valid number.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def save_to_history(self, entry):
        with open(self.history_file, 'a') as f:
            f.write(entry + '\n')

    def clear_history(self):
        try:
            with open(self.history_file, 'w') as f:
                f.truncate()
            QMessageBox.information(self, "Success", "History cleared.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
