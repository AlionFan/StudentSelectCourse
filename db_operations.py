import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='ADthq123',
    #password="!1004ROOTpasswd",
    database='StudentCourseSystem',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 用户验证
def verify_user(studentID, studentPassword):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM students WHERE studentID=%s AND studentPassword=%s"
        cursor.execute(sql, (studentID, studentPassword))
        result = cursor.fetchone()
        return result is not None
    
    
#新新新
#管理员验证
def verify_user_admin(adminID,adminPassword):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM administrators WHERE adminID=%s AND adminPassword=%s"
        cursor.execute(sql, (adminID, adminPassword))
        result = cursor.fetchone()
        return result is not None
#学生新增
def insert_student(studentID, studentName, studentPassword, studentMajor, studentGrade):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO students (studentID, studentName, studentPassword, studentMajor, studentGrade) VALUES ({studentID}, {studentName}, {studentPassword}, {studentMajor}, {studentGrade})")
        connection.commit()
        return "ID为"+str(studentID)+"的学生已新增"
#课程新增
def insert_student(courseID, courseName, courseNumber, courseCredit, courseTeacher, courseSchedule):
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO courses ( courseID, courseName, courseNumber, courseCredit, courseTeacher, courseSchedule) VALUES ({courseID}, {courseName}, {courseNumber}, {courseCredit}, {courseTeacher}, {courseSchedule})")
        connection.commit()
        return "课程新增成功"
#学生删除
def delete_student(studentID):
    with connection.cursor() as cursor:

        sql="DELETE FROM students WHERE studentID=%s"
        cursor.execute(sql,(studentID))
        connection.commit()
        return "ID为"+str(studentID)+"的学生已删除"
#课程删除
def delete_course(courseID):
    with connection.cursor() as cursor:
        sql="DELETE FROM courses WHERE courseID=%s"
        cursor.execute(sql,(courseID))
        connection.commit()
        return "ID为"+str(courseID)+"的课程已删除"

#新 the end

# 获取课程列表
def get_courses():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM courses"
        cursor.execute(sql)
        return cursor.fetchall()

# 获取当前选课人数
def get_number(courseID):
    
    with connection.cursor() as cursor:
        # SQL 查询语句
        sql = """
        SELECT COUNT(*) AS enrollment_count
        FROM enrollments
        WHERE courseID = %s
        """
        # 执行查询
        cursor.execute(sql, (courseID,))
        result = cursor.fetchone()
        # 返回结果
        return result['enrollment_count'] if result and result['enrollment_count'] else 0


# 选课
def enroll_course(studentID, courseID):
    with connection.cursor() as cursor:
        # 检查是否已选该课程
        sql = "SELECT * FROM enrollments WHERE studentID=%s AND courseID=%s"
        cursor.execute(sql, (studentID, courseID))
        if cursor.fetchone():
            return "您已选过该课程！"

        # 检查课程时间是否冲突
        sql = """
            SELECT c.courseSchedule FROM courses c
            JOIN enrollments e ON c.courseID = e.courseID
            WHERE e.studentID=%s
        """
        cursor.execute(sql, (studentID,))
        existing_schedules = [row['courseSchedule'] for row in cursor.fetchall()]

        # 获取新课程的时间
        sql = "SELECT courseSchedule FROM courses WHERE courseID=%s"
        cursor.execute(sql, (courseID,))
        new_schedule = cursor.fetchone()['courseSchedule']

        if new_schedule in existing_schedules:
            return "课程时间冲突，无法选课！"

        # 获取课程最大容量
        sql = "SELECT courseNumber FROM courses WHERE courseID=%s"
        cursor.execute(sql, (courseID,))
        course_info = cursor.fetchone()
        if not course_info:
            return "课程不存在！"
        max_capacity = course_info['courseNumber']

        # 判断选课人数是否达到上限
        current_count = get_number(courseID)
        if current_count >= max_capacity:
            return "选课人数已达上限，无法选课！" 

        # 插入新记录
        sql = "INSERT INTO enrollments (studentID, courseID) VALUES (%s, %s)"
        cursor.execute(sql, (studentID, courseID))
        connection.commit()
        return "选课成功！"

# 退课
def drop_course(studentID, courseID):
    with connection.cursor() as cursor:
        # 检查是否已选该课程
        sql = "SELECT * FROM enrollments WHERE studentID=%s AND courseID=%s"
        cursor.execute(sql, (studentID, courseID))
        if not cursor.fetchone():
            return "您未选该课程！"
        # 删除记录
        sql = "DELETE FROM enrollments WHERE studentID=%s AND courseID=%s"
        cursor.execute(sql, (studentID, courseID))
        connection.commit()
        return "退课成功！"

# 获取已选课程
def get_enrolled_courses(studentID):
    with connection.cursor() as cursor:
        sql = """
            SELECT c.* FROM courses c
            JOIN enrollments e ON c.courseID = e.courseID
            WHERE e.studentID=%s
        """
        cursor.execute(sql, (studentID,))
        return cursor.fetchall()
