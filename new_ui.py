# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 600))
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.labelStudentId = QLabel(self.loginPage)
        self.labelStudentId.setObjectName(u"labelStudentId")
        self.labelStudentId.setGeometry(QRect(200, 200, 60, 30))
        self.studentIdLineEdit = QLineEdit(self.loginPage)
        self.studentIdLineEdit.setObjectName(u"studentIdLineEdit")
        self.studentIdLineEdit.setGeometry(QRect(270, 200, 200, 30))
        self.labelPassword = QLabel(self.loginPage)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(200, 250, 60, 30))
        self.passwordLineEdit = QLineEdit(self.loginPage)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(270, 250, 200, 30))
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.loginButton = QPushButton(self.loginPage)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(320, 300, 100, 30))
        self.stackedWidget.addWidget(self.loginPage)
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.courseTableWidget = QTableWidget(self.mainPage)
        if (self.courseTableWidget.columnCount() < 12):
            self.courseTableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.courseTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.courseTableWidget.setObjectName(u"courseTableWidget")
        self.courseTableWidget.setGeometry(QRect(50, 50, 701, 200))
        self.courseTableWidget.setColumnCount(12)
        self.enrollButton = QPushButton(self.mainPage)
        self.enrollButton.setObjectName(u"enrollButton")
        self.enrollButton.setGeometry(QRect(200, 270, 100, 30))
        self.dropButton = QPushButton(self.mainPage)
        self.dropButton.setObjectName(u"dropButton")
        self.dropButton.setGeometry(QRect(350, 270, 100, 30))
        self.refreshButton = QPushButton(self.mainPage)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(500, 270, 100, 30))
        self.enrolledCourseTableWidget = QTableWidget(self.mainPage)
        if (self.enrolledCourseTableWidget.columnCount() < 6):
            self.enrolledCourseTableWidget.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.enrolledCourseTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.enrolledCourseTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.enrolledCourseTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.enrolledCourseTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.enrolledCourseTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.enrolledCourseTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.enrolledCourseTableWidget.setObjectName(u"enrolledCourseTableWidget")
        self.enrolledCourseTableWidget.setGeometry(QRect(50, 320, 700, 200))
        self.enrolledCourseTableWidget.setColumnCount(6)
        self.stackedWidget.addWidget(self.mainPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u9009\u8bfe\u7cfb\u7edf", None))
        self.labelStudentId.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u53f7\uff1a", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        ___qtablewidgetitem = self.courseTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0bID", None));
        ___qtablewidgetitem1 = self.courseTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.courseTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u5206", None));
        ___qtablewidgetitem3 = self.courseTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u6559\u5e08", None));
        ___qtablewidgetitem4 = self.courseTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u8bfe\u65f6\u95f4", None));
        ___qtablewidgetitem5 = self.courseTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u9009\u8bfe\u4eba\u6570", None));
        self.enrollButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u8bfe", None))
        self.dropButton.setText(QCoreApplication.translate("MainWindow", u"\u9000\u8bfe", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        ___qtablewidgetitem6 = self.enrolledCourseTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0bID", None));
        ___qtablewidgetitem7 = self.enrolledCourseTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u540d\u79f0", None));
        ___qtablewidgetitem8 = self.enrolledCourseTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u5206", None));
        ___qtablewidgetitem9 = self.enrolledCourseTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u6559\u5e08", None));
        ___qtablewidgetitem10 = self.enrolledCourseTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u8bfe\u65f6\u95f4", None));
        ___qtablewidgetitem11 = self.enrolledCourseTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u9009\u8bfe\u4eba\u6570", None));
    # retranslateUi

