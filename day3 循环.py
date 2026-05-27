# 1 for loop and while
for i in range(5):
    print("currently number: ", i)


for i in range(1, 6):
    print(f"{i}的平方是{i*i}")

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I love eat {fruit}")

count = 0
while count < 3:
    print("loop times: ", count)
    count = count + 1

for i in range(1, 10):
    if i == 5:
        break
    print(i)

total = 0
for i in range(1, 101):
    total = total + i
print("1加到100点结果是: ", total)
