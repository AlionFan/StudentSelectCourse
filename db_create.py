import pymysql

class CreateDatabase():
    def __init__(self, new_database):
        self.new_database = new_database
    def str_quyinhao(self,a):
        return a[1:len(a)-1]
    def create_new_database(self,remake=1):
        #remake:初始化参数 remake=0时初始化
        # 建立数据库连接
        connection = pymysql.connect(
            host='localhost',
            user='root',
            # password='ADthq123',
            password='!1004ROOTpasswd',
            cursorclass=pymysql.cursors.DictCursor
        )
 
        # 创建新数据库
        new_database_name = self.new_database
        cursor = connection.cursor()    # 创建游标对象
        cursor.execute("SHOW DATABASES;")
        dbnames=cursor.fetchall()

        db_ex=any(new_database_name in dbname for dbname in dbnames)
        if db_ex ==True or remake==0:
            if remake==0:
                cursor.execute(f"DROP DATABASE IF EXISTS {new_database_name};")#删除
                connection.commit()
                #print("删除成功")
                #cursor.execute("SHOW DATABASES;")
                #dbnames=cursor.fetchall()
                #for i in dbnames:
                    #print(i)

            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {new_database_name};")      # 执行新建数据库的SQL语句
            cursor.close()
            # 关闭数据库连接
            connection.close()
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='ADthq123',
                #password='!1004ROOTpasswd',
                database='StudentCourseSystem',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            ssscursor=connection.cursor()
            ssscursor.execute("CREATE TABLE IF NOT EXISTS students ( studentID INT UNIQUE PRIMARY KEY,studentName VARCHAR(50) NOT NULL,studentPassword VARCHAR(100) NOT NULL,studentMajor VARCHAR(50),studentGrade YEAR);")
            ssscursor.execute("CREATE TABLE IF NOT EXISTS courses ( courseID INT UNIQUE PRIMARY KEY, courseName 	VARCHAR(100) NOT NULL,courseNumber	INT NOT NULL,courseCredit INT,courseTeacher VARCHAR(50),courseSchedule VARCHAR(100));")
            ssscursor.execute("CREATE TABLE IF NOT EXISTS enrollments ( ID INT PRIMARY KEY AUTO_INCREMENT,studentID INT,courseID INT,FOREIGN KEY (studentID) REFERENCES students(studentID),FOREIGN KEY (courseID) REFERENCES courses(courseID));")
            ssscursor.execute("CREATE TABLE IF NOT EXISTS administrators (adminID INT UNIQUE PRIMARY KEY,adminPassword VARCHAR(100) NOT NULL);")
            ssscursor.execute("INSERT INTO administrators (adminID,adminPassword) VALUES (1001,'admin');")
            connection.commit()
            with open('./Data/CourseData.txt', 'r',encoding='utf-8') as file:
                for line in file.readlines():
                    courseID, courseName, courseNumber, courseCredit, courseTeacher, courseSchedule=line.split(',')
                    courseID=int(courseID)
                    #courseName=self.str_quyinhao(courseName)
                    #courseTeacher=self.str_quyinhao(courseTeacher)
                    #courseSchedule=courseSchedule[1:len(courseSchedule)-2]
                    courseNumber=int(courseNumber)
                    courseCredit=int(courseCredit)
                    ssscursor.execute(f"INSERT INTO courses ( courseID, courseName, courseNumber, courseCredit, courseTeacher, courseSchedule) VALUES ({courseID}, {courseName}, {courseNumber}, {courseCredit}, {courseTeacher}, {courseSchedule})")
            with open('./Data/StudentData.txt', 'r',encoding='utf-8') as file:
                for line in file.readlines():
                    studentID, studentName, studentPassword, studentMajor, studentGrade=line.split(',')
                    studentID=int(studentID)
                    #studentName=self.str_quyinhao(studentName)
                    #studentPassword=self.str_quyinhao(studentPassword)
                    #studentMajor=self.str_quyinhao(studentMajor)
                    studentGrade=int(studentGrade)
                    ssscursor.execute(f"INSERT INTO students (studentID, studentName, studentPassword, studentMajor, studentGrade) VALUES ({studentID}, {studentName}, {studentPassword}, {studentMajor}, {studentGrade})")
            #ssscursor.execute("")
            connection.commit()

            return
        else:
            cursor.close()
            # 关闭数据库连接
            connection.close()
        

def new_create(remake=1):
    try:
        CreateDatabase('StudentCourseSystem').create_new_database(remake)
 
    except pymysql.Error as e:
        print(f'新建数据库失败，{e}')