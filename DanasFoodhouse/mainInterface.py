import sys
from PyQt5.QtWidgets import  *
import pymysql.cursors
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot


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

        # ----------------------FRAME SECTION -------------------------------------------

        # CREATE-FRAME------------------------------------------------------------------------------------------

        self.createframe = QFrame(self)
        self.createframe.setFrameShape(QFrame.StyledPanel)
        self.createframe.setStyleSheet("background-color:  #540f35")
        self.createframe.setGeometry(40, 150, 160, 320)

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
        self.createlabel = QLabel('Add Products', self)
        self.createlabel.setStyleSheet("QLabel{"
                                       "font: 15pt Doppio One;"
                                       "color: #ffffff;}"
                                       )
        self.createlabel.move(60, 175)

        self.pidlabel = QLabel('Product Code: ', self)
        self.pidlabel.setStyleSheet("QLabel{"
                                    "font: 10pt Doppio One;"
                                    "color: #ffffff;}"
                                    )
        self.pidlabel.move(45, 220)

        self.pidbox = QLineEdit(self)
        self.pidbox.setStyleSheet("QLineEdit{ "
                                  "border: 2px white;"
                                  "border-radius: 5px;"
                                  "padding: 0 8px;"
                                  "font-size: 12px;}"
                                  "QLineEdit:focus { "
                                  "background-color:rgb(0 0, 0,0);}"
                                  )
        self.pidbox.move(45, 245)
        self.pidbox.resize(150, 20)
        self.pidbox.setMaxLength(15)

        self.prodnamelabel = QLabel('Product Name: ', self)
        self.prodnamelabel.setStyleSheet("QLabel{"
                                         "font: 10pt Doppio One;"
                                         "color: #ffffff;}"
                                         )
        self.prodnamelabel.move(45, 270)

        self.prodnamebox = QLineEdit(self)
        self.prodnamebox.setStyleSheet("QLineEdit{ "
                                       "border: 2px white;"
                                       "border-radius: 5px;"
                                       "padding: 0 8px;"
                                       "font-size: 12px;}"
                                       "QLineEdit:focus { "
                                       "background-color:rgb(0 0, 0,0);}"
                                       )
        self.prodnamebox.move(45, 295)
        self.prodnamebox.resize(150, 20)
        self.prodnamebox.setMaxLength(15)

        self.prodqtylabel = QLabel('QTY: ', self)
        self.prodqtylabel.setStyleSheet("QLabel{"
                                        "font: 10pt Doppio One;"
                                        "color: #ffffff;}"
                                        )
        self.prodqtylabel.move(45, 320)

        self.prodqtybox = QLineEdit(self)
        self.prodqtybox.setStyleSheet("QLineEdit{ "
                                      "border: 2px white;"
                                      "border-radius: 5px;"
                                      "padding: 0 8px;"
                                      "font-size: 12px;}"
                                      "QLineEdit:focus { "
                                      "background-color:rgb(0 0, 0,0);}"
                                      )
        self.prodqtybox.move(45, 345)
        self.prodqtybox.resize(150, 20)
        self.prodqtybox.setMaxLength(15)
        self.prodqtybox.setValidator(QIntValidator())

        self.prodpricelabel = QLabel('Product Price: ', self)
        self.prodpricelabel.setStyleSheet("QLabel{"
                                          "font: 10pt Doppio One;"
                                          "color: #ffffff;}"
                                          )
        self.prodpricelabel.move(45, 370)

        self.prodpricebox = QLineEdit(self)
        self.prodpricebox.setStyleSheet("QLineEdit{ "
                                        "border: 2px white;"
                                        "border-radius: 5px;"
                                        "padding: 0 8px;"
                                        "font-size: 12px;}"
                                        "QLineEdit:focus { "
                                        "background-color:rgb(0 0, 0,0);}"
                                        )
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

        # -------VIEW LABELS AND QLINEEDIT ----------------

        # VIEW LABEL -----------------
        self.viewlabel = QLabel('View Products', self)
        self.viewlabel.setStyleSheet("QLabel{"
                                     "font: 15pt Doppio One;"
                                     "color: #ffffff;}"
                                     )
        self.viewlabel.move(230, 175)

        self.viewbutton = QPushButton('View', self)
        self.viewbutton.setStyleSheet("QPushButton{ border: 2px solid #e6e6ff; border-radius: 10px;"
                                      "color: #ffccdd;"
                                      "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e60000, stop: 1 #EA485F);"
                                      "min-width: 80px;}"
                                      )
        self.viewbutton.move(250, 220)

        # UPDATE LABEL -----------------
        self.updatelabel = QLabel('Update Products', self)
        self.updatelabel.setStyleSheet("QLabel{"
                                       "font: 15pt Doppio One;"
                                       "color: #ffffff;}"
                                       )
        self.updatelabel.move(397, 175)

        self.updateprodlabel = QLabel('Product Code: ', self)
        self.updateprodlabel.setStyleSheet("QLabel{"
                                          "font: 10pt Doppio One;"
                                          "color: #ffffff;}"
                                          )
        self.updateprodlabel.move(395, 220)

        self.updateprodbox = QLineEdit(self)
        self.updateprodbox.setStyleSheet("QLineEdit{ "
                                         "border: 2px white;"
                                         "border-radius: 5px;"
                                         "padding: 0 8px;"
                                         "font-size: 12px;}"
                                         "QLineEdit:focus { "
                                         "background-color:rgb(0 0, 0,0);}"
                                         )
        self.updateprodbox.move(395, 245)
        self.updateprodbox.resize(150, 20)
        self.updateprodbox.setMaxLength(15)

        self.selectupdatelabel = QLabel('Update select: ', self)
        self.selectupdatelabel.setStyleSheet("QLabel{"
                                             "font: 10pt Doppio One;"
                                             "color: #ffffff;}"
                                             )
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
                                           )
        self.selectupdatebox.addItem('...', ' ')
        self.selectupdatebox.addItem('Product Name')
        self.selectupdatebox.addItem('Quantity')
        self.selectupdatebox.addItem('Price')

        self.updatedvaluelabel = QLabel('Updated Value: ', self)
        self.updatedvaluelabel.setStyleSheet("QLabel{"
                                        "font: 10pt Doppio One;"
                                        "color: #ffffff;}"
                                        )
        self.updatedvaluelabel.move(395, 320)

        self.updatedvaluebox = QLineEdit(self)
        self.updatedvaluebox.setStyleSheet("QLineEdit{ "
                                      "border: 2px white;"
                                      "border-radius: 5px;"
                                      "padding: 0 8px;"
                                      "font-size: 12px;}"
                                      "QLineEdit:focus { "
                                      "background-color:rgb(0 0, 0,0);}"
                                      )
        self.updatedvaluebox.move(395, 345)
        self.updatedvaluebox.resize(150, 20)
        self.updatedvaluebox.setMaxLength(15)
        self.updatedvaluebox.setValidator(QIntValidator())

        self.updatebutton = QPushButton('Update', self)
        self.updatebutton.setStyleSheet("QPushButton{ border: 2px solid #e6e6ff; border-radius: 10px;"
                                     "color: #ffccdd;"
                                     "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e60000, stop: 1 #EA485F);"
                                     "min-width: 80px;}"
                                     )
        self.updatebutton.move(430, 375)

        # ----DELETE LABEL -----------------
        self.deletelabel = QLabel('Delete Products', self)
        self.deletelabel.setStyleSheet("QLabel{"
                                       "font: 15pt Doppio One;"
                                       "color: #ffffff;}"
                                       )
        self.deletelabel.move(575, 175)

        self.deleteprodlabel = QLabel('Product Code: ', self)
        self.deleteprodlabel.setStyleSheet("QLabel{"
                                           "font: 10pt Doppio One;"
                                           "color: #ffffff;}"
                                           )
        self.deleteprodlabel.move(570, 220)

        self.deleteprodbox = QLineEdit(self)
        self.deleteprodbox.setStyleSheet("QLineEdit{ "
                                         "border: 2px white;"
                                         "border-radius: 5px;"
                                         "padding: 0 8px;"
                                         "font-size: 12px;}"
                                         "QLineEdit:focus { "
                                         "background-color:rgb(0 0, 0,0);}"
                                         )
        self.deleteprodbox.move(570, 245)
        self.deleteprodbox.resize(150, 20)
        self.deleteprodbox.setMaxLength(15)

        self.deletebutton = QPushButton('Update', self)
        self.deletebutton.setStyleSheet("QPushButton{ border: 2px solid #e6e6ff; border-radius: 10px;"
                                        "color: #ffccdd;"
                                        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e60000, stop: 1 #EA485F);"
                                        "min-width: 80px;}"
                                        )
        self.deletebutton.move(600, 275)

        # -----------

        # ----------------------END OF --- INSIDE FRAME CONTENTS--CRUD--------------------------------------------

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Main = Inventory()
    sys.exit(app.exec_())
