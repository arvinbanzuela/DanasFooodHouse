import sys
from PyQt5.QtWidgets import *
import pymysql.cursors
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator
from PyQt5.QtCore import pyqtSlot


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
        self.setWindowIcon(QIcon(r'C:\Users\XcomPh\Desktop\New folder (2)\ProjectDanas\Media Files\winicon.png'))

        # Background
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'C:\Users\XcomPh\Desktop\New folder (2)\ProjectDanas\Media Files\winbackground.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(0, 0)
        self.BackgroundHolder.resize(795, 525)
        self.BackgroundHolder.setScaledContents(True)

        # LoginDanasImage
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'C:\Users\XcomPh\Desktop\New folder (2)\ProjectDanas\Media Files\danaswinicon.png')
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
        self.usernamelabel.move(441, 193)

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
        self.registerbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 10px;"
                                          "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #EA485F, stop: 1 #EA485F);"
                                          "min-width: 80px;}"
                                          )
        self.registerbutton.move(460, 275)
        self.registerbutton.clicked.connect(self.Register)

        # Registerbuttonconnection MUST CREATE A FUCNTION FIRST FOR REGISTER WIDGET  self.registerbutton.clicked.connect(self.Register)

        # Login Button
        self.loginbutton = QPushButton('Login', self)
        self.loginbutton.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 10px;"
                                       "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #EA485F, stop: 1 #EA485F);"
                                       "min-width: 80px;}"
                                       )
        self.loginbutton.move(575, 275)
        self.loginbutton.clicked.connect(self.Login)
        self.show()

    def Register(self):
        self.newWindow = Register()
        self.newWindow.show()
        self.hide()

    def Login(self):
        Username = self.usernamebox.text()
        Password = self.password.text()
        Notblank = True
        if (len(Username) == 0 or len(Password) == 0):
            Notblank = False
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Information)
            self.msgbox.setText("Please do not leave an empty field")
            self.msgbox.setWindowTitle("Cannot Log in!")
            self.msgbox.show()

        if (Notblank):
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='',
                                         db='danasdb',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         port=3306)
            with connection.cursor() as cursor:
                result = cursor.execute("SELECT * from accounts where Username = %s and Password = %s",
                                        (Username, Password))
                if (result == 0):
                    self.msgbox = QMessageBox()
                    self.msgbox.setIcon(QMessageBox.Information)
                    self.msgbox.setText("Invalid Account!")
                    self.msgbox.setWindowTitle("Cannot Log in!")
                    self.msgbox.show()

                else:

                    global loginaccount
                    loginaccount = Username
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
                                          "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e60000, stop: 1 #EA485F);"
                                          "min-width: 80px;}"
                                          )
        self.registerbutton.move(445, 335)
        self.registerbutton.clicked.connect(self.Register)

        # Back Button to Main Menu
        self.loginbackbutton = QPushButton('Back to Log in', self)
        self.loginbackbutton.setStyleSheet("QPushButton{ border: 2px solid #e6e6ff; border-radius: 10px;"
                                           "color: #ffccdd;"
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e60000, stop: 1 #EA485F);"
                                           "min-width: 100px;}"
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
                                             user='root',
                                             password='',
                                             db='danasdb',
                                             charset='utf8mb4',
                                             cursorclass=pymysql.cursors.DictCursor,
                                             port=3306)
                with connection.cursor() as cursor:
                    result = cursor.execute('Select * from accounts where Username = %s;', (Username))
                    if (result == 1):
                        print('account already exist')
                    elif (result == 0):
                        connection = pymysql.connect(host='localhost',
                                                     user='root',
                                                     password='',
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
                            self.msgbox.setWindowTitle("Succes!")
                            self.msgbox.show()
                            self.newWindow = Login()
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
        self.setWindowIcon(QIcon(r'C:\Users\XcomPh\Desktop\New folder (2)\ProjectDanas\Media Files\winicon.png'))

        # Background
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'Media Files\winbackground.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(0, 0)
        self.BackgroundHolder.resize(795, 525)
        self.BackgroundHolder.setScaledContents(True)

        # ----------------------FRAME SECTION -------------------------------------------

        # CREATE-FRAME-AND-ICON------------------------------------------------------------------------------------------

        self.createframe = QFrame(self)
        self.createframe.setFrameShape(QFrame.StyledPanel)
        self.createframe.setStyleSheet("background-color: rgba(255, 255, 255, 60);")
        self.createframe.setGeometry(20, 30, 750, 50)


        # VIEW--FRAME------------------------------------------------------------------------------------------

        self.viewframe = QFrame(self)
        self.viewframe.setFrameShape(QFrame.StyledPanel)
        self.viewframe.setStyleSheet("background-color:  #540f35")
        self.viewframe.setGeometry(215, 150, 160, 320)

        # READ--FRAME------------------------------------------------------------------------------------------

        self.readframe = QFrame(self)
        self.readframe.setFrameShape(QFrame.StyledPanel)
        self.readframe.setStyleSheet("background-color:  #540f35")
        self.readframe.setGeometry(390, 150, 160, 320)

        # DELETE--FRAME------------------------------------------------------------------------------------------

        self.delframe = QFrame(self)
        self.delframe.setFrameShape(QFrame.StyledPanel)
        self.delframe.setStyleSheet("background-color:  #540f35")
        self.delframe.setGeometry(565, 150, 160, 320)

        # ----------------------END OF FRAME SECTION -------------------------------------------

        # ----------------------INSIDE FRAME CONTENTS -CRUD-------------------------------------

        # -------SETS OF LABELS--------------------------------------------------------------

        # -------CREATE LABELS AND QLINEEDIT ----------------

        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'Media Files\add_icon.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(40, 30)
        self.BackgroundHolder.resize(35, 35)
        self.BackgroundHolder.setScaledContents(True)
        # ----------------------
        self.addbutton1 = QPushButton('', self)
        self.addbutton1.setStyleSheet("QPushButton{ border: 1px solid #e6e6ff; border-radius: 5px;"
                                      "color: #000000;"
                                      "background-color: (255,255,255,0.5);"
                                      "min-height: 30px; min-width:50;}")

        self.addbutton1.move(35, 40)
        self.addbutton1.clicked.connect(self.addproducts)

        # -------VIEW LABELS AND QLINEEDIT ----------------

        # VIEW LABEL -----------------
        self.viewlabel = QLabel('View Products', self)
        self.viewlabel.setStyleSheet("QLabel{"
                                     "font: 15pt Doppio One;"
                                     "color: #ffffff;}"
                                     );
        self.viewlabel.move(230, 175)

        self.viewbutton = QPushButton('View', self)
        self.viewbutton.setStyleSheet("QPushButton{ border: 2px solid #e6e6ff; border-radius: 10px;"
                                      "color: #ffccdd;"
                                      "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e60000, stop: 1 #EA485F);"
                                      "min-width: 80px;}"
                                      )
        self.viewbutton.move(250, 220)
        self.viewbutton.clicked.connect(self.View)

        # UPDATE LABEL -----------------

        self.updatelabel = QLabel('Update Products', self)
        self.updatelabel.setStyleSheet("QLabel{"
                                       "font: 15pt Doppio One;"
                                       "color: #ffffff;}"
                                       );
        self.updatelabel.move(397, 175)

        self.updateprodlabel = QLabel('Product Code: ', self)
        self.updateprodlabel.setStyleSheet("QLabel{"
                                           "font: 10pt Doppio One;"
                                           "color: #ffffff;}"
                                           );
        self.updateprodlabel.move(395, 220)

        self.updateprodbox = QLineEdit(self)
        self.updateprodbox.setStyleSheet("QLineEdit{ "
                                         "border: 2px white;"
                                         "border-radius: 5px;"
                                         "padding: 0 8px;"
                                         "font-size: 12px;}"
                                         "QLineEdit:focus { "
                                         "background-color:rgb(0 0, 0,0);}"
                                         );
        self.updateprodbox.move(395, 245)
        self.updateprodbox.resize(150, 20)
        self.updateprodbox.setMaxLength(15)

        self.selectupdatelabel = QLabel('Update select: ', self)
        self.selectupdatelabel.setStyleSheet("QLabel{"
                                             "font: 10pt Doppio One;"
                                             "color: #ffffff;}"
                                             );
        self.selectupdatelabel.move(395, 270)

        self.selectupdatebox = QComboBox(self)
        self.selectupdatebox.setGeometry(395, 295, 150, 23)
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
        self.updatedvaluelabel.move(395, 320)

        self.updatedvaluebox = QLineEdit(self)
        self.updatedvaluebox.setStyleSheet("QLineEdit{ "
                                           "border: 2px white;"
                                           "border-radius: 5px;"
                                           "padding: 0 8px;"
                                           "font-size: 12px;}"
                                           "QLineEdit:focus { "
                                           "background-color:rgb(0 0, 0,0);}"
                                           );
        self.updatedvaluebox.move(395, 345)
        self.updatedvaluebox.resize(150, 20)
        self.updatedvaluebox.setMaxLength(15)
        self.updatedvaluebox.setValidator(QIntValidator())
        self.updatedvaluebox.setMaxLength(0)

        self.updatebutton = QPushButton('Update', self)
        self.updatebutton.setStyleSheet("QPushButton{ border: 2px solid #e6e6ff; border-radius: 10px;"
                                        "color: #ffccdd;"
                                        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e60000, stop: 1 #EA485F);"
                                        "min-width: 80px;}"
                                        )
        self.updatebutton.move(430, 375)
        self.updatebutton.setEnabled(False)
        self.updatebutton.clicked.connect(self.Update)

        # ----DELETE LABEL -----------------
        self.deletelabel = QLabel('Delete Products', self)
        self.deletelabel.setStyleSheet("QLabel{"
                                       "font: 15pt Doppio One;"
                                       "color: #ffffff;}"
                                       );
        self.deletelabel.move(575, 175)

        self.deleteprodlabel = QLabel('Product Code: ', self)
        self.deleteprodlabel.setStyleSheet("QLabel{"
                                           "font: 10pt Doppio One;"
                                           "color: #ffffff;}"
                                           );
        self.deleteprodlabel.move(570, 220)

        self.deleteprodbox = QLineEdit(self)
        self.deleteprodbox.setStyleSheet("QLineEdit{ "
                                         "border: 2px white;"
                                         "border-radius: 5px;"
                                         "padding: 0 8px;"
                                         "font-size: 12px;}"
                                         "QLineEdit:focus { "
                                         "background-color:rgb(0 0, 0,0);}"
                                         );
        self.deleteprodbox.move(570, 245)
        self.deleteprodbox.resize(150, 20)
        self.deleteprodbox.setMaxLength(15)

        self.deletebutton = QPushButton('Delete', self)
        self.deletebutton.setStyleSheet("QPushButton{ border: 2px solid #e6e6ff; border-radius: 10px;"
                                        "color: #ffccdd;"
                                        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e60000, stop: 1 #EA485F);"
                                        "min-width: 80px;}"
                                        )
        self.deletebutton.move(600, 275)
        self.deletebutton.clicked.connect(self.Delete)

        # Upperusernametext---------------------
        self.createlabel = QLabel('Hello, {}!'.format(loginaccount), self)
        self.createlabel.setStyleSheet("QLabel{"
                                       "font: 25pt Doppio One;"
                                       "color: #ffffff;}"
                                       );
        self.createlabel.move(285, 50)
        self.show()
        # ----------------------------------------

        # ----------------------END OF --- INSIDE FRAME CONTENTS--CRUD--------------------------------------------
        # ----------------------Function for Adding Products to the Database--------------------------------------

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
                self.msgbox.setWindowTitle("Cannot add the product")
                self.msgbox.show()
                break
        if (NotBlank):
            ProductQTY = int(ProductQTY)
            ProductPrice = int(ProductPrice)
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='',
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
                    self.msgbox.setWindowTitle("Cannot add the product")
                    self.msgbox.show()

                else:
                    connection = pymysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
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
                        self.msgbox.setWindowTitle("Cannot add the product")
                        self.msgbox.show()

    # -----------------------END OF Function for Adding Products to the Database----------------------

    # ----------------------Function for Viewing Products to the Database----------------------

    def addproducts(self):
        self.newWindow = Addproducts()
        self.newWindow.show()

    def View(self):
        self.newWindow = Viewproducts()
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
                                         user='root',
                                         password='',
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
                    self.msgbox.setWindowTitle("Cannot update the product")
                    self.msgbox.show()

                elif (result == 1):
                    connection = pymysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
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
                        elif UpdateSelect == 'Product Name':
                            cursor.execute('update products set product_name = %s where product_code = %s',
                                           (UpdatedValue, ProductCode))
                            connection.commit()
                            self.msgbox = QMessageBox()
                            self.msgbox.setIcon(QMessageBox.Information)
                            self.msgbox.setText("Updated Successfully")
                            self.msgbox.setWindowTitle("Congrats!")
                            self.msgbox.show()
                        elif UpdateSelect == 'Price':
                            cursor.execute('update products set product_price = %s where product_code = %s',
                                           (int(UpdatedValue), ProductCode))
                            connection.commit()
                            self.msgbox = QMessageBox()
                            self.msgbox.setIcon(QMessageBox.Information)
                            self.msgbox.setText("Updated Successfully")
                            self.msgbox.setWindowTitle("Congrats!")
                            self.msgbox.show()

    # -----------------------END OF Function for Updating Products to the Database----------------------
    # ----------------------Function for Deleting Products to the Database----------------------
    def Delete(self):
        ProductCode = self.deleteprodbox.text()
        NotBlank = True
        if (len(self.deleteprodbox.text()) == 0):
            self.msgbox = QMessageBox()
            self.msgbox.setIcon(QMessageBox.Information)
            self.msgbox.setText("Do not leave an empyty field")
            self.msgbox.setWindowTitle("Cannot add the product")
            self.msgbox.show()

        elif (NotBlank):
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='',
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
                                                 user='root',
                                                 password='',
                                                 db='danasdb',
                                                 charset='utf8mb4',
                                                 cursorclass=pymysql.cursors.DictCursor,
                                                 port=3306)
                    with connection.cursor() as cursor:
                        cursor.execute('DELETE from products where product_code = %s;', (ProductCode))
                        connection.commit()


class Addproducts(QWidget):

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
        self.setWindowIcon(QIcon(r'C:\Users\XcomPh\Desktop\New folder (2)\ProjectDanas\Media Files\winicon.png'))

        # Background
        self.BackgroundHolder = QLabel(self)
        self.Background = QPixmap(r'C:\Users\XcomPh\Desktop\New folder (2)\ProjectDanas\Media Files\winbackground.png')
        self.BackgroundHolder.setPixmap(self.Background)
        self.BackgroundHolder.move(0, 0)
        self.BackgroundHolder.resize(795, 525)
        self.BackgroundHolder.setScaledContents(True)
        # -------CREATE LABELS AND QLINEEDIT ----------------
        self.createlabel = QLabel('Add Products', self)
        self.createlabel.setStyleSheet("QLabel{"
                                       "font: 15pt Doppio One;"
                                       "color: #ffffff;}"
                                       );
        self.createlabel.move(60, 175)

        self.prodcodelabel = QLabel('Product Code: ', self)
        self.prodcodelabel.setStyleSheet("QLabel{"
                                         "font: 10pt Doppio One;"
                                         "color: #ffffff;}"
                                         );
        self.prodcodelabel.move(45, 220)

        self.prodcodebox = QLineEdit(self)
        self.prodcodebox.setStyleSheet("QLineEdit{ "
                                       "border: 2px white;"
                                       "border-radius: 5px;"
                                       "padding: 0 8px;"
                                       "font-size: 12px;}"
                                       "QLineEdit:focus { "
                                       "background-color:rgb(0 0, 0,0);}"
                                       );
        self.prodcodebox.move(45, 245)
        self.prodcodebox.resize(150, 20)
        self.prodcodebox.setMaxLength(15)

        self.prodnamelabel = QLabel('Product Name: ', self)
        self.prodnamelabel.setStyleSheet("QLabel{"
                                         "font: 10pt Doppio One;"
                                         "color: #ffffff;}"
                                         );
        self.prodnamelabel.move(45, 270)

        self.prodnamebox = QLineEdit(self)
        self.prodnamebox.setStyleSheet("QLineEdit{ "
                                       "border: 2px white;"
                                       "border-radius: 5px;"
                                       "padding: 0 8px;"
                                       "font-size: 12px;}"
                                       "QLineEdit:focus { "
                                       "background-color:rgb(0 0, 0,0);}"
                                       );
        self.prodnamebox.move(45, 295)
        self.prodnamebox.resize(150, 20)
        self.prodnamebox.setMaxLength(15)

        self.prodqtylabel = QLabel('QTY: ', self)
        self.prodqtylabel.setStyleSheet("QLabel{"
                                        "font: 10pt Doppio One;"
                                        "color: #ffffff;}"
                                        );
        self.prodqtylabel.move(45, 320)

        self.prodqtybox = QLineEdit(self)
        self.prodqtybox.setStyleSheet("QLineEdit{ "
                                      "border: 2px white;"
                                      "border-radius: 5px;"
                                      "padding: 0 8px;"
                                      "font-size: 12px;}"
                                      "QLineEdit:focus { "
                                      "background-color:rgb(0 0, 0,0);}"
                                      );
        self.prodqtybox.move(45, 345)
        self.prodqtybox.resize(150, 20)
        self.prodqtybox.setMaxLength(15)
        self.prodqtybox.setValidator(QIntValidator())

        self.prodpricelabel = QLabel('Product Price: ', self)
        self.prodpricelabel.setStyleSheet("QLabel{"
                                          "font: 10pt Doppio One;"
                                          "color: #ffffff;}"
                                          );
        self.prodpricelabel.move(45, 370)

        self.prodpricebox = QLineEdit(self)
        self.prodpricebox.setStyleSheet("QLineEdit{ "
                                        "border: 2px white;"
                                        "border-radius: 5px;"
                                        "padding: 0 8px;"
                                        "font-size: 12px;}"
                                        "QLineEdit:focus { "
                                        "background-color:rgb(0 0, 0,0);}"
                                        );
        self.prodpricebox.move(45, 395)
        self.prodpricebox.resize(150, 20)
        self.prodpricebox.setMaxLength(15)
        self.prodpricebox.setValidator(QIntValidator())

        self.addbutton = QPushButton('Add', self)
        self.addbutton.setStyleSheet("QPushButton{ border: 2px solid #e6e6ff; border-radius: 10px;"
                                     "color: #ffccdd;"
                                     "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e60000, stop: 1 #EA485F);"
                                     "min-width: 80px;}"
                                     )
        self.addbutton.move(75, 430)
        self.addbutton.clicked.connect(self.Add)

    # ----------------------Function for Adding Products to the Database--------------------------------------

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
                self.msgbox.setWindowTitle("Cannot add the product")
                self.msgbox.show()
                break
        if (NotBlank):
            ProductQTY = int(ProductQTY)
            ProductPrice = int(ProductPrice)
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='',
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
                    self.msgbox.setWindowTitle("Cannot add the product")
                    self.msgbox.show()

                else:
                    connection = pymysql.connect(host='localhost',
                                                 user='root',
                                                 password='',
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
                        self.msgbox.setWindowTitle("Cannot add the product")
                        self.msgbox.show()


# -----------------------END OF Function for Adding Products to the Database----------------------

class Viewproducts(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PRODUCTS LIST'  # Window Title
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(260, 100, 600, 525)  # Window Size
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

        # Connects Python to Mysql
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
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

                self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Login()
    sys.exit(app.exec_())
