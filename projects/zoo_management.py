class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name}发出了声音")

    def info(self):
        print(f"名字：{self.name}.年龄：{self.age}")


class Lion(Animal):
    def __init__(self, name, age, mane_color):
        super().__init__(name, age)
        self.mane_color = mane_color

    def speak(self):
        print(f"{self.name}说：吼！")

    def info(self):
        super().info()
        print(f"鬃毛颜色：{self.mane_color}")


class Penguin(Animal):
    def __init__(self, name, age, can_fly=False):
        super().__init__(name, age)
        self.can_fly = can_fly

    def speak(self):
        print(f"{self.name}说：嗷嗷！")

    def info(self):
        super().info()
        print(f"能飞翔：{'是' if self.can_fly else '否'}")


class Monkey(Animal):
    def __init__(self, name, age, is_trained=False):
        super().__init__(name, age)
        self.is_trained = is_trained

    def speak(self):
        print(f"{self.name}说：吱吱！")

    def info(self):
        super().info()
        print(f"是否经过训练：{'是' if self.is_trained else '否'}")


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []            # 用列表存所有动物

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} 已入园！")

    def show_all(self):
        print(f"\n===== {self.zoo_name} 动物名单 =====")
        for animal in self.animals:
            animal.info()            # 多态！每个动物调自己的 info()
            print("---")

    def all_speak(self):
        print(f"\n===== 动物大合唱 =====")
        for animal in self.animals:
            animal.speak()           # 多态！每个动物叫自己的声音

    def count(self):
        print(f"当前共有 {len(self.animals)} 只动物")

    def find_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                print(f"找到了！")
                animal.info()
                return
        print(f"没有找到名叫 {name} 的动物")


# 创建动物园
zoo = Zoo("阳光动物园")

# 创建动物
lion = Lion("辛巴", 4, "金黄色")
penguin = Penguin("波波", 2)
m1 = Monkey("悟空", 5, is_trained=True)
m2 = Monkey("花花", 3)

# 入园
zoo.add_animal(lion)
zoo.add_animal(penguin)
zoo.add_animal(m1)
zoo.add_animal(m2)

# 查看
zoo.count()
zoo.show_all()
zoo.all_speak()
zoo.find_animal("悟空")
zoo.find_animal("辛巴")
