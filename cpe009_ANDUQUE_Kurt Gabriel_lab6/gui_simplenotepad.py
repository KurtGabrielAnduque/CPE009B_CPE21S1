import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notepad")
        self.setWindowIcon(QIcon("pythonico.ico"))
        self.loadMenu()
        self.loadWidget()
        self.show()

    def loadMenu(self):
        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")

        editButton = QAction("Clear", self)
        editButton.setShortcut("Ctrl+N")
        editButton.triggered.connect(self.clearText)
        editMenu.addAction(editButton)

        fontButton = QAction("Font", self)
        fontButton.setShortcut("Ctrl+D")
        fontButton.triggered.connect(self.showFontDialog)
        editMenu.addAction(fontButton)

        saveButton = QAction("Save", self)
        saveButton.setShortcut("Ctrl+S")
        saveButton.triggered.connect(self.saveFileDialog)
        fileMenu.addAction(saveButton)

        openButton = QAction("Open", self)
        openButton.setShortcut("Ctrl+O")
        openButton.triggered.connect(self.openFileNameDialog)
        fileMenu.addAction(openButton)

        exitButton = QAction("Exit", self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.setStatusTip("Exit application")
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.notepad.text.setFont(font)

    def loadWidget(self):
        self.notepad = Notepad()
        self.setCentralWidget(self.notepad)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Save Notepad File", "","Text Files (*.txt);;Python Files (*.py);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.notepad.text.toPlainText())

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Notepad File", "",
                                                  "Text Files (*.txt);;Python Files (*.py);;All Files (*)",
                                                  options=options)
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.notepad.text.setText(data)

    def clearText(self):
        self.notepad.text.clear()


class Notepad(QWidget):
    def __init__(self):
        super(Notepad, self).__init__()
        self.text = QTextEdit(self)
        self.clearbtn = QPushButton("Clear")
        self.clearbtn.clicked.connect(self.cleartext)

        self.initUI()

    def initUI(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.clearbtn)

        self.horizontalGroupBox.setLayout(self.layout)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

    def cleartext(self):
        self.text.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
