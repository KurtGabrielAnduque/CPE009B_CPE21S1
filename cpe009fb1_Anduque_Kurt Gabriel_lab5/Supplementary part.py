import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot


class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("~Account Registration~")
        self.setGeometry(200, 200, 500, 350)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.initUI()

    def initUI(self):

        self.setStyleSheet("background-color: #f5f5f5;")

        main_layout = QVBoxLayout()
        form_layout = QVBoxLayout()

        self.first_name_label = QLabel("First Name:")
        self.first_name_label.setStyleSheet("color: #2c3e50; font-size: 14px;")
        self.first_name_input = QLineEdit(self)
        self.first_name_input.setStyleSheet(
            "background-color: #ecf0f1; border-radius: 5px; padding: 10px; font-size: 14px;")

        self.last_name_label = QLabel("Last Name:")
        self.last_name_label.setStyleSheet("color: #2c3e50; font-size: 14px;")
        self.last_name_input = QLineEdit(self)
        self.last_name_input.setStyleSheet(
            "background-color: #ecf0f1; border-radius: 5px; padding: 10px; font-size: 14px;")

        self.username_label = QLabel("Username:")
        self.username_label.setStyleSheet("color: #2c3e50; font-size: 14px;")
        self.username_input = QLineEdit(self)
        self.username_input.setStyleSheet(
            "background-color: #ecf0f1; border-radius: 5px; padding: 10px; font-size: 14px;")

        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet("color: #2c3e50; font-size: 14px;")
        self.password_input = QLineEdit(self)
        self.password_input.setStyleSheet(
            "background-color: #ecf0f1; border-radius: 5px; padding: 10px; font-size: 14px;")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.email_label = QLabel("Email Address:")
        self.email_label.setStyleSheet("color: #2c3e50; font-size: 14px;")
        self.email_input = QLineEdit(self)
        self.email_input.setStyleSheet("background-color: #ecf0f1; border-radius: 5px; padding: 10px; font-size: 14px;")

        self.contact_label = QLabel("Contact No.:")
        self.contact_label.setStyleSheet("color: #2c3e50; font-size: 14px;")
        self.contact_input = QLineEdit(self)
        self.contact_input.setStyleSheet(
            "background-color: #ecf0f1; border-radius: 5px; padding: 10px; font-size: 14px;")

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setStyleSheet(
            "background-color: #1abc9c; color: white; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.submit_button.clicked.connect(self.register_account)

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setStyleSheet(
            "background-color: #e74c3c; color: white; padding: 10px 20px; border-radius: 5px; font-size: 16px;")
        self.clear_button.clicked.connect(self.clear_all)

        form_layout.addWidget(self.first_name_label)
        form_layout.addWidget(self.first_name_input)
        form_layout.addWidget(self.last_name_label)
        form_layout.addWidget(self.last_name_input)
        form_layout.addWidget(self.username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.email_label)
        form_layout.addWidget(self.email_input)
        form_layout.addWidget(self.contact_label)
        form_layout.addWidget(self.contact_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.clear_button)

        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        self.show()

    def clear_all(self):
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.email_input.clear()
        self.contact_input.clear()

    @pyqtSlot()
    def register_account(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()
        contact = self.contact_input.text()

        if not all([first_name, last_name, username, password, email, contact]):
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        try:
            with open("accounts.txt", "a") as file:
                file.write(f"First Name: {first_name}\n")
                file.write(f"Last Name: {last_name}\n")
                file.write(f"Username: {username}\n")
                file.write(f"Password: {password}\n")
                file.write(f"Email: {email}\n")
                file.write(f"Contact No.: {contact}\n")
                file.write("----\n")

            QMessageBox.information(self, "Success", "Account successfully registered!")
            self.clear_all()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Registration failed: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationForm()
    sys.exit(app.exec_())