#类

# class CuteCat:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.score = {'语文':0,'数学':0,'英语':0}
    def set_score(self, course, grade):
        if course in self.score:
            self.score[course] = grade
    def print_score(self):
        print(f"学生{self.name} 学号{self.student_id} 成绩为：")
        for course in self.score:
            print(f"{course}:{self.score[course]}")

jojo=Student("Jojo","109123")
jojo.set_score("语文",80)
jojo.set_score("数学",90)
jojo.set_score("英语",85)
jojo.print_score()
#cat1=CuteCat(11,1)
#print(cat1.name)
#print(cat1.age)