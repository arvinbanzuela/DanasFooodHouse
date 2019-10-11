import sys
import pymysql.cursors
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# Test of git using different proxy
# Login Window
class Login(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Login'  # Window Title
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(260, 100, 795, 525)  # Window Size
        self.setStyleSheet(
            'QPushButton,QLabel,QLineEdit {font: 10pt Doppio One}')  # Changes Font for Whole Window for QPushButton, QLabel, and QlineEdit
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon(r'Media Files\danaswinicon.png'))

        # Background
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'Media Files\winbackground.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(0, 0)
        self.BackgroundHolder.resize(795, 525)
        self.BackgroundHolder.setScaledContents(True)

        # LoginDanasImage
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'Media Files\danaswinicon.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(175, 120)
        self.BackgroundHolder.resize(200, 200)
        self.BackgroundHolder.setScaledContents(True)

        # MidFrameLogin
        self.frame1 = QFrame(self)
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setStyleSheet("background-color:  #2A363B")
        self.frame1.setGeometry(400, 145, 2, 180)

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
        self.usernamebox.move(505, 197)
        self.usernamebox.resize(120, 20)
        self.usernamebox.setMaxLength(15)

        # Username Label
        self.usernamelabel = QLabel(self)
        self.usernamelabel.setStyleSheet('color: #ffffff')
        self.usernamelabel.setText('Username:')
        self.usernamelabel.move(437, 193)

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
        self.password.move(505, 235)
        self.password.resize(120, 20)
        self.password.setMaxLength(15)

        # Password Label
        self.passLabel = QLabel(self)
        self.passLabel.setStyleSheet('color: #ffffff')
        self.passLabel.setText('Password:')
        self.passLabel.move(441, 229)

        # Register Button
        self.registerbutton = QPushButton('Register', self)
        self.registerbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                          "color: #ffffff;"
                                          "background-color: rgba(51, 0, 16,100);"
                                          "min-height: 30px; min-width: 60;}"
                                          "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                          "background-color: rgba(255, 0, 81,100);}"
                                          "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                          "background-color: rgba(153, 153, 153,80);}"
                                          )
        self.registerbutton.move(460, 275)
        self.registerbutton.clicked.connect(self.Register)

        # Registerbuttonconnection MUST CREATE A FUCNTION FIRST FOR REGISTER WIDGET  self.registerbutton.clicked.connect(self.Register)

        # Login Button
        self.loginbutton = QPushButton('Login', self)
        self.loginbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                       "color: #ffffff;"
                                       "background-color: rgba(51, 0, 16,100);"
                                       "min-height: 30px; min-width: 60;}"
                                       "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(255, 0, 81,100);}"
                                       "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(153, 153, 153,80);}"
                                       )
        self.loginbutton.move(575, 275)
        self.loginbutton.clicked.connect(self.Login)
        self.show()

    def Register(self):
        self.newWindow = Register()
        self.newWindow.show()
        self.hide()

    def Login(self):
        Username1 = self.usernamebox.text()
        Password1 = self.password.text()
        Notblank = True
        if (len(Username1) == 0 or len(Password1) == 0):
            Notblank = False
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Information)
            self.msgbox.setText("Please do not leave an empty field")
            self.msgbox.setWindowTitle("Cannot Log in!")
            self.msgbox.show()

        if (Notblank):
            connection = pymysql.connect(host='localhost',
                                         user='danasuser',
                                         password='bunny47love',
                                         db='danasdb',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         port=3306)
            with connection.cursor() as cursor:
                result = cursor.callproc('usplogin',
                                        (Username1, Password1))
                if (result == 0):
                    self.msgbox = QMessageBox()
                    self.msgbox.setIcon(QMessageBox.Information)
                    self.msgbox.setText("Invalid Account!")
                    self.msgbox.setWindowTitle("Cannot Log in!")
                    self.msgbox.show()

                else:

                    global loginaccount
                    loginaccount = Username1
                    self.newWindow = Inventory()
                    self.newWindow.show()
                    self.hide()


# ------------------------------------Register Window-------------------------------
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
        self.setWindowIcon(QIcon(r'Media Files\winicon.png'))

        # Background
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'Media Files\winbackground.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(0, 0)
        self.BackgroundHolder.resize(795, 525)
        self.BackgroundHolder.setScaledContents(True)

        # RegisterDanasImage
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'Media Files\danaswinicon.png')
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
        self.registerbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                          "color: #ffffff;"
                                          "background-color: rgba(51, 0, 16,100);"
                                          "min-height: 30px; min-width: 60;}"
                                          "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                          "background-color: rgba(255, 0, 81,100);}"
                                          "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                          "background-color: rgba(153, 153, 153,80);}"
                                          )
        self.registerbutton.move(445, 335)
        self.registerbutton.clicked.connect(self.Register)

        # Back Button to Main Menu
        self.loginbackbutton = QPushButton('Back to Log in', self)
        self.loginbackbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                           "color: #ffffff;"
                                           "background-color: rgba(51, 0, 16,100);"
                                           "min-height: 30px; min-width: 70;}"
                                           "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                           "background-color: rgba(255, 0, 81,100);}"
                                           "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                           "background-color: rgba(153, 153, 153,80);}"
                                           )
        self.loginbackbutton.move(290, 335)
        self.loginbackbutton.clicked.connect(self.Back)
        # Back Button Function
        self.show()

    # ----------Backbuttonconnection------------------
    def Back(self):
        self.newWindow = Login()
        self.newWindow.show()
        self.hide()

    # -------ErrorHandling-Continue-------------------
    def Register(self):
        Username = self.usernamebox.text()
        Password = self.password.text()
        ConfirmPassword = self.conpassword.text()
        accountinfo = (Username, Password, ConfirmPassword)
        NotBlank = True
        for i in accountinfo:
            if (len(i) == 0):
                NotBlank = False

                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Information)
                self.msgbox.setText("Do not leave empty field")
                self.msgbox.setWindowTitle("Failed to register!")
                self.msgbox.show()

                break

        if (NotBlank):
            if (len(Username) < 5):
                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Information)
                self.msgbox.setText("Username must be atleast 5 characters")
                self.msgbox.setWindowTitle("Failed to register!")
                self.msgbox.show()
            elif (len(Password) < 5):
                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Information)
                self.msgbox.setText("Password must be atleast 5 characters")
                self.msgbox.setWindowTitle("Failed to register!")
                self.msgbox.show()
            elif (Password != ConfirmPassword):
                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Information)
                self.msgbox.setText("Password do not match")
                self.msgbox.setWindowTitle("Failed to register!")
                self.msgbox.show()
            else:
                connection = pymysql.connect(host='localhost',
                                             user='danasuser',
                                             password='bunny47love',
                                             db='danasdb',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor,
                                             port=3306)
                with connection.cursor() as cursor:
                    result = cursor.execute('Select * from accounts where Username = %s;', (Username))
                    if (result == 1):
                        self.msgbox = QMessageBox()
                        self.msgbox.setIcon(QMessageBox.Information)
                        self.msgbox.setText("Account already exist")
                        self.msgbox.setWindowTitle("Error!")
                        self.msgbox.show()

                    elif (result == 0):
                        connection = pymysql.connect(host='localhost',
                                                     user='danasuser',
                                                     password='bunny47love',
                                                     db='danasdb',
                                                     charset='utf8mb4',
                                                     cursorclass=pymysql.cursors.DictCursor,
                                                     port=3306)
                        with connection.cursor() as cursor:
                            cursor.execute('insert into accounts values(%s,%s);', (Username, Password))
                            connection.commit()
                            self.msgbox = QMessageBox()
                            self.msgbox.setIcon(QMessageBox.Information)
                            self.msgbox.setText("Registration complete successfully!")
                            self.msgbox.setWindowTitle("Success!")
                            self.msgbox.show()
                            self.newWindow = Register()
                            self.newWindow.show()
                            self.hide()

        # Registerbuttonconnection MUST CREATE A FUCNTION FIRST FOR REGISTER WIDGET  self.registerbutton.clicked.connect(self.Register)


class Inventory(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'DANAS-INVENTORY'  # Window Title
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(260, 100, 795, 525)  # Window Size
        self.setStyleSheet(
            'QPushButton,QLabel,QLineEdit {font: 10pt Doppio One}')  # Changes Font for Whole Window for QPushButton, QLabel, and QlineEdit
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon(r'Media Files\winicon.png'))

        # Background
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'Media Files\winbackground.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(0, 0)
        self.BackgroundHolder.resize(795, 525)
        self.BackgroundHolder.setScaledContents(True)

        # -------------DATA TABLE QTABLEWIDGET----------------
        # Connects Python to Mysql

        # ----------------------FRAME SECTION -------------------------------------------

        # CREATE-FRAME-AND-ICON------------------------------------------------------------------------------------------

        self.createframe = QFrame(self)
        self.createframe.setFrameShape(QFrame.StyledPanel)
        self.createframe.setStyleSheet("background-color: rgba(84, 15, 53, 100);")
        self.createframe.setGeometry(5, 30, 790, 50)

        self.createframe = QFrame(self)
        self.createframe.setFrameShape(QFrame.StyledPanel)
        self.createframe.setStyleSheet("background-color: rgba(244, 190, 219, 0);")
        self.createframe.setGeometry(5, 30, 790, 490)

        # ADD--FRAME------------------------------------------------------------------------------------------
        self.addframe = QFrame(self)
        self.addframe.setFrameShape(QFrame.StyledPanel)
        self.addframe.setStyleSheet("background-color: #540f35;")
        self.addframe.setGeometry(465, 90, 160, 300)

        # DELETE--FRAME------------------------------------------------------------------------------------------

        self.deleteframe = QFrame(self)
        self.deleteframe.setFrameShape(QFrame.StyledPanel)
        self.deleteframe.setStyleSheet("background-color:  #540f35")
        self.deleteframe.setGeometry(520, 400, 220, 75)

        # DELETE--FRAME------------------------------------------------------------------------------------------

        # Update------Frame
        self.updateframe = QFrame(self)
        self.updateframe.setFrameShape(QFrame.StyledPanel)
        self.updateframe.setStyleSheet("background-color: #540f35;")
        self.updateframe.setGeometry(630, 90, 160, 300)

        # ----------------------END OF FRAME SECTION -------------------------------------------

        # ----------------------INSIDE FRAME CONTENTS -CRUD-------------------------------------

        # -------SETS OF LABELS--------------------------------------------------------------

        # -------CREATE LABELS AND QLINEEDIT ----------------
        self.createlabel = QLabel('Add Products', self)
        self.createlabel.setStyleSheet("QLabel{"
                                       "font: 12pt Doppio One;"
                                       "color: #ffffff;}"
                                       );
        self.createlabel.move(495, 95)

        self.prodcodelabel = QLabel('Product Code: ', self)
        self.prodcodelabel.setStyleSheet("QLabel{"
                                         "font: 10pt Doppio One;"
                                         "color: #ffffff;}"
                                         );
        self.prodcodelabel.move(470, 140)

        self.prodcodebox = QLineEdit(self)
        self.prodcodebox.setStyleSheet("QLineEdit{ "
                                       "border: 2px white;"
                                       "border-radius: 5px;"
                                       "padding: 0 8px;"
                                       "font-size: 12px;}"
                                       "QLineEdit:focus { "
                                       "background-color:rgb(0 0, 0,0);}"
                                       );
        self.prodcodebox.move(470, 165)
        self.prodcodebox.resize(150, 20)
        self.prodcodebox.setMaxLength(15)

        self.prodnamelabel = QLabel('Product Name: ', self)
        self.prodnamelabel.setStyleSheet("QLabel{"
                                         "font: 10pt Doppio One;"
                                         "color: #ffffff;}"
                                         );
        self.prodnamelabel.move(470, 190)

        self.prodnamebox = QLineEdit(self)
        self.prodnamebox.setStyleSheet("QLineEdit{ "
                                       "border: 2px white;"
                                       "border-radius: 5px;"
                                       "padding: 0 8px;"
                                       "font-size: 12px;}"
                                       "QLineEdit:focus { "
                                       "background-color:rgb(0 0, 0,0);}"
                                       );
        self.prodnamebox.move(470, 215)
        self.prodnamebox.resize(150, 20)
        self.prodnamebox.setMaxLength(15)

        self.prodqtylabel = QLabel('QTY: ', self)
        self.prodqtylabel.setStyleSheet("QLabel{"
                                        "font: 10pt Doppio One;"
                                        "color: #ffffff;}"
                                        );
        self.prodqtylabel.move(470, 240)

        self.prodqtybox = QLineEdit(self)
        self.prodqtybox.setStyleSheet("QLineEdit{ "
                                      "border: 2px white;"
                                      "border-radius: 5px;"
                                      "padding: 0 8px;"
                                      "font-size: 12px;}"
                                      "QLineEdit:focus { "
                                      "background-color:rgb(0 0, 0,0);}"
                                      );
        self.prodqtybox.move(470, 265)
        self.prodqtybox.resize(150, 20)
        self.prodqtybox.setMaxLength(15)
        self.prodqtybox.setValidator(QIntValidator(0,999))

        self.prodpricelabel = QLabel('Product Price: ', self)
        self.prodpricelabel.setStyleSheet("QLabel{"
                                          "font: 10pt Doppio One;"
                                          "color: #ffffff;}"
                                          );
        self.prodpricelabel.move(470, 290)

        self.prodpricebox = QLineEdit(self)
        self.prodpricebox.setStyleSheet("QLineEdit{ "
                                        "border: 2px white;"
                                        "border-radius: 5px;"
                                        "padding: 0 8px;"
                                        "font-size: 12px;}"
                                        "QLineEdit:focus { "
                                        "background-color:rgb(0 0, 0,0);}"
                                        );
        self.prodpricebox.move(470, 315)
        self.prodpricebox.resize(150, 20)
        self.prodpricebox.setMaxLength(15)
        self.prodpricebox.setValidator(QIntValidator(0,999))

        # ----------------DELETE-------

        self.deletelabel = QLabel('Delete Products', self)
        self.deletelabel.setStyleSheet("QLabel{"
                                       "font: 11pt Doppio One;"
                                       "color: #ffffff;}"
                                       );
        self.deletelabel.move(585, 405)

        self.deleteprodlabel = QLabel('Product Code: ', self)
        self.deleteprodlabel.setStyleSheet("QLabel{"
                                           "font: 10pt Doppio One;"
                                           "color: #ffffff;}"
                                           );
        self.deleteprodlabel.move(525, 430)

        self.deleteprodbox = QLineEdit(self)
        self.deleteprodbox.setStyleSheet("QLineEdit{ "
                                         "border: 2px white;"
                                         "border-radius: 5px;"
                                         "padding: 0 8px;"
                                         "font-size: 12px;}"
                                         "QLineEdit:focus { "
                                         "background-color:rgb(0 0, 0,0);}"
                                         );
        self.deleteprodbox.move(525, 450)
        self.deleteprodbox.resize(125, 20)
        self.deleteprodbox.setMaxLength(15)

        self.deletebutton = QPushButton('', self)
        self.deletebutton.setIcon(QtGui.QIcon(r'Media Files\delete-8x.png'))
        self.deletebutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                        "color: #ffffff;"
                                        "background-color: rgba(51, 0, 16,100);"
                                        "min-height: 30px; min-width: 60;}"
                                        "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                        "background-color: rgba(255, 0, 81,100);}"
                                        "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                        "background-color: rgba(153, 153, 153,80);}"
                                        )
        self.deletebutton.move(660, 437.5)
        self.deletebutton.setToolTip('Click to delete product')
        self.deletebutton.clicked.connect(self.Delete)

        # ----------------------
        self.addbutton1 = QPushButton('Add Product', self)
        self.addbutton1.setIcon(QtGui.QIcon(r'Media Files\plus-8x.png'))
        self.addbutton1.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                      "color: #ffffff;"
                                      "background-color: rgba(51, 0, 16,100);"
                                      "min-height: 30px; min-width: 100;}"
                                      "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                      "background-color: rgba(255, 0, 81,100);}"
                                      "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                      "background-color: rgba(153, 153, 153,80);}"
                                      )

        self.addbutton1.move(493, 347)
        self.addbutton1.setToolTip('Click to add product')
        self.addbutton1.clicked.connect(self.Add)

        # ---------VIEW LABELS AND QLINEEDIT ----------------

        # ----LOG OUT ----
        # UPDATE LABEL -----------------

        self.updatelabel = QLabel('Update Products', self)
        self.updatelabel.setStyleSheet("QLabel{"
                                       "font: 12pt Doppio One;"
                                       "color: #ffffff;}"
                                       );
        self.updatelabel.move(647, 95)

        self.updateprodlabel = QLabel('Product Code: ', self)
        self.updateprodlabel.setStyleSheet("QLabel{"
                                           "font: 10pt Doppio One;"
                                           "color: #ffffff;}"
                                           );
        self.updateprodlabel.move(635, 140)

        self.updateprodbox = QLineEdit(self)
        self.updateprodbox.setStyleSheet("QLineEdit{ "
                                         "border: 2px white;"
                                         "border-radius: 5px;"
                                         "padding: 0 8px;"
                                         "font-size: 12px;}"
                                         "QLineEdit:focus { "
                                         "background-color:rgb(0 0, 0,0);}"
                                         );
        self.updateprodbox.move(635, 165)
        self.updateprodbox.resize(150, 20)
        self.updateprodbox.setMaxLength(15)

        self.selectupdatelabel = QLabel('Update select: ', self)
        self.selectupdatelabel.setStyleSheet("QLabel{"
                                             "font: 10pt Doppio One;"
                                             "color: #ffffff;}"
                                             );
        self.selectupdatelabel.move(635, 190)

        self.selectupdatebox = QComboBox(self)
        self.selectupdatebox.setGeometry(635, 215, 150, 20)
        self.selectupdatebox.setStyleSheet("QComboBox{ "
                                           "border: 2px white;"
                                           "border-radius: 5px;"
                                           "padding: 0 8px;"
                                           "font-size: 12px;}"
                                           "QLineEdit:focus { "
                                           "background-color:rgb(0 0, 0,0);}"
                                           );
        self.selectupdatebox.addItem('...')
        self.selectupdatebox.addItem('Product Name')
        self.selectupdatebox.addItem('Quantity')
        self.selectupdatebox.addItem('Price')
        self.selectupdatebox.activated.connect(self.UpdatedValue)

        self.updatedvaluelabel = QLabel('Updated Value: ', self)
        self.updatedvaluelabel.setStyleSheet("QLabel{"
                                             "font: 10pt Doppio One;"
                                             "color: #ffffff;}"
                                             );
        self.updatedvaluelabel.move(635, 240)

        self.updatedvaluebox = QLineEdit(self)
        self.updatedvaluebox.setStyleSheet("QLineEdit{ "
                                           "border: 2px white;"
                                           "border-radius: 5px;"
                                           "padding: 0 8px;"
                                           "font-size: 12px;}"
                                           "QLineEdit:focus { "
                                           "background-color:rgb(0 0, 0,0);}"
                                           );
        self.updatedvaluebox.move(635, 265)
        self.updatedvaluebox.resize(150, 20)
        self.updatedvaluebox.setMaxLength(15)
        self.updatedvaluebox.setValidator(QIntValidator())
        self.updatedvaluebox.setMaxLength(0)

        self.updatebutton = QPushButton('Update Product', self)
        self.updatebutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                        "color: #ffffff;"
                                        "background-color: rgba(51, 0, 16,100);"
                                        "min-height: 30px; min-width: 100;}"
                                        "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                        "background-color: rgba(255, 0, 81,100);}"
                                        "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                        "background-color: rgba(153, 153, 153,80);}"
                                        )

        self.updatebutton.move(650, 295)
        self.updatebutton.setToolTip('Click to update product')
        self.updatebutton.clicked.connect(self.Update)

        # --------ORDER SYSTEM CONNECTION FROM INVENTORY SYSTEM-----------

        self.orderbutton = QPushButton('Order system', self)
        self.orderbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                       "color: #ffffff;"
                                       "background-color: rgba(51, 0, 16,100);"
                                       "min-height: 30px; min-width: 100;}"
                                       "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(255, 0, 81,100);}"
                                       "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(153, 153, 153,80);}"
                                       )
        self.orderbutton.move(25, 40)
        self.orderbutton.setToolTip('Feature Updated ^_^ ')
        self.orderbutton.clicked.connect(self.orderfunction)


        self.orderbutton = QPushButton('Log out', self)
        self.orderbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                       "color: #ffffff;"
                                       "background-color: rgba(51, 0, 16,100);"
                                       "min-height: 30px; min-width: 100;}"
                                       "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(255, 0, 81,100);}"
                                       "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(153, 153, 153,80);}"
                                       )
        self.orderbutton.move(170, 40)
        self.orderbutton.setToolTip('Click to logout')
        self.orderbutton.clicked.connect(self.mainmenu)


        # ----DELETE LABEL -----------------

        # Upperusernametext---------------------
        self.createlabel = QLabel('Hello, {}!'.format(loginaccount), self)
        self.createlabel.setStyleSheet("QLabel{"
                                       "font: 10pt Doppio One;"
                                       "color: #ffffff;}"
                                       );
        self.createlabel.move(650, 45)
        self.show()

        # --------------DATABASE TABLE----------------
        connection = pymysql.connect(host='localhost',
                                     user='danasuser',
                                     password='bunny47love',
                                     db='danasdb',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor,
                                     port=3306)
        with connection.cursor() as cursor:
            numberofproducts = cursor.execute(
                'SELECT * from products;')  # Counts the Number of Students in that group and section
            cursor.execute('SELECT * from products;')  # Select each products

            # Creates the product table
            self.tableWidget = QTableWidget()
            self.tableWidget.setRowCount(10)
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Makes the table non-editable
            self.tableWidget.verticalHeader().setVisible(False)  # Hides Vertical Headers
            self.tableWidget.setHorizontalHeaderLabels(
                ['product_code', 'product_name', 'product_qty', 'product_price'])  # Set Horizontal Header Labels
            self.tableWidget.setMaximumWidth(450)
            self.tableWidget.setMaximumHeight(300)
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.resizeColumnsToContents()
            self.header = self.tableWidget.horizontalHeader()
            self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

            self.layout = QVBoxLayout()
            self.layout.addWidget(self.tableWidget)
            self.setLayout(self.layout)

            # ---Transfer information from DB to GUI---------------
            for i in range(numberofproducts):
                productinfo = cursor.fetchone()
                self.tableWidget.setItem(i, 0, QTableWidgetItem('{}'.format(productinfo['product_code'])))
                self.tableWidget.setItem(i, 1, QTableWidgetItem('{}'.format(productinfo['product_name'])))
                self.tableWidget.setItem(i, 2, QTableWidgetItem('{}'.format(productinfo['product_qty'])))
                self.tableWidget.setItem(i, 3, QTableWidgetItem('{}'.format(productinfo['product_price'])))

    ## ----------------------END OF --- INSIDE FRAME CONTENTS--CRUD--------------------------------------------

    # -----------DATABASE TABLE--------

    # ----------------------Method for Adding Products to the Database--------------------------------------

    def orderfunction(self):

        self.newWindow = Order()
        self.newWindow.show()
        self.hide()

        self.msgbox = QMessageBox()
        self.msgbox.setIcon(QMessageBox.Information)
        self.msgbox.setText("Feature Updated ^_^ ")
        self.msgbox.setWindowTitle("Congratulations !")
        self.msgbox.show()

    def mainmenu(self):
        self.newwindow = Login()
        self.newwindow.show()
        self.hide()

    def Add(self):
        ProductCode = self.prodcodebox.text()
        ProductName = self.prodnamebox.text()
        ProductQTY = self.prodqtybox.text()
        ProductPrice = self.prodpricebox.text()
        ProductInfo = (ProductCode, ProductName, ProductQTY, ProductPrice)
        NotBlank = True
        for i in ProductInfo:
            if (len(i) == 0):
                NotBlank = False
                self.msgbox = QMessageBox()
                self.msgbox.setIcon(QMessageBox.Information)
                self.msgbox.setText("Do not leave an empty field")
                self.msgbox.setWindowTitle("Add error")
                self.msgbox.show()
                break

        if (NotBlank):
            ProductQTY = int(ProductQTY)
            ProductPrice = int(ProductPrice)
            connection = pymysql.connect(host='localhost',
                                         user='danasuser',
                                         password='bunny47love',
                                         db='danasdb',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         port=3306)
            with connection.cursor() as cursor:
                result = cursor.execute('select * from products where product_code = %s;', (ProductCode))

                if (result == 1):

                    self.msgbox = QMessageBox()
                    self.msgbox.setIcon(QMessageBox.Information)
                    self.msgbox.setText("Product already exist!")
                    self.msgbox.setWindowTitle("Add error")
                    self.msgbox.show()

                else:
                    connection = pymysql.connect(host='localhost',
                                                 user='danasuser',
                                                 password='bunny47love',
                                                 db='danasdb',
                                                 charset='utf8mb4',
                                                 cursorclass=pymysql.cursors.DictCursor,
                                                 port=3306)
                    with connection.cursor() as cursor:
                        cursor.execute('insert into products values(%s,%s,%s,%s);',
                                       (ProductCode, ProductName, ProductQTY, ProductPrice))
                        connection.commit()
                        self.msgbox = QMessageBox()
                        self.msgbox.setIcon(QMessageBox.Information)
                        self.msgbox.setText("Successfully added")
                        self.msgbox.setWindowTitle("Successful")
                        self.msgbox.show()
                        self.newwindow = Inventory()
                        self.newwindow.show()
                        self.hide()

    # -----------------------END OF Function for Adding Products to the Database----------------------

    # ----------------------Function for Viewing Products to the Database----------------------

    def addproducts(self):
        self.newWindow = Addproducts()
        self.newWindow.show()

    # -----------------------Function for Updating Products to the Database----------------------

    def UpdatedValue(self, index):
        global UpdateSelect
        UpdateSelect = self.selectupdatebox.itemText(index)
        if (UpdateSelect == '...'):
            self.updatebutton.setEnabled(False)
            self.updatedvaluebox.clear()
            self.updatedvaluebox.setMaxLength(0)
        elif (UpdateSelect == 'Product Name'):
            self.updatebutton.setEnabled(True)
            self.updatedvaluebox.clear()
            self.updatedvaluebox.setMaxLength(25)
            self.updatedvaluebox.setValidator(None)
        elif (UpdateSelect == 'Price' or UpdateSelect == 'Quantity'):
            self.updatebutton.setEnabled(True)
            self.updatedvaluebox.clear()
            self.updatedvaluebox.setMaxLength(4)
            self.updatedvaluebox.setValidator(QIntValidator())

    def Update(self):
        global UpdateSelect
        ProductCode = self.updateprodbox.text()
        UpdatedValue = self.updatedvaluebox.text()
        if (len(ProductCode) == 0 or len(UpdatedValue) == 0):
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Information)
            self.msgbox.setText("Empty field")
            self.msgbox.setWindowTitle("Cannot update the product")
            self.msgbox.show()
        else:
            connection = pymysql.connect(host='localhost',
                                         user='danasuser',
                                         password='bunny47love',
                                         db='danasdb',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         port=3306)
            with connection.cursor() as cursor:
                result = cursor.execute('select * from products where product_code = %s;', (ProductCode))

                if (result == 0):
                    self.msgbox = QMessageBox()
                    self.msgbox.setIcon(QMessageBox.Information)
                    self.msgbox.setText("Product not found!")
                    self.msgbox.setWindowTitle("Update error")
                    self.msgbox.show()

                elif (result == 1):
                    connection = pymysql.connect(host='localhost',
                                                 user='danasuser',
                                                 password='bunny47love',
                                                 db='danasdb',
                                                 charset='utf8mb4',
                                                 cursorclass=pymysql.cursors.DictCursor,
                                                 port=3306)
                    with connection.cursor() as cursor:
                        if UpdateSelect == 'Quantity':
                            cursor.execute('update products set product_qty = %s where product_code = %s',
                                           (int(UpdatedValue), ProductCode))
                            connection.commit()
                            self.msgbox = QMessageBox()
                            self.msgbox.setIcon(QMessageBox.Information)
                            self.msgbox.setText("Updated Successfully")
                            self.msgbox.setWindowTitle("Congrats!")
                            self.msgbox.show()
                            self.newwindow = Inventory()
                            self.newwindow.show()
                            self.hide()
                        elif UpdateSelect == 'Product Name':
                            cursor.execute('update products set product_name = %s where product_code = %s',
                                           (UpdatedValue, ProductCode))
                            connection.commit()
                            self.msgbox = QMessageBox()
                            self.msgbox.setIcon(QMessageBox.Information)
                            self.msgbox.setText("Updated Successfully")
                            self.msgbox.setWindowTitle("Congrats!")
                            self.msgbox.show()
                            self.newwindow = Inventory()
                            self.newwindow.show()
                            self.hide()
                        elif UpdateSelect == 'Price':
                            cursor.execute('update products set product_price = %s where product_code = %s',
                                           (int(UpdatedValue), ProductCode))
                            connection.commit()
                            self.msgbox = QMessageBox()
                            self.msgbox.setIcon(QMessageBox.Information)
                            self.msgbox.setText("Updated Successfully")
                            self.msgbox.setWindowTitle("Congrats!")
                            self.msgbox.show()
                            self.newwindow = Inventory()
                            self.newwindow.show()
                            self.hide()

    # -----------------------END OF Function for Updating Products to the Database----------------------
    # ----------------------Function for Deleting Products to the Database----------------------
    def Delete(self):
        ProductCode = self.deleteprodbox.text()
        NotBlank = True
        if (len(self.deleteprodbox.text()) == 0):
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Information)
            self.msgbox.setText("Do not leave an empyty field")
            self.msgbox.setWindowTitle("Error while deleting")
            self.msgbox.show()

        elif (NotBlank):
            connection = pymysql.connect(host='localhost',
                                         user='danasuser',
                                         password='bunny47love',
                                         db='danasdb',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         port=3306)
            with connection.cursor() as cursor:
                result = cursor.execute('select * from products where product_code = %s;', (ProductCode))

                if (result == 0):
                    self.msgbox = QMessageBox()
                    self.msgbox.setIcon(QMessageBox.Information)
                    self.msgbox.setText("Product not found!")
                    self.msgbox.setWindowTitle("Cannot delete the product")
                    self.msgbox.show()

                elif (result == 1):
                    connection = pymysql.connect(host='localhost',
                                                 user='danasuser',
                                                 password='bunny47love',
                                                 db='danasdb',
                                                 charset='utf8mb4',
                                                 cursorclass=pymysql.cursors.DictCursor,
                                                 port=3306)
                    with connection.cursor() as cursor:
                        cursor.execute('DELETE from products where product_code = %s;', (ProductCode))
                        connection.commit()
                        self.msgbox = QMessageBox()
                        self.msgbox.setIcon(QMessageBox.Information)
                        self.msgbox.setText("Successfully deleted ")
                        self.msgbox.setWindowTitle("Success")
                        self.msgbox.show()
                        self.newwindow = Inventory()
                        self.newwindow.show()
                        self.hide()

class Order(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'DANAS-ORDER'  # Window Title
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(260, 100, 795, 525)  # Window Size
        self.setStyleSheet(
            'QPushButton,QLabel,QLineEdit {font: 10pt Doppio One}')  # Changes Font for Whole Window for QPushButton, QLabel, and QlineEdit
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon(r'Media Files\danaswinicon.png'))

        # Background
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'Media Files\winbackground.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(0, 0)
        self.BackgroundHolder.resize(795, 525)
        self.BackgroundHolder.setScaledContents(True)

        self.createlabel = QLabel('Welcome , {} !'.format(loginaccount), self)
        self.createlabel.setStyleSheet("QLabel{"
                                       "font: 25pt Doppio One;"
                                       "color: #ffffff;}"
                                       )
        self.createlabel.move(285, 50)
        

         # ORDER LABEL -----------------
        self.orderlabel =QLabel(self)
        self.orderlabel.setText('Product Menu')
        self.orderlabel.move(20,105)
        self.orderlabel.setStyleSheet("QLabel{"
                                       "font: 25pt Doppio One;"
                                       "color: #ffffff;}"
                                       )
        self.orderlabel.adjustSize()
        

        self.orderlabel =QLabel(self)
        self.orderlabel.setText('Quantity')
        self.orderlabel.move(20,205)
        self.orderlabel.setStyleSheet("QLabel{"
                                       "font: 25pt Doppio One;"
                                       "color: #ffffff;}"
                                       )
        self.orderlabel.adjustSize()

        connection = pymysql.connect(host='localhost',
                                         user='danasuser',
                                         password='bunny47love',
                                         db='danasdb',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         port=3306)
        with connection.cursor() as cursor:
            
            numberofMenu = cursor.execute('select distinct product_name from products;')
            cursor.execute('select distinct product_name from products;')
                
            
        self.menubox = QComboBox(self)
        self.menubox.setGeometry(200,45,180,50)
        self.menubox.move(250,120)
        self.menubox.addItem(' ')
        
        for i in range(numberofMenu):
            order = cursor.fetchone()
            self.menubox.addItem('{}'.format(order['product_name']))
        self.menubox.setStyleSheet("font: 20pt Doppio One")
        self.menubox.activated.connect(self.setMenu)

        global setMenu
        setMenu = ' '
        global SetSize

        SetSize = ' '

        connection = pymysql.connect(host='localhost',
                                         user='danasuser',
                                         password='bunny47love',
                                         db='danasdb',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         port=3306)
        with connection.cursor() as cursor:
            
            numberofMenu = cursor.execute('select distinct product_name from products;')
            cursor.execute('select distinct product_name from products;')
        
        self.qtybox = QLineEdit(self)
        self.qtybox.move(250,215)
        self.qtybox.resize(180,20)
        self.qtybox.setMaxLength(3)
        self.qtybox.setValidator(QIntValidator(0,999))
        self.qtybox.setStyleSheet("QLineEdit{ "
                                       "border: 2px white;"
                                       "border-radius: 5px;"
                                       "padding: 0 8px;"
                                       "font-size: 12px;}"
                                       "QLineEdit:focus { "
                                       "background-color:rgb(0 0, 0,0);}"
                                       )

        self.ordernowbutton = QPushButton('Order Now',self) 
        self.ordernowbutton.move(300,300)
        self.ordernowbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                       "color: #ffffff;"
                                       "background-color: rgba(51, 0, 16,100);"
                                       "min-height: 30px; min-width: 60;}"
                                       "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(255, 0, 81,100);}"
                                       "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(153, 153, 153,80);}"
                                       )
        self.ordernowbutton.setEnabled(False)
        self.ordernowbutton.clicked.connect(self.cart)

        self.cancelbutton = QPushButton('Cancel', self)
        self.cancelbutton.move(200,300)
        self.cancelbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                       "color: #ffffff;"
                                       "background-color: rgba(51, 0, 16,100);"
                                       "min-height: 30px; min-width: 60;}"
                                       "QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(255, 0, 81,100);}"
                                       "QPushButton:pressed {border: 2px solid #f0ffe3;border-radius: 5px;"
                                       "background-color: rgba(153, 153, 153,80);}"
                                       )
        self.cancelbutton.clicked.connect(self.Cancel)
        
        self.show()
        

    def setMenu(self, index):
      
        global setMenu
        setMenu = self.menubox.itemText(index)
        
        if (setMenu == ' '):
            self.ordernowbutton.setEnabled(False)
        else:
            self.ordernowbutton.setEnabled(True)
           



    def cart(self):

        if (len(self.qtybox.text()) == 0):
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Warning)
            self.msgbox.setText(" Lagyan mo ng bilang kapatid :) ! ")
            self.msgbox.setWindowTitle("Invalid Action")
            self.msgbox.show()
        else:
            global setqty
            setqty = int(self.qtybox.text())
            self.newWindow = Cart()
            self.newWindow.show()
            self.hide()
        
    def Cancel(self):
        self.newWindow = Inventory()
        self.newWindow.show()
        self.hide()
class Cart(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'DANAS-ORDER'  # Window Title
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(260, 100, 795, 525)  # Window Size
        self.setStyleSheet(
            'QPushButton,QLabel,QLineEdit {font: 10pt Doppio One}')  # Changes Font for Whole Window for QPushButton, QLabel, and QlineEdit
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon(r'Media Files\danaswinicon.png'))

        # Background
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'Media Files\winbackground.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(0, 0)
        self.BackgroundHolder.resize(795, 525)
        self.BackgroundHolder.setScaledContents(True)

        self.createlabel = QLabel('Welcome , {} !'.format(loginaccount), self)
        self.createlabel.setStyleSheet("QLabel{"
                                       "font: 25pt Doppio One;"
                                       "color: #ffffff;}"
                                       )
        self.createlabel.move(285, 50)  
        
        self.orderconfirm = QLabel(self)
        self.orderconfirm.setText('TANSACTION SUMMARY: ')
        self.orderconfirm.move(250, 240)
        self.orderconfirm.setStyleSheet("font: 28pt Impact; color: white")
        self.orderconfirm.adjustSize()
        
        self.orderconfirm = QLabel(self)
        self.orderconfirm.setText('Product : {} \n Quantity: {} '.format(setMenu,setqty))
        self.orderconfirm.move(265, 290)
        self.orderconfirm.setStyleSheet("font: 20pt Impact; color:white")
        self.orderconfirm.adjustSize()
        
        connection = pymysql.connect(host = 'localhost',
                            user='danasuser', password = 'bunny47love',
                            db = 'danasdb',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor,
                            port = 3306)
        with connection.cursor() as cursor:
            # Gets the information of the product with the certain Flavor and Size, then stores it on variable product
            cursor.execute('SELECT * from products where product_name = %s ;',(setMenu))
            
            product=cursor.fetchone()
            
            
        TotalPrice = int(product['product_price'])*setqty

        self.orderconfirm = QLabel(self)
        self.orderconfirm.setText('\n Total Price: P{}'.format(TotalPrice))
        self.orderconfirm.move(265, 330)
        self.orderconfirm.setStyleSheet("font: 20pt Impact; color: white")
        self.orderconfirm.adjustSize()
        
        self.backbutton = QPushButton('Cancel Order', self)
        self.backbutton.move(320,  430)     
        self.backbutton.setStyleSheet("font: 10pt Century Gothic")
        self.backbutton.clicked.connect(self.Back)
        
        self.confirmorderbutton = QPushButton('Finish', self)
        self.confirmorderbutton.move(450,  430)     
        self.confirmorderbutton.setStyleSheet("font: 10pt Century Gothic")
        self.confirmorderbutton.clicked.connect(self.OrderComplete)
        
        self.show()
    
    def Back(self):
        global SetFlavor
        global SetSize
        SetFlavor = ' '
        SetSize = ' '
        
        self.newWindow = Order()
        self.newWindow.show()
        self.hide()
        
    def OrderComplete(self):
        connection = pymysql.connect(host = 'localhost',
                            user='danasuser', password = 'bunny47love',
                            db = 'danasdb',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor,
                            port = 3306)
        with connection.cursor() as cursor:
        
            cursor.execute('SELECT * from products where product_name = %s ;',(setMenu))
            product = cursor.fetchone()
            
            if(setqty > int(product['product_qty'])):
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText("Your order is too much")
                self.msgBox.setWindowTitle("Warning")
                self.msgBox.show()
                self.newWindow = Order()
                self.newWindow.show()
                self.hide()
                
            else:
                NewQuantity = int(product['product_qty'])-setqty
                connection = pymysql.connect(host = 'localhost',
                             user= 'danasuser',
                             password = 'bunny47love',
                             db = 'danasdb',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor,
                             port = 3306)
                with connection.cursor() as cursor:
                    cursor.execute('UPDATE products set product_qty = %s where product_name = %s; ',(NewQuantity,setMenu))
                    connection.commit()
                    cursor.execute('SELECT * from products where product_name = %s ;',(setMenu))
                    product = cursor.fetchone()
                    
                    
                    if(product['product_qty']<100 and product['product_qty']!=0):
                        self.msgBox = QMessageBox()
                        self.msgBox.setIcon(QMessageBox.Information)
                        self.msgBox.setText("Few stocks left")
                        self.msgBox.setWindowTitle("Warning")
                        self.msgBox.show()
                    elif(product['product_qty'] ==0):
                        self.msgBox = QMessageBox()
                        self.msgBox.setIcon(QMessageBox.Information)
                        self.msgBox.setText("No stock available")
                        self.msgBox.setWindowTitle("Warning")
                        self.msgBox.show()
                    self.transactionmsgBox = QMessageBox()
                    self.transactionmsgBox.setIcon(QMessageBox.Information)
                    self.transactionmsgBox.setText("Thank you for ordering from danas food house ^_^")
                    self.transactionmsgBox.setWindowTitle("Transaction Complete")
                    self.transactionmsgBox.show()
                    self.newWindow = Order()
                    self.newWindow.show()
                    self.hide()
                    
                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Login()
    sys.exit(app.exec_())
