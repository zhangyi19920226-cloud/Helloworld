import os
import csv
import time


def is_even(n):
    return n % 2 == 0


print(is_even(4))


def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b


print(max_of_two(5, 4))


def is_even(n):
    return n % 2 == 0


def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b


print(f"{is_even(10)},{max_of_two(7, 3)}")


def make_greeting(greeting="hello"):
    def make_newgreeting(name):
        print(f"{greeting},{name}")
    return make_newgreeting


make_greeting("hey")("草原")


def log_call(func):
    """接收一个函数，返回一个增强版函数，调用前后打印日志"""
    def wrapper(*args, **kwargs):
        print("正在调用...")
        result = func(*args, **kwargs)
        print("调用结束")
        return result
    return wrapper


def add(a, b):
    return a + b


logged_add = log_call(add)

print(logged_add(3, 5))

print("在那片辽阔的草原上...")
time.sleep(1)

for i in range(5, 0, -1):
    print(f"距离说出那句话还有 {i} 秒...")
    time.sleep(1)

print("\n✨ 风带来了你的名字 ✨")
time.sleep(0.5)
print("🌾 每一株青草都在低声诉说 🌾")
time.sleep(0.5)
print("\u8349\u539f\uff0c\u6211\u7231\u4f60")


string = ["apple", "banana", "pear"]
sorted_string = sorted(string, key=lambda x: len(x))
print(sorted_string)


def create_student(name, **kwargs):
    print(name)
    for key, Value in kwargs.items():
        print(f"{key}:{Value}")


create_student("张三", age=20, city="beijing", major="CS")


students = []
zhang = {"姓名": "张三", "语文": 85, "数学": 92, "英语": 88}
students.append(zhang)
li = {"姓名": "李四", "语文": 78, "数学": 88, "英语": 90}
students.append(li)


def show_all():
    for stu in students:
        print(stu["姓名"], stu["语文"], stu["数学"], stu["英语"])
