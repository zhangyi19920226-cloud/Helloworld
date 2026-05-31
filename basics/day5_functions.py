# 函数是一段有名字的、可以重复使用的代码块。它用来完成一个特定的任务。
def 函数名():
    print("执行了函数")


def say_hello():
    print("Hello!")

    say_hello()


def greet(name):
    print(f"你好，{name}!")


greet("小明")


def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")


def multiply(x, y):
    return x * y


product = multiply(4, 5)
print(product)


def just_print(msg):
    print(msg)


result = just_print("hi")
print(result)

x = 10


def change():
    global x
    x = 20


change()
print(x)


def greet(name, greeting="Hello"):
    print(f"{greeting},{name}!")


greet("Alice")
greet("Bob", "Hi")


def func(a, b=10):
    pass


def add_item(item, lst=[]):
    lst.append(item)
    return lst


print(add_item(1))
print(add_item(2))


def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


def introduce(name, age, city):
    print(f"{name},{age}岁， 来自{city}")


introduce(city="Beijing", name="Tom", age=20)


def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_all(1, 2, 3))
print(sum_all(5, 10))


def show_info(**kwargs):
    for key, Value in kwargs.items():
        print(f"{key}:{Value}")


show_info(Name="Alice", age=25, city="Shanghai")


def example(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)
