# 1
numbers = [5, 2, 8, 1, 9]
max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("最大值是：", max_value)
print("最小值是：", min_value)
# 2
inventory = {"apple": 10, "banana": 5, "orange": 8}

for k, v in inventory.items():
    if v > 6:
        print(f"{k}")


keys = ["a", "b", "c"]
values = [1, 2, 3]
result = dict(zip(keys, values))
print(result)

keys = ["a", "b", "c"]
values = [1, 2, 3]
result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i]
print(result)
