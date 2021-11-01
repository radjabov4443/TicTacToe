import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QGridLayout, QRadioButton, QPushButton, qApp
from MyButton import MyButton


class mainWindow(QWidget):
    EXIT_CODE_REBOOT = -123

    def __init__(self):
        super().__init__()
        self.gamer = None
        self.start_btn = QPushButton("START")
        self.start_btn.setDisabled(True)
        self.player_x = QRadioButton("X")
        self.player_0 = QRadioButton("0")
        self.buttons = [MyButton(i) for i in range(9)]
        pos = [(i, j) for i in range(3) for j in range(3)]

        self.layout = QGridLayout()

        for btn, p in zip(self.buttons, pos):
            self.layout.addWidget(btn, *p)
            btn.clicked.connect(self.play)

        self.layout.addWidget(self.player_x, 4, 0)
        self.layout.addWidget(self.player_0, 4, 1)
        self.layout.addWidget(self.start_btn, 4, 2)

        self.player_x.toggled.connect(self.p_x)
        self.player_0.toggled.connect(self.p_0)
        self.start_btn.clicked.connect(self.start_game)

        self.setLayout(self.layout)
        self.show()

    def play(self):
        btn = self.sender()
        btn.setText(self.gamer)
        btn.setDisabled(True)
        self.gamer = not self.gamer
        self.wins()

    def wins(self):
        if self.buttons[0].text() == self.buttons[1].text() == self.buttons[2].text() != "":
            self.showDialog(self.buttons[0].text())
        elif self.buttons[3].text() == self.buttons[4].text() == self.buttons[5].text() != "":
            self.showDialog(self.buttons[3].text())
        elif self.buttons[6].text() == self.buttons[7].text() == self.buttons[8].text() != "":
            self.showDialog(self.buttons[6].text())
        elif self.buttons[0].text() == self.buttons[3].text() == self.buttons[6].text() != "":
            self.showDialog(self.buttons[0].text())
        elif self.buttons[1].text() == self.buttons[4].text() == self.buttons[7].text() != "":
            self.showDialog(self.buttons[1].text())
        elif self.buttons[2].text() == self.buttons[5].text() == self.buttons[8].text() != "":
            self.showDialog(self.buttons[2].text())
        elif self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text() != "":
            self.showDialog(self.buttons[0].text())
        elif self.buttons[2].text() == self.buttons[4].text() == self.buttons[6].text() != "":
            self.showDialog(self.buttons[2].text())
        
    def showDialog(self, player_win):
        self.player_win = player_win
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(f"{self.player_win} is wins this game")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.retry_game()
        else:
            sys.exit(app.exec_())

    @staticmethod
    def retry_game():
        qApp.exit(mainWindow.EXIT_CODE_REBOOT)

    def start_game(self):
        for i in range(len(self.buttons)):
            self.buttons[i].setDisabled(False)
        self.start_btn.setText("RETRY")
        self.start_btn.clicked.connect(self.retry_game)

    def p_x(self):
        self.start_btn.setDisabled(False)
        self.gamer = True

    def p_0(self):
        self.start_btn.setDisabled(False)
        self.gamer = False


if __name__ == '__main__':
    currentExitCode = mainWindow.EXIT_CODE_REBOOT
    while currentExitCode == mainWindow.EXIT_CODE_REBOOT:
        app = QApplication([])
        win = mainWindow()
        currentExitCode = app.exec_()
        app = None
