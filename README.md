# 学生选课系统介绍

## 仓库说明
本仓库用于2024学年秋季学期 首都师范大学《数据库原理课程》大作业，内容由第5组编写及使用。

README.md中代码并非仓库完整代码，仅为demo样例。
## 开发环境
+ 数据库：Mysql9.0
+ 后端交互： Pymysql
+ 前端界面： pyside6 + designer


+ 开发工具： VScode
+ 开发语言： Python3.12.7

环境配置：
```bash
cd ~
mkdir venv
cd venv
sudo apt install python@3.12  python3.12-venv
source ./bin/activate
pip install -r requirements.txt
```

运行
```bash
python main.py
```
**登陆学号和密码在mysql代码中标注++
|学号|密码|
|---|---|
|2021001|passwd001|
|2021002|passwd002|

**选课退课需要全选当前行**
## 功能介绍

### 登录
+ 输入学号和密码，点击登录按钮，系统会验证输入的学号和密码是否正确，如果正确则进入系统，否则提示错误信息。

+ 可以进行选课和退课操作。
  + 选课退课有最大选课人数，每次选课都会刷新当前选课人数，达到最大人数无法选课
  + 选课有时间冲突判断，不能选择上课时间相同的两门课
  + 已经选的课无法再次选择
  + 只有选的课才能进行退课操作


## 代码
### mysql
```sql
CREATE DATABASE IF NOT EXISTS StudentCourseSystem;
USE StudentCourseSystem;

-- 学生表
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    major VARCHAR(50),
    grade VARCHAR(10)
);

-- 课程表
CREATE TABLE IF NOT EXISTS courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credit INT,
    teacher VARCHAR(50),
    schedule VARCHAR(100)
);

-- 选课表
CREATE TABLE IF NOT EXISTS enrollments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


-- 插入示例课程数据
INSERT INTO courses (course_id, course_name, credit, teacher, schedule) VALUES
(1, '高等数学', 4, '王老师', '周一 8:00-10:00'),
(2, '大学英语', 2, '李老师', '周二 10:00-12:00'),
(3, '数据结构', 3, '张老师', '周三 14:00-16:00');


INSERT INTO students (student_id, name, password, major, grade) VALUES
(2021001, '张三', 'passwd001', '计算机科学', '2021'),
(2021002, '李四', 'passwd002', '电子工程', '2021');
```

### pymysql后端代码(注意修改第6行的密码)

```python
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='your_passwd',    # 这里需要替换成你的密码
    database='StudentCourseSystem',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 用户验证
def verify_user(student_id, password):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM students WHERE student_id=%s AND password=%s"
        cursor.execute(sql, (student_id, password))
        result = cursor.fetchone()
        return result is not None
    
# 获取课程信息
# def get_courses():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM courses"
        cursor.execute(sql)
        return cursor.fetchall()
    
# 选课
# def enroll_course(student_id, course_id):
    with connection.cursor() as cursor:
        # 检查是否已选该课程
        sql = "SELECT * FROM enrollments WHERE student_id=%s AND course_id=%s"
        cursor.execute(sql, (student_id, course_id))
        if cursor.fetchone():
            return "您已选过该课程！"

        # 检查课程时间是否冲突
        sql = """
            SELECT c.schedule FROM courses c
            JOIN enrollments e ON c.course_id = e.course_id
            WHERE e.student_id=%s
        """
        cursor.execute(sql, (student_id,))
        existing_schedules = [row['schedule'] for row in cursor.fetchall()]

        # 获取新课程的时间
        sql = "SELECT schedule FROM courses WHERE course_id=%s"
        cursor.execute(sql, (course_id,))
        new_schedule = cursor.fetchone()['schedule']

        if new_schedule in existing_schedules:
            return "课程时间冲突，无法选课！"

        # 插入新记录
        sql = "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)"
        cursor.execute(sql, (student_id, course_id))
        connection.commit()
        return "选课成功！"
    
# 退课
# def drop_course(student_id, course_id):
    with connection.cursor() as cursor:
        # 检查是否已选该课程
        sql = "SELECT * FROM enrollments WHERE student_id=%s AND course_id=%s"
        cursor.execute(sql, (student_id, course_id))
        if not cursor.fetchone():
            return "您未选该课程！"
        # 删除记录
        sql = "DELETE FROM enrollments WHERE student_id=%s AND course_id=%s"
        cursor.execute(sql, (student_id, course_id))
        connection.commit()
        return "退课成功！"
    
# def get_enrolled_courses(student_id):
    with connection.cursor() as cursor:
        sql = """
            SELECT c.* FROM courses c
            JOIN enrollments e ON c.course_id = e.course_id
            WHERE e.student_id=%s
        """
        cursor.execute(sql, (student_id,))
        return cursor.fetchall()


# 获取课程列表
def get_courses():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM courses"
        cursor.execute(sql)
        return cursor.fetchall()

# 选课
def enroll_course(student_id, course_id):
    with connection.cursor() as cursor:
        # 检查是否已选该课程
        sql = "SELECT * FROM enrollments WHERE student_id=%s AND course_id=%s"
        cursor.execute(sql, (student_id, course_id))
        if cursor.fetchone():
            return "您已选过该课程！"

        # 检查课程时间是否冲突（可选）
        sql = """
            SELECT c.schedule FROM courses c
            JOIN enrollments e ON c.course_id = e.course_id
            WHERE e.student_id=%s
        """
        cursor.execute(sql, (student_id,))
        existing_schedules = [row['schedule'] for row in cursor.fetchall()]

        # 获取新课程的时间
        sql = "SELECT schedule FROM courses WHERE course_id=%s"
        cursor.execute(sql, (course_id,))
        new_schedule = cursor.fetchone()['schedule']

        if new_schedule in existing_schedules:
            return "课程时间冲突，无法选课！"

        # 插入新记录
        sql = "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)"
        cursor.execute(sql, (student_id, course_id))
        connection.commit()
        return "选课成功！"

# 退课
def drop_course(student_id, course_id):
    with connection.cursor() as cursor:
        # 检查是否已选该课程
        sql = "SELECT * FROM enrollments WHERE student_id=%s AND course_id=%s"
        cursor.execute(sql, (student_id, course_id))
        if not cursor.fetchone():
            return "您未选该课程！"
        # 删除记录
        sql = "DELETE FROM enrollments WHERE student_id=%s AND course_id=%s"
        cursor.execute(sql, (student_id, course_id))
        connection.commit()
        return "退课成功！"

# 获取已选课程
def get_enrolled_courses(student_id):
    with connection.cursor() as cursor:
        sql = """
            SELECT c.* FROM courses c
            JOIN enrollments e ON c.course_id = e.course_id
            WHERE e.student_id=%s
        """
        cursor.execute(sql, (student_id,))
        return cursor.fetchall()
```

### 前端界面new_ui.ui
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>学生选课系统</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QStackedWidget" name="stackedWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>800</width>
      <height>600</height>
     </rect>
    </property>
    <!-- 登录界面 -->
    <widget class="QWidget" name="loginPage">
     <widget class="QLabel" name="labelStudentId">
      <property name="text">
       <string>学号：</string>
      </property>
      <property name="geometry">
       <rect>
        <x>200</x>
        <y>200</y>
        <width>60</width>
        <height>30</height>
       </rect>
      </property>
     </widget>
     <widget class="QLineEdit" name="studentIdLineEdit">
      <property name="geometry">
       <rect>
        <x>270</x>
        <y>200</y>
        <width>200</width>
        <height>30</height>
       </rect>
      </property>
     </widget>
     <widget class="QLabel" name="labelPassword">
      <property name="text">
       <string>密码：</string>
      </property>
      <property name="geometry">
       <rect>
        <x>200</x>
        <y>250</y>
        <width>60</width>
        <height>30</height>
       </rect>
      </property>
     </widget>
     <widget class="QLineEdit" name="passwordLineEdit">
      <property name="geometry">
       <rect>
        <x>270</x>
        <y>250</y>
        <width>200</width>
        <height>30</height>
       </rect>
      </property>
      <property name="echoMode">
       <enum>QLineEdit::Password</enum>
      </property>
     </widget>
     <widget class="QPushButton" name="loginButton">
      <property name="text">
       <string>登录</string>
      </property>
      <property name="geometry">
       <rect>
        <x>320</x>
        <y>300</y>
        <width>100</width>
        <height>30</height>
       </rect>
      </property>
     </widget>
    </widget>
    <!-- 主界面 -->
    <widget class="QWidget" name="mainPage">
     <widget class="QTableWidget" name="courseTableWidget">
      <property name="geometry">
       <rect>
        <x>50</x>
        <y>50</y>
        <width>700</width>
        <height>200</height>
       </rect>
      </property>
      <property name="columnCount">
       <number>5</number>
      </property>
      <column>
       <property name="text">
        <string>课程ID</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>课程名称</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>学分</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>教师</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>时间</string>
       </property>
      </column>
     </widget>
     <widget class="QPushButton" name="enrollButton">
      <property name="text">
       <string>选课</string>
      </property>
      <property name="geometry">
       <rect>
        <x>200</x>
        <y>270</y>
        <width>100</width>
        <height>30</height>
       </rect>
      </property>
     </widget>
     <widget class="QPushButton" name="dropButton">
      <property name="text">
       <string>退课</string>
      </property>
      <property name="geometry">
       <rect>
        <x>350</x>
        <y>270</y>
        <width>100</width>
        <height>30</height>
       </rect>
      </property>
     </widget>
     <widget class="QPushButton" name="refreshButton">
      <property name="text">
       <string>刷新</string>
      </property>
      <property name="geometry">
       <rect>
        <x>500</x>
        <y>270</y>
        <width>100</width>
        <height>30</height>
       </rect>
      </property>
     </widget>
     <widget class="QTableWidget" name="enrolledCourseTableWidget">
      <property name="geometry">
       <rect>
        <x>50</x>
        <y>320</y>
        <width>700</width>
        <height>200</height>
       </rect>
      </property>
      <property name="columnCount">
       <number>5</number>
      </property>
      <column>
       <property name="text">
        <string>课程ID</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>课程名称</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>学分</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>教师</string>
       </property>
      </column>
      <column>
       <property name="text">
        <string>时间</string>
       </property>
      </column>
     </widget>
    </widget>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
```
### 前端代码转换
```bash
pyside6-uic new_ui.ui -o new_ui.py
```

### 主函数main.py
```python
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from new_ui import Ui_MainWindow  # 导入生成的UI类
import db_operations

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.student_id = None  # 初始化学生ID
        self.bind_events()
        self.stackedWidget.setCurrentIndex(0)  # 显示登录界面

    def bind_events(self):
        # 登录界面按钮事件
        self.loginButton.clicked.connect(self.login)

        # 选课界面按钮事件
        self.enrollButton.clicked.connect(self.enroll_course)
        self.dropButton.clicked.connect(self.drop_course)
        self.refreshButton.clicked.connect(self.load_courses)

    def login(self):
        student_id = self.studentIdLineEdit.text()
        password = self.passwordLineEdit.text()
        if db_operations.verify_user(student_id, password):
            QMessageBox.information(self, "成功", "登录成功")
            self.student_id = student_id  # 保存学生ID
            self.load_courses()           # 加载课程列表
            self.load_enrolled_courses()  # 加载已选课程列表
            self.stackedWidget.setCurrentIndex(1)  # 切换到主界面
        else:
            QMessageBox.warning(self, "错误", "学号或密码错误")

    def load_courses(self):
        courses = db_operations.get_courses()
        self.courseTableWidget.setRowCount(len(courses))
        for row_num, course in enumerate(courses):
            self.courseTableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(course['course_id'])))
            self.courseTableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(course['course_name']))
            self.courseTableWidget.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(course['credit'])))
            self.courseTableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(course['teacher']))
            self.courseTableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(course['schedule']))

    def load_enrolled_courses(self):
        courses = db_operations.get_enrolled_courses(self.student_id)
        self.enrolledCourseTableWidget.setRowCount(len(courses))
        for row_num, course in enumerate(courses):
            self.enrolledCourseTableWidget.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(course['course_id'])))
            self.enrolledCourseTableWidget.setItem(row_num, 1, QtWidgets.QTableWidgetItem(course['course_name']))
            self.enrolledCourseTableWidget.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(course['credit'])))
            self.enrolledCourseTableWidget.setItem(row_num, 3, QtWidgets.QTableWidgetItem(course['teacher']))
            self.enrolledCourseTableWidget.setItem(row_num, 4, QtWidgets.QTableWidgetItem(course['schedule']))

    def enroll_course(self):
        selected_items = self.courseTableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "提示", "请先选择一门课程！")
            return
        course_id = selected_items[0].text()  # 假设课程ID在第0列
        result = db_operations.enroll_course(self.student_id, course_id)
        QMessageBox.information(self, "选课结果", result)
        self.load_enrolled_courses()  # 更新已选课程列表

    def drop_course(self):
        selected_items = self.enrolledCourseTableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "提示", "请先选择一门课程！")
            return
        course_id = selected_items[0].text()
        result = db_operations.drop_course(self.student_id, course_id)
        QMessageBox.information(self, "退课结果", result)
        self.load_enrolled_courses()  # 更新已选课程列表

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

```
