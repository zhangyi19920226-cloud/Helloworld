# 2.1 布尔值比较
print(5 > 3)
print(10 == 10)
print(4 != 5)
print(7 <= 6)

# 2.2 if 语句基本结构
score = 85
if score >= 90:
    print("excellent")
else:
    print("good")

# 2.3 elif 多分支
score = int(input("your score"))

if score >= 90:
    print("excellent")
elif score >= 70:
    print("good")
elif score >= 60:
    print("not bad")
else:
    print("keep fighting")

# 2.4 练习：猜数字游戏

secret = 7
guess = int(input("guess a number range from 1~ 10"))

if guess == secret:
    print("congrats you are right")
elif guess > secret:
    print("guess bigger")
else:
    print("guess smaller")

# 2.5 逻辑运算符 and/or

age = int(input("number range 1~100"))
has_ticket = True

if age >= 18 and has_ticket:
    print("you can get into cinima")
else:
    print("forbiden entry")
