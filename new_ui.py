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
        self.stackedWidget.setGeometry(QRect(-10, 0, 811, 601))
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
        self.adminpage = QWidget()
        self.adminpage.setObjectName(u"adminpage")
        self.addstudent = QPushButton(self.adminpage)
        self.addstudent.setObjectName(u"addstudent")
        self.addstudent.setGeometry(QRect(260, 90, 100, 32))
        self.addcourse = QPushButton(self.adminpage)
        self.addcourse.setObjectName(u"addcourse")
        self.addcourse.setGeometry(QRect(370, 370, 100, 32))
        self.studentname = QLineEdit(self.adminpage)
        self.studentname.setObjectName(u"studentname")
        self.studentname.setGeometry(QRect(10, 30, 113, 21))
        self.label = QLabel(self.adminpage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 58, 16))
        self.studentid = QLineEdit(self.adminpage)
        self.studentid.setObjectName(u"studentid")
        self.studentid.setGeometry(QRect(130, 30, 113, 21))
        self.label_3 = QLabel(self.adminpage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 10, 58, 16))
        self.studentpassword = QLineEdit(self.adminpage)
        self.studentpassword.setObjectName(u"studentpassword")
        self.studentpassword.setGeometry(QRect(250, 30, 113, 21))
        self.label_4 = QLabel(self.adminpage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 10, 58, 16))
        self.studentmajor = QLineEdit(self.adminpage)
        self.studentmajor.setObjectName(u"studentmajor")
        self.studentmajor.setGeometry(QRect(10, 90, 113, 21))
        self.label_5 = QLabel(self.adminpage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 70, 58, 16))
        self.studentgrade = QLineEdit(self.adminpage)
        self.studentgrade.setObjectName(u"studentgrade")
        self.studentgrade.setGeometry(QRect(130, 90, 113, 21))
        self.label_6 = QLabel(self.adminpage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 70, 58, 16))
        self.coursename = QLineEdit(self.adminpage)
        self.coursename.setObjectName(u"coursename")
        self.coursename.setGeometry(QRect(10, 310, 113, 21))
        self.label_7 = QLabel(self.adminpage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 290, 58, 16))
        self.label_8 = QLabel(self.adminpage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 290, 58, 16))
        self.coursenumber = QLineEdit(self.adminpage)
        self.coursenumber.setObjectName(u"coursenumber")
        self.coursenumber.setGeometry(QRect(250, 310, 113, 21))
        self.courseteacher = QLineEdit(self.adminpage)
        self.courseteacher.setObjectName(u"courseteacher")
        self.courseteacher.setGeometry(QRect(10, 370, 113, 21))
        self.label_9 = QLabel(self.adminpage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(160, 350, 58, 16))
        self.coursecredit = QLineEdit(self.adminpage)
        self.coursecredit.setObjectName(u"coursecredit")
        self.coursecredit.setGeometry(QRect(130, 370, 113, 21))
        self.label_10 = QLabel(self.adminpage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 350, 58, 16))
        self.label_11 = QLabel(self.adminpage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 290, 58, 16))
        self.courseid = QLineEdit(self.adminpage)
        self.courseid.setObjectName(u"courseid")
        self.courseid.setGeometry(QRect(130, 310, 113, 21))
        self.studenttable = QTableWidget(self.adminpage)
        if (self.studenttable.columnCount() < 4):
            self.studenttable.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.studenttable.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.studenttable.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.studenttable.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.studenttable.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.studenttable.setObjectName(u"studenttable")
        self.studenttable.setGeometry(QRect(10, 120, 411, 151))
        self.coursetable = QTableWidget(self.adminpage)
        if (self.coursetable.columnCount() < 6):
            self.coursetable.setColumnCount(6)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.coursetable.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.coursetable.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.coursetable.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.coursetable.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.coursetable.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.coursetable.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        self.coursetable.setObjectName(u"coursetable")
        self.coursetable.setGeometry(QRect(10, 410, 611, 151))
        self.label_42 = QLabel(self.adminpage)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(280, 350, 58, 16))
        self.coursedate = QLineEdit(self.adminpage)
        self.coursedate.setObjectName(u"coursedate")
        self.coursedate.setGeometry(QRect(250, 370, 113, 21))
        self.delectstudent = QPushButton(self.adminpage)
        self.delectstudent.setObjectName(u"delectstudent")
        self.delectstudent.setGeometry(QRect(390, 90, 100, 32))
        self.delectcourse = QPushButton(self.adminpage)
        self.delectcourse.setObjectName(u"delectcourse")
        self.delectcourse.setGeometry(QRect(490, 370, 100, 32))
        self.label_2 = QLabel(self.adminpage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(490, 250, 301, 111))
        self.stackedWidget.addWidget(self.adminpage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u9009\u8bfe\u7cfb\u7edf", None))
        self.labelStudentId.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7\uff1a", None))
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
        self.addstudent.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5b66\u751f", None))
        self.addcourse.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u8bfe\u7a0b", None))
        self.studentname.setText(QCoreApplication.translate("MainWindow", u"\u77f3\u5934", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.studentid.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u53f7", None))
        self.studentpassword.setText(QCoreApplication.translate("MainWindow", u"123456", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.studentmajor.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u5de5\u667a\u80fd", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u4e1a", None))
        self.studentgrade.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u7ea7", None))
        self.coursename.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93\u539f\u7406", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0bID", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u5bb9\u91cf", None))
        self.coursenumber.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.courseteacher.setText(QCoreApplication.translate("MainWindow", u"\u674e\u8001\u5e08", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u5b66\u5206", None))
        self.coursecredit.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6559\u5e08", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b", None))
        self.courseid.setText("")
        ___qtablewidgetitem12 = self.studenttable.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751fID", None));
        ___qtablewidgetitem13 = self.studenttable.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u540d", None));
        ___qtablewidgetitem14 = self.studenttable.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u4e1a", None));
        ___qtablewidgetitem15 = self.studenttable.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u7ea7", None));
        ___qtablewidgetitem16 = self.coursetable.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u540d\u79f0", None));
        ___qtablewidgetitem17 = self.coursetable.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0bID", None));
        ___qtablewidgetitem18 = self.coursetable.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u6559\u5e08", None));
        ___qtablewidgetitem19 = self.coursetable.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u5b66\u5206", None));
        ___qtablewidgetitem20 = self.coursetable.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f", None));
        ___qtablewidgetitem21 = self.coursetable.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u9009\u8bfe\u4eba\u6570", None));
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f", None))
        self.coursedate.setText(QCoreApplication.translate("MainWindow", u"\u5468\u4e09 16:00-18:00", None))
        self.delectstudent.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5b66\u751f", None))
        self.delectcourse.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u8bfe\u7a0b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; color:#ff40ff;\">\u5220\u9664\u5b66\u751f\u548c\u8bfe\u7a0b\u4ec5\u6839\u636eID\u53f7</span></p></body></html>", None))
    # retranslateUi

