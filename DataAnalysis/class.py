# 是创建对象得模板
# 对象是类的实例
# 类定义了对象有何种属性和方法
# 对象拥有的具体属性可以不尽相同

# 定义一个学生类
# 要求：
# 1. 属性包括学生姓名、学号，以及语数英三科的成绩
# 2. 能够设置学生某科目的成绩
# 3. 能够打印出该学生的所有科目成绩

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文":0, "数学":0, "英语":0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name} (学号):{self.student_id}) 的成绩为：")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}分")



chen = Student("amy",'1000')
chen.set_grade("数学", 69)
print(chen.name)
print(chen.grades)
chen.print_grades()

