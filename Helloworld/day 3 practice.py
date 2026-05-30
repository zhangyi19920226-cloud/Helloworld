import random
for i in range(10, 0, -1):
    print("从10计数到1:", i)

i = 1
count = 1
while i <= 10:
    count *= i
    i += 1
print("1*到10的结果:", count)


num = int(input("用户输入数字："))
for i in range(1, 101):
    if num != i:
        continue
    else:
        print(i)
        break
else:
    # 如果循环结束都没找到（即num不在1-100内）
    print("数字不在1-100范围内")


secret = random.randint(1, 100)
guess_count = 0
while True:
    guess = int(input("Guess a number from(1~100)"))
    guess_count += 1

    if guess == secret:
        print(f"congrats,the number is{secret}")
        print(f"you are totally guess{guess_count}times")
        break
    elif guess < secret:
        print("It's smaller,try again")
    else:
        print("It's bigger,try again")
