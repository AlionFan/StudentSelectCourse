CREATE DATABASE IF NOT EXISTS StudentCourseSystem;
USE StudentCourseSystem;

-- 学生表
CREATE TABLE IF NOT EXISTS students (
    studentID 			INT UNIQUE PRIMARY KEY,
    studentName 		VARCHAR(50) NOT NULL,
    studentPassword 	VARCHAR(100) NOT NULL,
    studentMajor 		VARCHAR(50),
    studentGrade		YEAR
);

-- 课程表
CREATE TABLE IF NOT EXISTS courses (
    courseID 			INT UNIQUE PRIMARY KEY,
    courseName 			VARCHAR(100) NOT NULL,
    courseNumber		INT NOT NULL,
    courseCredit		INT,
    courseTeacher 		VARCHAR(50),
    courseSchedule 		VARCHAR(100)
);


-- 教师表 
-- CREATE TABLE IF NOT EXISTS teachers (
-- 	teacherID			INT			 PRIMARY KEY,
--     teacherName			VARCHAR(50)  NOT NULL,
--     teacherPassword		VARCHAR(100) NOT NULL,
--     teacherEmail		VARCHAR(100)
-- );

-- 选课表
CREATE TABLE IF NOT EXISTS enrollments (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    studentID INT,
    courseID INT,
    FOREIGN KEY (studentID) REFERENCES students(studentID),
    FOREIGN KEY (courseID) REFERENCES courses(courseID)
);


-- 插入示例课程数据
INSERT INTO courses (courseID, courseName, courseNumber, courseCredit, courseTeacher, courseSchedule) VALUES
(1, '高等数学', 40, 4, '王老师', '周一 8:00-10:00'),
(2, '大学英语', 16, 2, '李老师', '周二 10:00-12:00'),
(3, '数据结构', 5, 3,  '张老师', '周三 14:00-16:00'),
(4, '线性代数', 6, 2,  '赵老师', '周一 10:00-12:00'),
(5, '概率论与数理统计', 6, 3, '钱老师', '周二 8:00-10:00'),
(6, '计算机组成原理', 6, 4, '孙老师', '周三 8:00-10:00'),
(7, '操作系统',6,  3, '周老师', '周四 10:00-12:00'),
(8, '数据库原理',6,  2, '吴老师', '周五 14:00-16:00'),
(9, '人工智能导论',6, 2, '郑老师', '周一 14:00-16:00'),
(10, '机器学习', 6,4, '王老师', '周二 14:00-16:00'),
(11, '模式识别', 6,3, '李老师', '周三 10:00-12:00'),
(12, '深度学习', 6,2, '张老师', '周四 8:00-10:00'),
(13, '计算机视觉', 6,3, '赵老师', '周五 8:00-10:00'),
(14, '自然语言处理', 6,3, '钱老师', '周一 16:00-18:00'),
(15, '算法分析与设计',6, 3, '孙老师', '周二 16:00-18:00'),
(16, '离散数学', 6,3, '周老师', '周三 16:00-18:00'),
(17, '计算机网络',6, 3, '吴老师', '周四 14:00-16:00'),
(18, '软件工程', 6,2, '郑老师', '周五 10:00-12:00'),
(19, '编译原理', 6,3, '王老师', '周一 10:00-12:00'),
(20, '计算机图形学',6, 3, '李老师', '周二 8:00-10:00'),
(21, '高等数学',6, 4, '张老师', '周三 8:00-10:00'),
(22, '线性代数',6, 3, '赵老师', '周四 10:00-12:00'),
(23, '概率论与数理统计',6, 3, '钱老师', '周五 14:00-16:00'),
(24, '计算机组成原理',6, 2, '孙老师', '周一 14:00-16:00'),
(25, '操作系统',6, 3, '周老师', '周二 14:00-16:00'),
(26, '数据库原理',6, 3, '吴老师', '周三 10:00-12:00'),
(27, '人工智能导论', 6,2, '郑老师', '周四 8:00-10:00'),
(28, '机器学习',6, 4, '王老师', '周五 8:00-10:00'),
(29, '模式识别',6, 3, '李老师', '周一 16:00-18:00'),
(30, '深度学习',6, 2, '张老师', '周二 16:00-18:00'),
(31, '计算机视觉',6, 3, '赵老师', '周三 16:00-18:00'),
(32, '自然语言处理',6, 3, '钱老师', '周四 14:00-16:00'),
(33, '算法分析与设计',6, 3, '孙老师', '周五 10:00-12:00'),
(34, '离散数学',6, 3, '周老师', '周一 10:00-12:00'),
(35, '计算机网络', 6,2, '吴老师', '周二 8:00-10:00'),
(36, '软件工程', 6,3, '郑老师', '周三 8:00-10:00'),
(37, '编译原理', 6,2, '王老师', '周四 10:00-12:00'),
(38, '计算机图形学', 6,3, '李老师', '周五 14:00-16:00'),
(39, '高等数学', 6,4, '张老师', '周一 14:00-16:00'),
(40, '线性代数', 6,3, '刘老师' , '周五 14:00-16:00');


INSERT INTO students (studentID, studentName, studentPassword, studentMajor, studentGrade) VALUES
(2022001, '张三', 'passwd001', '计算机科学', 2022),
(2022002, '李四', 'passwd002', '电子工程', 2022),
(2021001, '赵瑾瑜', 'passwd001', '计算机科学', 2021),
(2021002, '钱浩然', 'passwd002', '电子工程', 2021),
(2021003, '孙思远', 'passwd003', '人工智能', 2021),
(2021004, '李晓蕾', 'passwd004', '软件工程', 2021),
(2021005, '周芷若', 'passwd005', '计算机科学', 2021),
(2021006, '吴文轩', 'passwd006', '电子工程', 2021),
(2021007, '郑雅婷', 'passwd007', '人工智能', 2021),
(2021008, '王梓轩', 'passwd008', '软件工程', 2021),
(2021009, '冯嘉熙', 'passwd009', '计算机科学', 2021),
(2021010, '陈思敏', 'passwd010', '电子工程', 2021),
(2021011, '褚子涵', 'passwd011', '人工智能', 2021),
(2021012, '卫子夫', 'passwd012', '软件工程', 2021),
(2021013, '蒋梦婕', 'passwd013', '计算机科学', 2021),
(2021014, '沈涛', 'passwd014', '电子工程', 2021),
(2021015, '韩雪', 'passwd015', '人工智能', 2021),
(2021016, '杨洋', 'passwd016', '软件工程', 2021),
(2021017, '朱一龙', 'passwd017', '计算机科学', 2021),
(2021018, '秦岚', 'passwd018', '电子工程', 2021),
(2021019, '尤靖茹', 'passwd019', '人工智能', 2021),
(2021020, '许凯', 'passwd020', '软件工程', 2021),
(2021021, '罗云熙', 'passwd021', '计算机科学', 2021),
(2021022, '邓紫棋', 'passwd022', '电子工程', 2021),
(2021023, '韩孝周', 'passwd023', '人工智能', 2021),
(2021024, '谢霆锋', 'passwd024', '软件工程', 2021),
(2021025, '冯绍峰', 'passwd025', '计算机科学', 2021),
(2021026, '沈腾', 'passwd026', '电子工程', 2021),
(2021027, '汪峰', 'passwd027', '人工智能', 2021),
(2021028, '程瑶瑶', 'passwd028', '软件工程', 2021),
(2021029, '曹曦文', 'passwd029', '计算机科学', 2021),
(2021030, '严宽', 'passwd030', '电子工程', 2021),
(2021031, '金瀚', 'passwd031', '人工智能', 2021),
(2021032, '魏晨', 'passwd032', '软件工程', 2021),
(2021033, '陶虹', 'passwd033', '计算机科学', 2021),
(2021034, '姜潮', 'passwd034', '电子工程', 2021),
(2021035, '戚薇', 'passwd035', '人工智能', 2021),
(2021036, '谢楠', 'passwd036', '软件工程', 2021),
(2021037, '邹市明', 'passwd037', '计算机科学', 2021),
(2021038, '喻恩泰', 'passwd038', '电子工程', 2021),
(2021039, '柏雪', 'passwd039', '人工智能', 2021),
(2021040, '水原希子', 'passwd040', '软件工程', 2021),
(2021041, '窦骁', 'passwd041', '计算机科学', 2021),
(2021042, '章子怡', 'passwd042', '电子工程', 2021),
(2021043, '云朵', 'passwd043', '人工智能', 2021),
(2021044, '苏醒', 'passwd044', '软件工程', 2021);




-- LOAD DATA INFILE './Data/StudentData.txt'
-- INTO TABLE students
-- FIELDS TERMINATED BY ',' ENCLOSED BY '\''
-- LINES TERMINATED BY '\n'
-- (studentID, studentName, studentPassword, studentMajor, studentGrade);


-- LOAD DATA INFILE './Data/CourseData.txt'
-- INTO TABLE courses
-- FIELDS TERMINATED BY ',' ENCLOSED BY '\''
-- LINES TERMINATED BY '\n'
-- (courseID, courseName, courseNumber, courseCredit, courseTeacher, courseSchedule);
