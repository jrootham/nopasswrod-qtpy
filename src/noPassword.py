import sys
from PySide2 import QtWidgets

from MailboxesWidget import MailboxesWidget
from ConnectWidget import ConnectWidget
from RegisterWidget import RegisterWidget
from LoginWidget import LoginWidget

class NoPasswordWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.mailboxes = MailboxesWidget()
        self.connect = ConnectWidget()
        self.register = RegisterWidget()
        self.login = LoginWidget()

        self.layout = QtWidgets.QVBoxLayout()

        self.layout.addWidget(self.mailboxes)
        self.layout.addWidget(self.connect)
        self.layout.addWidget(self.register)
        self.layout.addWidget(self.login)
        
        self.layout.insertStretch(-1)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = NoPasswordWidget()
    widget.resize(600, 800)
    widget.show()

    sys.exit(app.exec_())
