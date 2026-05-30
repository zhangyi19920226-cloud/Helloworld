# 1
nubmers = int(input("give me a number"))
if nubmers > 0:
    print("positive")
elif nubmers == 0:
    print("0")
else:
    print("negative")


# 2
year = int(input("plese enter the year"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("闰年")
else:
    print("平年")

# 3

score = float(input("用户输入分数0~100"))
if score >= 90:
    print("A")
elif 70 <= score <= 89:
    print("B")
elif 60 <= score <= 69:
    print("C")
else:
    print("D")
