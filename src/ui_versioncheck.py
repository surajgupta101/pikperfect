# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'versioncheckExaTGT.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(733, 570)
        MainWindow.setStyleSheet(u"#history_main{\n"
"   background-color:#dedede;\n"
"   border-radius:20px;\n"
"}\n"
"#wishlist_main{\n"
"   background-color:#dedede;\n"
"   border-radius:20px;\n"
"}\n"
"#mainpage{\n"
"   background-color:#ffffff;\n"
"   \n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(100, 100))
        self.centralwidget.setStyleSheet(u"*{\n"
"   color:#000;\n"
"   border:none;\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit{\n"
"   background:transparent;\n"
"}\n"
"#searchFrame{\n"
"   border-radius: 8px;\n"
"   border: 2px solid #000;\n"
"}\n"
"\n"
"#pushButton_3{\n"
"   background-color:#d9ead3;\n"
"   border-radius: 8px;\n"
"   border: 1px solid #000;\n"
"}\n"
"#pushButton_4{\n"
"   background-color:#d9ead3;\n"
"   border-radius: 8px;\n"
"   border: 1px solid #000;\n"
"}\n"
"#pushButton{\n"
"   background-color:#d9ead3;\n"
"   border-radius: 8px;\n"
"   border: 1px solid #000;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.mainpage = QWidget()
        self.mainpage.setObjectName(u"mainpage")
        self.verticalLayout_3 = QVBoxLayout(self.mainpage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.topmain = QWidget(self.mainpage)
        self.topmain.setObjectName(u"topmain")
        self.horizontalLayout = QHBoxLayout(self.topmain)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 50)
        self.appname_wid = QWidget(self.topmain)
        self.appname_wid.setObjectName(u"appname_wid")
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.appname_wid.setFont(font)
        self.horizontalLayout_4 = QHBoxLayout(self.appname_wid)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 14, 0, 0)
        self.label = QLabel(self.appname_wid)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout.addWidget(self.appname_wid, 0, Qt.AlignTop)

        self.search_wid = QWidget(self.topmain)
        self.search_wid.setObjectName(u"search_wid")
        self.horizontalLayout_2 = QHBoxLayout(self.search_wid)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.searchFrame = QFrame(self.search_wid)
        self.searchFrame.setObjectName(u"searchFrame")
        self.searchFrame.setFrameShape(QFrame.StyledPanel)
        self.searchFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.searchFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.searchFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(self.searchFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon()
        icon.addFile(u"today/img_524293.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.searchFrame)


        self.horizontalLayout.addWidget(self.search_wid, 0, Qt.AlignTop)

        self.userid_wid = QWidget(self.topmain)
        self.userid_wid.setObjectName(u"userid_wid")
        self.horizontalLayout_5 = QHBoxLayout(self.userid_wid)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.userid_wid)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setMargin(2)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.pushButton = QPushButton(self.userid_wid)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u"today/logout-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.userid_wid, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.topmain, 0, Qt.AlignTop)

        self.bottommain = QWidget(self.mainpage)
        self.bottommain.setObjectName(u"bottommain")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottommain.sizePolicy().hasHeightForWidth())
        self.bottommain.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"AppleGothic"])
        self.bottommain.setFont(font3)
        self.horizontalLayout_6 = QHBoxLayout(self.bottommain)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.history_main = QWidget(self.bottommain)
        self.history_main.setObjectName(u"history_main")
        self.verticalLayout_4 = QVBoxLayout(self.history_main)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.history_main)
        self.frame.setObjectName(u"frame")
        font4 = QFont()
        font4.setPointSize(16)
        self.frame.setFont(font4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 141, 31))
        font5 = QFont()
        font5.setFamilies([u".AppleSystemUIFont"])
        font5.setPointSize(20)
        font5.setBold(True)
        self.label_3.setFont(font5)
        self.clearbutton1 = QPushButton(self.frame)
        self.clearbutton1.setObjectName(u"clearbutton1")
        self.clearbutton1.setGeometry(QRect(170, 10, 101, 32))
        font6 = QFont()
        font6.setPointSize(20)
        self.clearbutton1.setFont(font6)
        icon2 = QIcon()
        icon2.addFile(u"today/delete-button.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clearbutton1.setIcon(icon2)
        self.clearbutton1.setIconSize(QSize(24, 24))
        self.pushButton1 = QPushButton(self.frame)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(10, 60, 271, 21))
        self.pushButton1.setFont(font4)
        self.pushButton2 = QPushButton(self.frame)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(10, 90, 271, 21))
        self.pushButton2.setFont(font4)
        self.pushButton3 = QPushButton(self.frame)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setGeometry(QRect(10, 120, 271, 21))
        self.pushButton3.setFont(font4)
        self.pushButton4 = QPushButton(self.frame)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setGeometry(QRect(10, 150, 271, 21))
        self.pushButton4.setFont(font4)
        self.pushButton5 = QPushButton(self.frame)
        self.pushButton5.setObjectName(u"pushButton5")
        self.pushButton5.setGeometry(QRect(10, 180, 271, 21))
        self.pushButton5.setFont(font4)
        self.pushButton6 = QPushButton(self.frame)
        self.pushButton6.setObjectName(u"pushButton6")
        self.pushButton6.setGeometry(QRect(10, 210, 271, 21))
        self.pushButton6.setFont(font4)
        self.pushButton7 = QPushButton(self.frame)
        self.pushButton7.setObjectName(u"pushButton7")
        self.pushButton7.setGeometry(QRect(10, 240, 271, 21))
        self.pushButton7.setFont(font4)
        self.pushButton8 = QPushButton(self.frame)
        self.pushButton8.setObjectName(u"pushButton8")
        self.pushButton8.setGeometry(QRect(10, 270, 271, 21))
        self.pushButton8.setFont(font4)
        self.pushButton9 = QPushButton(self.frame)
        self.pushButton9.setObjectName(u"pushButton9")
        self.pushButton9.setGeometry(QRect(10, 300, 271, 21))
        self.pushButton9.setFont(font4)

        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_6.addWidget(self.history_main)

        self.wishlist_main = QWidget(self.bottommain)
        self.wishlist_main.setObjectName(u"wishlist_main")
        self.verticalLayout_5 = QVBoxLayout(self.wishlist_main)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.wishlist_main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 141, 31))
        self.label_4.setFont(font5)
        self.clear2 = QPushButton(self.frame_2)
        self.clear2.setObjectName(u"clear2")
        self.clear2.setGeometry(QRect(170, 10, 101, 32))
        self.clear2.setFont(font6)
        self.clear2.setIcon(icon2)
        self.clear2.setIconSize(QSize(24, 24))
        self.pushButto4 = QPushButton(self.frame_2)
        self.pushButto4.setObjectName(u"pushButto4")
        self.pushButto4.setGeometry(QRect(10, 150, 271, 21))
        self.pushButto4.setFont(font4)
        self.pushButto1 = QPushButton(self.frame_2)
        self.pushButto1.setObjectName(u"pushButto1")
        self.pushButto1.setGeometry(QRect(10, 60, 271, 21))
        self.pushButto1.setFont(font4)
        self.pushButto8 = QPushButton(self.frame_2)
        self.pushButto8.setObjectName(u"pushButto8")
        self.pushButto8.setGeometry(QRect(10, 270, 271, 21))
        self.pushButto8.setFont(font4)
        self.pushButto5 = QPushButton(self.frame_2)
        self.pushButto5.setObjectName(u"pushButto5")
        self.pushButto5.setGeometry(QRect(10, 180, 271, 21))
        self.pushButto5.setFont(font4)
        self.pushButto2 = QPushButton(self.frame_2)
        self.pushButto2.setObjectName(u"pushButto2")
        self.pushButto2.setGeometry(QRect(10, 90, 271, 21))
        self.pushButto2.setFont(font4)
        self.pushButto7 = QPushButton(self.frame_2)
        self.pushButto7.setObjectName(u"pushButto7")
        self.pushButto7.setGeometry(QRect(10, 240, 271, 21))
        self.pushButto7.setFont(font4)
        self.pushButto6 = QPushButton(self.frame_2)
        self.pushButto6.setObjectName(u"pushButto6")
        self.pushButto6.setGeometry(QRect(10, 210, 271, 21))
        self.pushButto6.setFont(font4)
        self.pushButto3 = QPushButton(self.frame_2)
        self.pushButto3.setObjectName(u"pushButto3")
        self.pushButto3.setGeometry(QRect(10, 120, 271, 21))
        self.pushButto3.setFont(font4)
        self.pushButto9 = QPushButton(self.frame_2)
        self.pushButto9.setObjectName(u"pushButto9")
        self.pushButto9.setGeometry(QRect(10, 300, 271, 21))
        self.pushButto9.setFont(font4)

        self.verticalLayout_5.addWidget(self.frame_2)


        self.horizontalLayout_6.addWidget(self.wishlist_main)


        self.verticalLayout_2.addWidget(self.bottommain)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.mainpage)
        self.comparepage = QWidget()
        self.comparepage.setObjectName(u"comparepage")
        self.stackedWidget.addWidget(self.comparepage)
        self.searchresult = QWidget()
        self.searchresult.setObjectName(u"searchresult")
        self.stackedWidget.addWidget(self.searchresult)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PikPerfect", None))
        self.pushButton_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.clearbutton1.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton1.setText("")
        self.pushButton2.setText("")
        self.pushButton3.setText("")
        self.pushButton4.setText("")
        self.pushButton5.setText("")
        self.pushButton6.setText("")
        self.pushButton7.setText("")
        self.pushButton8.setText("")
        self.pushButton9.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Wishlist", None))
        self.clear2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButto4.setText("")
        self.pushButto1.setText("")
        self.pushButto8.setText("")
        self.pushButto5.setText("")
        self.pushButto2.setText("")
        self.pushButto7.setText("")
        self.pushButto6.setText("")
        self.pushButto3.setText("")
        self.pushButto9.setText("")
    # retranslateUi

