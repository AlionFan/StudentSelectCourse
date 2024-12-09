import pymysql
 
class CreateDatabase():
    def __init__(self, new_database):
        self.new_database = new_database
 
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
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {new_database_name};")      # 执行新建数据库的SQL语句
            # 关闭游标
            cursor.close()
            # 关闭数据库连接
            connection.close()
            connection = pymysql.connect(
                host='localhost',
                user='root',
                # password='ADthq123',
                password='!1004ROOTpasswd',
                database='StudentCourseSystem',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            ssscursor=connection.cursor()
            ssscursor.execute("CREATE TABLE IF NOT EXISTS students (student_id INT PRIMARY KEY,name VARCHAR(50) NOT NULL,password VARCHAR(100) NOT NULL,major VARCHAR(50),grade VARCHAR(10));")
            ssscursor.execute("CREATE TABLE IF NOT EXISTS courses (course_id INT PRIMARY KEY,course_name VARCHAR(100) NOT NULL,credit INT,teacher VARCHAR(50),schedule VARCHAR(100));")
            ssscursor.execute("CREATE TABLE IF NOT EXISTS enrollments (id INT PRIMARY KEY AUTO_INCREMENT,student_id INT,course_id INT,FOREIGN KEY (student_id) REFERENCES students(student_id),FOREIGN KEY (course_id) REFERENCES courses(course_id));")
            ssscursor.execute("INSERT INTO courses (course_id, course_name, credit, teacher, schedule,courseNumber) VALUES(1, '高等数学', 4, '王老师', '周一 8:00-10:00',0),(2, '大学英语', 2, '李老师', '周二 10:00-12:00',0),(3, '数据结构', 3, '张老师', '周三 14:00-16:00',0);")
            ssscursor.execute("INSERT INTO students (student_id, name, password, major, grade) VALUES(2021001, '张三', 'passwd001', '计算机科学', '2021'),(2021002, '李四', 'passwd002', '电子工程', '2021');")
            connection.commit()
            return
        else:
            cursor.close()
            # 关闭数据库连接
            connection.close()
        

def new_create(remake=1):
    try:
        CreateDatabase('database_test').create_new_database(remake)
 
    except pymysql.Error as e:
        print(f'新建数据库失败，{e}')