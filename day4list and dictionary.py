# List
empty = []
numbers = [10, 20, 30, 40]
mixed = [1, "hello", 3.14, True]

fruits = ["apple", "banana", "orange"]
print(fruits[0])
print(fruits[-1])

fruits[1] = "grape"
print(fruits)

nums = [1, 2, 3]
nums.append(4)
nums.insert(1, 99)
nums.remove(99)
last = nums.pop()
print(nums[1:3])
print(len(nums))
print(2 in nums)

for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(f"index{i}: {fruit}")

# Dictionary
empty = {}
person = {"name": "Jonny", "age": 34, "city": "Chengdu"}

print(person["name"])
person["age"] = 26
person["email"] = "zhangyi19920226@gmail.com"
print(person.get("phone", "no prvide"))
del person["city"]
email = person.pop("email")

person = {"name": "Bob", "age": 30}
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for k, v in person.items():
    print(f"{k}:{v}")

for key in person:
    print(key, person[key])

for key.value in person.item():
    print(key, value)


students = [
    {"name": "zhangsan", "score": 85},
    {"name": "lisi", "score": 92},
    {"name": "wangwu", "score": 78}
]

print(students[1]["score"])

for stu in students:
    print(f"{stu['name']} 成绩 {stu['score']} ")
