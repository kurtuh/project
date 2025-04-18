# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)
import files_rc
import files_rc1

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1082, 1127)
        MainWindow.setMinimumSize(QSize(1082, 1127))
        MainWindow.setMaximumSize(QSize(1082, 1127))
        icon = QIcon()
        icon.addFile(u":/icons/4107608.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(810, 110, 91, 41))
        self.label.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(910, 110, 31, 41))
        self.label_2.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QRect(10, 50, 161, 131))
        self.label_3.setMouseTracking(False)
        self.label_3.setTabletTracking(False)
        self.label_3.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_3.setAcceptDrops(False)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"border-image: url(:/icons/photo_5395603866361390873_m (1).jpg);")
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 200, 131, 31))
        self.label_4.setStyleSheet(u"\n"
"font: 600 15pt \"Segoe UI\";\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(-30, 240, 311, 201))
        self.label_5.setMouseTracking(False)
        self.label_5.setTabletTracking(False)
        self.label_5.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_5.setAcceptDrops(False)
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"border-image: url(:/icons/M_height.jpg);")
        self.label_5.setFrameShadow(QFrame.Shadow.Plain)
        self.label_5.setTextFormat(Qt.TextFormat.AutoText)
        self.label_5.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)
        self.label_5.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(120, 560, 111, 41))
        self.pushButton_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"radius 10px;")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 550, 81, 41))
        self.label_6.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(410, 560, 111, 41))
        self.pushButton_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"radius 10px;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QRect(290, 220, 211, 201))
        self.label_7.setMouseTracking(False)
        self.label_7.setTabletTracking(False)
        self.label_7.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_7.setAcceptDrops(False)
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet(u"border-image: url(:/icons/photo_5458702399138032533_m.jpg);")
        self.label_7.setFrameShadow(QFrame.Shadow.Plain)
        self.label_7.setTextFormat(Qt.TextFormat.AutoText)
        self.label_7.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)
        self.label_7.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 550, 81, 41))
        self.label_8.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 430, 141, 41))
        self.label_9.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(290, 430, 161, 41))
        self.label_10.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(570, 560, 81, 41))
        self.label_11.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(680, 560, 111, 41))
        self.pushButton_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"radius 10px;")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QRect(560, 220, 221, 201))
        self.label_12.setMouseTracking(False)
        self.label_12.setTabletTracking(False)
        self.label_12.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_12.setAcceptDrops(False)
        self.label_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet(u"border-image: url(:/icons/\u0442\u0430\u0440\u0442\u0430\u0440.jpg);")
        self.label_12.setFrameShadow(QFrame.Shadow.Plain)
        self.label_12.setTextFormat(Qt.TextFormat.AutoText)
        self.label_12.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setWordWrap(False)
        self.label_12.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(570, 430, 161, 41))
        self.label_13.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 1000, 81, 41))
        self.label_14.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(140, 1000, 111, 41))
        self.pushButton_13.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"radius 10px;")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setEnabled(True)
        self.label_15.setGeometry(QRect(20, 650, 231, 201))
        self.label_15.setMouseTracking(False)
        self.label_15.setTabletTracking(False)
        self.label_15.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_15.setAcceptDrops(False)
        self.label_15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet(u"border-image: url(:/icons1/\u0441\u0443\u0448\u0438.jpg);")
        self.label_15.setFrameShadow(QFrame.Shadow.Plain)
        self.label_15.setTextFormat(Qt.TextFormat.AutoText)
        self.label_15.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setWordWrap(False)
        self.label_15.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 860, 161, 41))
        self.label_16.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(290, 1000, 81, 41))
        self.label_17.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(410, 1000, 111, 41))
        self.pushButton_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"radius 10px;")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setEnabled(True)
        self.label_18.setGeometry(QRect(290, 660, 231, 201))
        self.label_18.setMouseTracking(False)
        self.label_18.setTabletTracking(False)
        self.label_18.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_18.setAcceptDrops(False)
        self.label_18.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_18.setAutoFillBackground(False)
        self.label_18.setStyleSheet(u"border-image: url(:/icons1/\u0431\u0443\u0440\u0433\u0435\u0440.jpg);")
        self.label_18.setFrameShadow(QFrame.Shadow.Plain)
        self.label_18.setTextFormat(Qt.TextFormat.AutoText)
        self.label_18.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setWordWrap(False)
        self.label_18.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(290, 870, 211, 41))
        self.label_19.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(570, 1010, 81, 41))
        self.label_20.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(680, 1010, 111, 41))
        self.pushButton_15.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"radius 10px;")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setEnabled(True)
        self.label_21.setGeometry(QRect(570, 620, 211, 241))
        self.label_21.setMouseTracking(False)
        self.label_21.setTabletTracking(False)
        self.label_21.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_21.setAcceptDrops(False)
        self.label_21.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setStyleSheet(u"border-image: url(:/icons1/\u043a\u043e\u043a\u0430\u043b\u044f.jpg);")
        self.label_21.setFrameShadow(QFrame.Shadow.Plain)
        self.label_21.setTextFormat(Qt.TextFormat.AutoText)
        self.label_21.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setWordWrap(False)
        self.label_21.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(570, 870, 161, 41))
        self.label_22.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(820, 560, 81, 41))
        self.label_23.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(930, 560, 111, 41))
        self.pushButton_16.setStyleSheet(u"")
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setEnabled(True)
        self.label_24.setGeometry(QRect(810, 220, 231, 211))
        self.label_24.setMouseTracking(False)
        self.label_24.setTabletTracking(False)
        self.label_24.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_24.setAcceptDrops(False)
        self.label_24.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_24.setAutoFillBackground(False)
        self.label_24.setStyleSheet(u"border-image: url(:/icons1/\u043a\u0430\u0440\u0431\u043e\u043d\u0430\u0440\u0430.jpg);")
        self.label_24.setFrameShadow(QFrame.Shadow.Plain)
        self.label_24.setTextFormat(Qt.TextFormat.AutoText)
        self.label_24.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setWordWrap(False)
        self.label_24.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(810, 420, 161, 41))
        self.label_25.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(810, 1010, 81, 41))
        self.label_26.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(930, 1010, 111, 41))
        self.pushButton_17.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"radius 10px;")
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setEnabled(True)
        self.label_27.setGeometry(QRect(810, 630, 211, 241))
        self.label_27.setMouseTracking(False)
        self.label_27.setTabletTracking(False)
        self.label_27.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_27.setAcceptDrops(False)
        self.label_27.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_27.setAutoFillBackground(False)
        self.label_27.setStyleSheet(u"border-image: url(:/icons1/\u043c\u0438\u043b\u043a\u0448\u0435\u0439\u043a.jpg);")
        self.label_27.setFrameShadow(QFrame.Shadow.Plain)
        self.label_27.setTextFormat(Qt.TextFormat.AutoText)
        self.label_27.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setWordWrap(False)
        self.label_27.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(810, 880, 161, 41))
        self.label_28.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 470, 231, 91))
        self.textEdit.setStyleSheet(u"font: 7pt \"Segoe UI\";\n"
"color: rgb(172, 255, 147);\n"
"border: none;")
        self.textEdit.setReadOnly(True)
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(280, 470, 231, 91))
        self.textEdit_2.setStyleSheet(u"font: 7pt \"Segoe UI\";\n"
"color: rgb(172, 255, 147);\n"
"border: none;")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(560, 470, 191, 91))
        self.textEdit_3.setStyleSheet(u"font: 7pt \"Segoe UI\";\n"
"color: rgb(172, 255, 147);\n"
"border: none;")
        self.textEdit_3.setReadOnly(True)
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(810, 460, 231, 91))
        self.textEdit_4.setStyleSheet(u"font: 7pt \"Segoe UI\";\n"
"color: rgb(172, 255, 147);\n"
"border: none;")
        self.textEdit_4.setReadOnly(True)
        self.textEdit_5 = QTextEdit(self.centralwidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(20, 900, 231, 91))
        self.textEdit_5.setStyleSheet(u"font: 7pt \"Segoe UI\";\n"
"color: rgb(172, 255, 147);\n"
"border: none;")
        self.textEdit_5.setReadOnly(True)
        self.textEdit_6 = QTextEdit(self.centralwidget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(280, 900, 231, 91))
        self.textEdit_6.setStyleSheet(u"font: 7pt \"Segoe UI\";\n"
"color: rgb(172, 255, 147);\n"
"border: none;")
        self.textEdit_6.setReadOnly(True)
        self.textEdit_7 = QTextEdit(self.centralwidget)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setGeometry(QRect(560, 910, 221, 91))
        self.textEdit_7.setStyleSheet(u"font: 7pt \"Segoe UI\";\n"
"color: rgb(172, 255, 147);\n"
"border: none;")
        self.textEdit_7.setReadOnly(True)
        self.textEdit_8 = QTextEdit(self.centralwidget)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setGeometry(QRect(800, 910, 231, 91))
        self.textEdit_8.setStyleSheet(u"font: 7pt \"Segoe UI\";\n"
"color: rgb(172, 255, 147);\n"
"border: none;")
        self.textEdit_8.setReadOnly(True)
        self.textEdit_9 = QTextEdit(self.centralwidget)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(180, 140, 161, 61))
        self.textEdit_9.setStyleSheet(u"font: 600 7pt \"Segoe UI\";\n"
"color: rgb(172, 255, 147);\n"
"border: none;")
        self.textEdit_9.setReadOnly(True)
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setEnabled(True)
        self.label_29.setGeometry(QRect(810, 40, 171, 71))
        self.label_29.setMouseTracking(False)
        self.label_29.setTabletTracking(False)
        self.label_29.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.label_29.setAcceptDrops(False)
        self.label_29.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_29.setAutoFillBackground(False)
        self.label_29.setStyleSheet(u"border-image: url(:/icons3/\u0421\u043d\u0438\u043c\u043e\u043a \u044d\u043a\u0440\u0430\u043d\u0430 2025-04-10 113238.png);")
        self.label_29.setFrameShadow(QFrame.Shadow.Plain)
        self.label_29.setTextFormat(Qt.TextFormat.AutoText)
        self.label_29.setPixmap(QPixmap(u":/icons/Downloads/3.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setWordWrap(False)
        self.label_29.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 0, 131, 41))
        self.label_30.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(170, 0, 91, 41))
        self.label_31.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(270, 0, 131, 41))
        self.label_32.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(410, 0, 181, 41))
        self.label_33.setStyleSheet(u"font: 10pt \"Segoe UI\";")
        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(800, 150, 111, 41))
        self.pushButton_18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"radius 10px;")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(450, 51, 331, 181))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(590, 10, 111, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI\";\n"
"radius 10px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Avocado", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u0437\u0430\u043a\u0430\u0437\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.label_5.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"400\u20bd", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"300\u20bd", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u0446\u0446\u0430 \u0427\u043e\u0440\u0438\u0437\u043e \u0424\u0440\u0435\u0448 ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0441\u0442 \u0441 \u0430\u0432\u043e\u043a\u0430\u0434\u043e \u0438 \u044f\u0439\u0446\u043e\u043c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"500\u20bd", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0440 \u0442\u0430\u0440 \u0441 \u0433\u043e\u0432\u044f\u0434\u0438\u043d\u043e\u0439", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"450\u20bd", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u0448\u0438 \u0424\u0438\u043b\u0430\u0434\u0435\u043b\u044c\u0444\u0438\u044f  ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"520\u20bd", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0440\u0433\u0435\u0440 \u0441 \u043c\u0440\u0430\u043c\u043e\u0440\u043d\u043e\u0439 \u0433\u043e\u0432\u044f\u0434\u0438\u043d\u043e\u0439", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"200\u20bd", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_21.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043a\u0430 \u043a\u043e\u043b\u0430", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"420\u20bd", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u0442\u0430 \u043a\u0430\u0440\u0431\u043e\u043d\u0430\u0440\u0430  \n"
"", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"300\u20bd", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u043b\u043e\u0447\u043d\u044b\u0439 \u043a\u043e\u043a\u0442\u0435\u0439\u043b\u044c", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','-apple-system','apple color emoji','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:8pt; font-weight:700; color:#515151; background-color:#ffffff;\">\u0412\u043a\u0443\u0441\u043d\u0430\u044f \u043f\u0438\u0446\u0446\u0430 \u0441 \u043f\u0438\u043a\u0430\u043d\u0442\u043d\u043e\u0439 \u043a\u043e\u043b"
                        "\u0431\u0430\u0441\u043e\u0439 \u0447\u043e\u0440\u0438\u0437\u043e, \u0441\u0432\u0435\u0436\u0438\u043c\u0438 \u043e\u0432\u043e\u0449\u0430\u043c\u0438 \u0438 \u0430\u0440\u043e\u043c\u0430\u0442\u043d\u044b\u043c\u0438 \u0441\u043f\u0435\u0446\u0438\u044f\u043c\u0438. \u0414\u0430\u0435\u0442 \u0437\u0430\u0440\u044f\u0434 \u044d\u043d\u0435\u0440\u0433\u0438\u0438 \u0438 \u043e\u0442\u043b\u0438\u0447\u043d\u043e \u043f\u043e\u0434\u0445\u043e\u0434\u0438\u0442 \u0434\u043b\u044f \u043b\u044e\u0431\u0438\u0442\u0435\u043b\u0435\u0439 \u043e\u0441\u0442\u0440\u0435\u043d\u044c\u043a\u043e\u0433\u043e!</span></p></body></html>", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','-apple-system','apple color emoji','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:8pt; font-weight:700; color:#515151; background-color:#ffffff;\">\u041d\u0435\u0436\u043d\u044b\u0439 \u0430\u0432\u043e\u043a\u0430\u0434\u043e \u043d\u0430 \u043f\u043e\u0434\u0436\u0430\u0440\u0435\u043d\u043d\u043e"
                        "\u043c \u0445\u043b\u0435\u0431\u0435, \u0443\u043a\u0440\u0430\u0448\u0435\u043d\u043d\u044b\u0439 \u044f\u0439\u0446\u043e\u043c \u043f\u0430\u0448\u043e\u0442. \u0418\u0434\u0435\u0430\u043b\u044c\u043d\u044b\u0439 \u0437\u0430\u0432\u0442\u0440\u0430\u043a \u0434\u043b\u044f \u043b\u044e\u0431\u0438\u0442\u0435\u043b\u0435\u0439 \u0437\u0434\u043e\u0440\u043e\u0432\u043e\u0439 \u043a\u0443\u0445\u043d\u0438!</span></p></body></html>", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','-apple-system','apple color emoji','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:8pt; font-weight:700; color:#515151; background-color:#ffffff;\">\u0421\u043e\u0447\u043d\u044b\u0435 \u043a\u0443\u0441\u043e\u0447\u043a\u0438 \u0441\u0432\u0435\u0436\u0435\u0439 \u0433\u043e\u0432\u044f\u0434\u0438"
                        "\u043d\u044b \u0441 \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u043c \u0441\u043e\u0443\u0441\u043e\u043c, \u043f\u043e\u0434\u0430\u043d\u043d\u044b\u0435 \u0441 \u0445\u0440\u0443\u0441\u0442\u044f\u0449\u0438\u043c\u0438 \u0447\u0438\u043f\u0441\u0430\u043c\u0438. \u042d\u043b\u0435\u0433\u0430\u043d\u0442\u043d\u043e\u0435 \u0438 \u0432\u043a\u0443\u0441\u043d\u043e\u0435 \u043d\u0430\u0447\u0430\u043b\u043e \u0432\u0435\u0447\u0435\u0440\u0430.</span></p></body></html>", None))
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','-apple-system','apple color emoji','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:8pt; font-weight:700; color:#515151; background-color:#ffffff;\">\u0417\u0430\u0432\u043e\u0440\u0430\u0436\u0438\u0432\u0430\u044e\u0449\u0430\u044f \u043f\u0430\u0441\u0442\u0430, \u043f\u0440\u0438\u0433\u043e\u0442"
                        "\u043e\u0432\u043b\u0435\u043d\u043d\u0430\u044f \u043f\u043e \u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u043e\u043c\u0443 \u0440\u0435\u0446\u0435\u043f\u0442\u0443 \u2013 \u043a\u0440\u0435\u043c\u043e\u0432\u044b\u0439 \u0441\u043e\u0443\u0441, \u043a\u0443\u0441\u043e\u0447\u043a\u0438 \u043f\u0430\u043d\u0447\u0435\u0442\u0442\u044b \u0438 \u043f\u0430\u0440\u043c\u0435\u0437\u0430\u043d. \u0418\u0442\u0430\u043b\u0438\u044f \u043d\u0430 \u0432\u0430\u0448\u0435\u043c \u0441\u0442\u043e\u043b\u0435!</span></p></body></html>", None))
        self.textEdit_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','-apple-system','apple color emoji','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:8pt; font-weight:700; color:#515151; background-color:#ffffff;\">\u041d\u0435\u0436\u043d\u044b\u0439 \u0440\u043e\u043b\u043b \u0441 \u043a\u0440\u0435\u043c\u043e\u043e\u0431\u0440\u0430\u0437\u043d\u044b\u043c \u0441"
                        "\u044b\u0440\u043e\u043c \u0424\u0438\u043b\u0430\u0434\u0435\u043b\u044c\u0444\u0438\u044f, \u0441\u0432\u0435\u0436\u0438\u043c \u043e\u0433\u0443\u0440\u0446\u043e\u043c \u0438 \u0441\u043e\u0447\u043d\u043e\u0439 \u0440\u044b\u0431\u043e\u0439, \u0437\u0430\u0432\u0435\u0440\u043d\u0443\u0442\u044b\u0439 \u0432 \u0440\u0438\u0441 \u0438 \u043d\u043e\u0440\u0438. \u0418\u0434\u0435\u0430\u043b\u044c\u043d\u043e\u0435 \u0441\u043e\u0447\u0435\u0442\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u043e\u0432 \u0432 \u043a\u0430\u0436\u0434\u043e\u043c \u043a\u0443\u0441\u043e\u0447\u043a\u0435!</span></p></body></html>", None))
        self.textEdit_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','-apple-system','apple color emoji','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:8pt; font-weight:700; color:#515151; background-color:#ffffff;\">\u0421\u043e\u0447\u043d\u044b\u0435 \u043a\u043e\u0442\u043b\u0435\u0442\u044b \u0438\u0437 \u043c\u0440\u0430\u043c\u043e\u0440\u043d\u043e\u0439 \u0433"
                        "\u043e\u0432\u044f\u0434\u0438\u043d\u044b, \u0441\u0432\u0435\u0436\u0438\u0435 \u043e\u0432\u043e\u0449\u0438 \u0438 \u0430\u0440\u043e\u043c\u0430\u0442\u043d\u044b\u0439 \u0441\u043e\u0443\u0441, \u0437\u0430\u0432\u0435\u0440\u043d\u0443\u0442\u044b\u0435 \u0432 \u043f\u0443\u0448\u0438\u0441\u0442\u0443\u044e \u0431\u0443\u043b\u043e\u0447\u043a\u0443. \u041d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u0439 \u0444\u0430\u0441\u0442-\u0444\u0443\u0434 \u0434\u043b\u044f \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0438\u0445 \u0433\u0443\u0440\u043c\u0430\u043d\u043e\u0432!</span></p></body></html>", None))
        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','-apple-system','apple color emoji','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:8pt; font-weight:700; color:#515151; background-color:#ffffff;\">\u041a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0433\u0430\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u043d"
                        "\u0430\u043f\u0438\u0442\u043e\u043a, \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0438\u0434\u0435\u0430\u043b\u044c\u043d\u043e \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442 \u043b\u044e\u0431\u043e\u0435 \u0431\u043b\u044e\u0434\u043e. \u041e\u0441\u0432\u0435\u0436\u0430\u044e\u0449\u0435\u0435 \u0443\u0434\u043e\u0432\u043e\u043b\u044c\u0441\u0442\u0432\u0438\u0435 \u0432 \u043a\u0430\u0436\u0434\u043e\u043c \u0433\u043b\u043e\u0442\u043a\u0435!</span></p></body></html>", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto','-apple-system','apple color emoji','BlinkMacSystemFont','Segoe UI','Roboto','Oxygen-Sans','Ubuntu','Cantarell','Helvetica Neue','sans-serif'; font-size:8pt; font-weight:700; color:#515151; background-color:#ffffff;\">\u041d\u0435\u0436\u043d\u044b\u0439 \u0438 \u0441\u043b\u0430\u0434\u043a\u0438\u0439, \u0441 \u0431\u043e\u0433\u0430\u0442\u044b\u043c \u0432\u043a"
                        "\u0443\u0441\u043e\u043c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0432\u0430\u043c\u0438 \u043d\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044f \u2013 \u0438\u0434\u0435\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043f\u043e\u0441\u043e\u0431 \u043e\u0441\u0432\u0435\u0436\u0438\u0442\u044c\u0441\u044f!</span></p></body></html>", None))
        self.textEdit_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:7pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'FuturaPT'; font-size:16px; font-weight:400; color:#1f1f1f; background-color:#ffffff;\">\u0425\u043e\u0440\u043e\u0448\u0430\u044f \u0435\u0434\u0430 \u043e\u0431\u044a\u0435\u0434\u0438\u043d\u044f\u0435\u0442 \u043b\u044e\u0434\u0435\u0439!</span></p></body></html>", None))
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u" \u0420\u0430\u0431\u043e\u0442\u0430 \u0432 \u0410\u0432\u043e\u043a\u0430\u0434\u043e", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043d\u0430\u0441", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u043f\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u0437\u0430\u043a\u0430\u0437\u044b", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

