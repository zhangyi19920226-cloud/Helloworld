# 读取文件的例子找到4个部分
def read_file(filename):
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
    except FileNotFoundError:
        print(f"file {filename} not exsit")
    except PermissionError:
        print("read this file without permission")
    else:
        print("read success!")
        print(content)
    finally:
        print("operate ended")


read_file("students.json")
read_file("ghost.txt")

# 捕获多个异常
try:
    num = int(input("enter a number:"))
    result = 100 / num
except ValueError:
    print("entered not a number！")
except ZeroDivisionError:
    print("cannot divide zero！")
except Exception as e:
    print(f"unknown fault:{e}")
else:
    print(f"result is:{result}")

# 主动跑出异常raise


def set_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"age{age}illegal,should be range from 1~150")
    return age


try:
    set_age(200)
except ValueError as e:
    print(f"wrong: {e}")


class ScoreError(Exception):
    pass


class AgeError(Exception):
    pass


def creat_student(name, age, score):
    if age < 0 or age > 150:
        raise AgeError(f"age illeage: {age}")
    if score < 0 or score > 100:
        raise ScoreError(f"score illeage: {score}")


try:
    s = creat_student("小明", 18, 150)
except AgeError as e:
    print(f"年龄错误:{e}")
except ScoreError as e:
    print(f"分数错误：{e}")
else:
    print(f"创建成功：{s}")


class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError(f"amount {amount} illegal")
    if amount > balance:
        raise InsufficientFundsError
    else:
        balance -= amount
        return balance


for amount in [500, -100, 2000]:
    try:
        new_balance = withdraw(1000, amount)
    except ValueError as e:
        print(f"输入错误：{e}")
    except InsufficientFundsError as e:
        print(f"余额不足：{e}")
    else:
        print(f"取款成功，余额：{new_balance}")
    finally:
        print("---")
