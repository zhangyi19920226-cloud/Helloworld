类 (class)模板/蓝图class Student:对象/实例根据类创建的具体个体s1 = Student(...)属性对象存储的数据self.name, self.score方法对象能执行的操作def greet(self):__init__构造方法，创建时自动调用def __init__(self, ...):self指代当前对象本身每个方法的第一个参数
class Person:
    def __init__(self, name ,age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"我叫{self.name}, 今年{self.age}岁")

class Student(Person):
    def __init___(self, name,age,score):
        super().__init__(name,age)
        self.score = score

    def get_grade(self):
        return "优秀" if self score >= 90 else "及格"


class Pricipal1(Person):
    def __init__(self, name ,age, school):
        super().__init__(name,age)
        self.school = school 

    def announce(self):
        print(f"我是{self.school}学校的校长，我叫{self.name}")
