class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def greet(self):

        print(f"你好，我是{self.name}!")

    def get_grade(self):
        if self.score >= 90:
            return "excellent"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"

    def introduce(self):
        grade = self.get_grade()
        print(f"我叫{self.name}, 我的成绩{grade}.")


s1 = Student("小明", 92)

s1.greet()
s1.introduce()
print(s1.get_grade())
