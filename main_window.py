
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(683, 360)
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input = QLabel(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(10, 20, 321, 231))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.input.setFont(font1)
        self.input.setScaledContents(True)
        self.output = QLabel(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(360, 20, 311, 231))
        self.output.setFont(font1)
        self.output.setScaledContents(True)
        self.output.setWordWrap(False)
        self.output.setOpenExternalLinks(True)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(335, 20, 20, 231))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.imgButton = QPushButton(self.centralwidget)
        self.imgButton.setObjectName(u"imgButton")
        self.imgButton.setGeometry(QRect(290, 260, 111, 31))
        self.videoButton = QPushButton(self.centralwidget)
        self.videoButton.setObjectName(u"videoButton")
        self.videoButton.setGeometry(QRect(290, 300, 111, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"电动车头盔佩戴检测系统——2023毕业设计", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"                        \u539f\u59cb\u56fe\u50cf", None))
        self.output.setText(QCoreApplication.translate("MainWindow", u"                        \u68c0\u6d4b\u56fe\u50cf", None))
        self.imgButton.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u68c0\u6d4b", None))
        self.videoButton.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u68c0\u6d4b", None))
    # retranslateUi

