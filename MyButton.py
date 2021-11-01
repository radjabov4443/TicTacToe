from PyQt5.QtWidgets import QPushButton


class MyButton(QPushButton):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.setDisabled(True)
        self.setText(-1)

    def setText(self, text: int) -> None:
        if text == 1:
            super().setText("X")
            self.setDisabled(True)
        elif text == 0:
            super().setText("0")
            self.setDisabled(True)
        elif text == -1:
            super().setText("")
