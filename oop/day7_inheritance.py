class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")


class Principal1(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def announce(self):
        print(f"我是{self.school}学校的校长，我叫{self.name}")

    def introduce(self):
        print(f"您好，我是{self.school}的校长{self.name},很高兴认识您")


p = Principal1("李校长", 50, "北京实验小学")
p.announce()
p.introduce()
