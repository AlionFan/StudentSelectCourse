import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password="!1004ROOTpasswd",
    database='StudentCourseSystem',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def insert_course(courseID, courseName, courseNumber, courseCredit, courseTeacher, courseSchedule):
    with connection.cursor() as cursor:
        sql = """
        INSERT INTO courses (
            courseID,
            courseName,
            courseNumber,
            courseCredit,
            courseTeacher,
            courseSchedule
        ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (courseID, courseName, courseNumber, courseCredit, courseTeacher, courseSchedule))
        connection.commit()
        return "课程新增成功"

def insert_student(studentID, studentName, studentPassword, studentMajor, studentGrade):
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO students (
                studentID, 
                studentName, 
                studentPassword, 
                studentMajor, 
                studentGrade) 
                VALUES (%s, %s, %s, %s, %s)
            """
        cursor.execute(sql, (studentID, studentName, studentPassword, studentMajor, studentGrade))
        connection.commit()
        return "ID为"+str(studentID)+"的学生已新增"
    
result = insert_student("2021000", "石头", "123456", "人工智能", "2021")
print(result)
# 示例调用
# result = insert_course()
# print(result)