import sys
from PyQt5.QtWidgets import *
from zmq import NULL
from db import instructors


class University(QWidget):
    def __init__(self):
        super().__init__()
        # setting up window properties
        self.title = f'University {instructors}'
        """ self.left = 0
        self.top = 0
        self.right = 0
        self.bottom = 0 """

        self.show()  # showing the window


if __name__ == '__main__':
    app = QApplication(sys.argv)

    i = University()

    sys.exit(app.exec_())
