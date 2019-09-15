import sys
from PyQt5.QtWidgets import *
import pymysql.cursors
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot


class Register(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Register'  # Window Title
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(260, 100, 795, 525)  # Window Size
        self.setStyleSheet(
            'QPushButton,QLabel,QLineEdit {font: 10pt Doppio One}')  # Changes Font for Whole Window for QPushButton, QLabel, and QlineEdit
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon(r'C:\Users\XcomPh\Desktop\New folder (2)\ProjectDanas\Media Files\winicon.png'))

        # Background
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'C:\Users\XcomPh\Desktop\New folder (2)\ProjectDanas\Media Files\winbackground.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(0, 0)
        self.BackgroundHolder.resize(795, 525)
        self.BackgroundHolder.setScaledContents(True)

        # RegisterDanasImage
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'C:\Users\XcomPh\Desktop\New folder (2)\ProjectDanas\Media Files\danaswinicon.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(325, 0)
        self.BackgroundHolder.resize(150, 150)
        self.BackgroundHolder.setScaledContents(True)

        # MidFrameRegister
        self.frame1 = QFrame(self)
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setStyleSheet("background-color:  #2A363B")
        self.frame1.setGeometry(310, 150, 180, 2)

        # REGISTER Label
        self.regLabel = QLabel('REGISTER', self)
        self.regLabel.setStyleSheet("QLabel{"
                                    "font: 15pt Doppio One;"
                                    "color: #ffffff;}"
                                    );
        self.regLabel.move(360, 165)

        # Create Username box
        self.usernamebox = QLineEdit(self)
        self.usernamebox.setStyleSheet("QLineEdit{ "
                                       "border: 2px white;"
                                       "border-radius: 5px;"
                                       "padding: 0 8px;"
                                       "font-size: 12px;}"
                                       "QLineEdit:focus { "
                                       "background-color:rgb(0 0, 0,0);}"
                                       );
        self.usernamebox.move(365, 212)
        self.usernamebox.resize(165, 20)
        self.usernamebox.setMaxLength(15)

        # Username Label
        self.usernamelabel = QLabel(self)
        self.usernamelabel.setStyleSheet('color: #ffffff')
        self.usernamelabel.setText('Username:')
        self.usernamelabel.move(291, 213)

        # ---------------------PASSWORD SECTION-----------------------------------------

        # Create Password box
        self.password = QLineEdit(self)
        self.password.setStyleSheet("QLineEdit{ "
                                    "border: 2px white;"
                                    "border-radius: 5px;"
                                    "padding: 0 8px;"
                                    "font-size: 12px;}"
                                    "QLineEdit:focus { "
                                    "background-color:rgb(0 0, 0,0);}"
                                    );
        self.password.setEchoMode(QLineEdit.Password)
        self.password.move(365, 250)
        self.password.resize(165, 20)
        self.password.setMaxLength(15)

        # Password Label
        self.passLabel = QLabel(self)
        self.passLabel.setStyleSheet('color: #ffffff')
        self.passLabel.setText('Password:')
        self.passLabel.move(291, 252)

        # Confirm password
        self.conpassword = QLineEdit(self)
        self.conpassword.setStyleSheet("QLineEdit{ "
                                       "border: 2px white;"
                                       "border-radius: 5px;"
                                       "padding: 0 8px;"
                                       "font-size: 12px;}"
                                       "QLineEdit:focus { "
                                       "background-color:rgb(0 0, 0,0);}"
                                       );
        self.conpassword.setEchoMode(QLineEdit.Password)
        self.conpassword.move(410, 288)
        self.conpassword.resize(120, 20)
        self.conpassword.setMaxLength(15)

        # Confirm Password Label
        self.conpassLabel = QLabel(self)
        self.conpassLabel.setStyleSheet('color: #ffffff')
        self.conpassLabel.setText('Confirm Password:')
        self.conpassLabel.move(291, 291)

        # Register Button
        self.registerbutton = QPushButton('Register', self)
        self.registerbutton.setStyleSheet("QPushButton{ border: 2px solid #e6e6ff; border-radius: 10px;"
                                          "color: #ffccdd;"
                                          "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #EA485F, stop: 1 #EA485F);"
                                          "min-width: 80px;}"
                                          )
        self.registerbutton.move(445, 335)



        # Registerbuttonconnection MUST CREATE A FUCNTION FIRST FOR REGISTER WIDGET  self.registerbutton.clicked.connect(self.Register)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Register()
    sys.exit(app.exec_())
