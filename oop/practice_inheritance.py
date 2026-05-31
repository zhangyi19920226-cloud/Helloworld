class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}发出来声音")


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}说:旺旺！")


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}说:喵喵！")


d = Dog("小黑")
c = Cat("咪咪")
d.speak()
c.speak()
