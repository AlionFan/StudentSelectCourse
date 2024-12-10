import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from new_ui import Ui_MainWindow  # 导入生成的UI类
import db_operations
import db_create
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.studentID = None  # 初始化学生ID
        self.bind_events()
        self.stackedWidget.setCurrentIndex(0)  # 显示登录界面

    def bind_events(self):
        # 登录界面按钮事件
        self.loginButton.clicked.connect(self.login)

        # 选课界面按钮事件
        self.enrollButton.clicked.connect(self.enroll_course)
        self.dropButton.clicked.connect(self.drop_course)
        self.refreshButton.clicked.connect(self.load_courses)
        self.addstudent.clicked.connect(self.insert_student)
        self.addcourse.clicked.connect(self.insert_course)
        self.delectstudent.clicked.connect(self.drop_student)
        self.delectcourse.clicked.connect(self.drop_course_admin)

    def login(self):
        studentID = self.studentIdLineEdit.text()
        studentPassword = self.passwordLineEdit.text()
        if len(studentID) == 7:
            if db_operations.verify_user(studentID, studentPassword):
                QMessageBox.information(self, "成功", "登录成功")
                self.studentID = studentID  # 保存学生ID
                self.load_courses()           # 加载课程列表
                self.load_enrolled_courses()  # 加载已选课程列表
                self.stackedWidget.setCurrentIndex(1)  # 切换到主界面
            else:
                QMessageBox.warning(self, "错误", "账号或密码错误")
        else:
            if db_operations.verify_user_admin(studentID, studentPassword):
                QMessageBox.information(self, "成功", "登录成功")
                self.studentID = studentID  # 保存学生ID
                self.load_students()         # 加载课程列表
                self.load_courses_admin()  # 加载已选课程列表
                self.stackedWidget.setCurrentIndex(2)  # 切换到主界面

    def load_courses(self):
        courses = db_operations.get_courses()
        self.courseTableWidget.setRowCount(len(courses))
        for row_num, course in enumerate(courses):
            num = db_operations.get_number(course["courseID"])
            self.courseTableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(course['courseID'])))
            self.courseTableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(course['courseName']))
            self.courseTableWidget.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(course['courseCredit'])))
            self.courseTableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(course['courseTeacher']))
            self.courseTableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(course['courseSchedule']))
            self.courseTableWidget.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(num) + " / " + str(course['courseNumber'])))

    def load_courses_admin(self):
        courses = db_operations.get_courses()
        self.coursetable.setRowCount(len(courses))
        for row_num, course in enumerate(courses):
            num = db_operations.get_number(course["courseID"])
            self.coursetable.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(course['courseID'])))
            self.coursetable.setItem(row_num, 0, QtWidgets.QTableWidgetItem(course['courseName']))
            self.coursetable.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(course['courseCredit'])))
            self.coursetable.setItem(row_num, 2, QtWidgets.QTableWidgetItem(course['courseTeacher']))
            self.coursetable.setItem(row_num, 4, QtWidgets.QTableWidgetItem(course['courseSchedule']))
            self.coursetable.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(num) + " / " + str(course['courseNumber'])))

    def load_students(self):
        students = db_operations.get_students()
        self.studenttable.setRowCount(len(students))
        for row_num, student in enumerate(students):
            self.studenttable.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(student['studentID'])))
            self.studenttable.setItem(row_num, 1, QtWidgets.QTableWidgetItem(student['studentName']))
            self.studenttable.setItem(row_num, 2, QtWidgets.QTableWidgetItem(student['studentMajor']))
            self.studenttable.setItem(row_num, 3, QtWidgets.QTableWidgetItem(str(student['studentGrade'])))

    def insert_student(self):
        sid = int(self.studentid.text())
        sname = self.studentname.text()
        sgrade = self.studentgrade.text()
        smajor = self.studentmajor.text()
        spasswd = self.studentpassword.text()
        # print(sid, type(sid), sname, type(sname), sgrade, type(sgrade), smajor, type(smajor), spasswd, type(spasswd))

        print(db_operations.insert_student(int(sid), sname, spasswd, smajor, sgrade))
        # print("插入学生！")
        self.load_students()

    def insert_course(self):
        cid = self.courseid.text()
        cname = self.coursename.text()
        cteacher = self.courseteacher.text()
        ccredit = self.coursecredit.text()
        cdate = self.coursedate.text()
        cnum = self.coursenumber.text()
        print(db_operations.insert_course(cid, cname, cnum, ccredit, cteacher, cdate))
        self.load_courses_admin()
    
    def drop_student(self):
        sid = self.studentid.text()
        print(db_operations.delete_student(sid))
        self.load_students()

    def drop_course_admin(self):
        cid = self.courseid.text()
        print(db_operations.delete_course(cid))
        self.load_courses_admin()

    def load_enrolled_courses(self):
        courses = db_operations.get_enrolled_courses(self.studentID)
        self.enrolledCourseTableWidget.setRowCount(len(courses))
        for row_num, course in enumerate(courses):
            num = db_operations.get_number(course["courseID"])
            self.enrolledCourseTableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(course['courseID'])))
            self.enrolledCourseTableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(course['courseName']))
            self.enrolledCourseTableWidget.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(course['courseCredit'])))
            self.enrolledCourseTableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(course['courseTeacher']))
            self.enrolledCourseTableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(course['courseSchedule']))
            self.enrolledCourseTableWidget.setItem(row_num, 5, QtWidgets.QTableWidgetItem(str(num) + " / " + str(course['courseNumber'])))


    def enroll_course(self):
        selected_items = self.courseTableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "提示", "请先选择一门课程！")
            return
        courseID = selected_items[0].text()  # 假设课程ID在第0列
        result = db_operations.enroll_course(self.studentID, courseID)
        QMessageBox.information(self, "选课结果", result)
        self.load_courses()
        self.load_enrolled_courses()  # 更新已选课程列表

    def drop_course(self):
        selected_items = self.enrolledCourseTableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "提示", "请先选择一门课程！")
            return
        courseID = selected_items[0].text()
        result = db_operations.drop_course(self.studentID, courseID)
        QMessageBox.information(self, "退课结果", result)
        self.load_courses()
        self.load_enrolled_courses()  # 更新已选课程列表

if __name__ == "__main__":
    db_create.new_create()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())