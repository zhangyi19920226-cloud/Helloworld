big_list = [i * 2 for i in range(1_000_000)]
# 生成器的表达式
big_list = [i * 2 for i in range(10)]
print(big_list)

big_gen = (i * 2 for i in range(10))
print(big_gen)

print(next(big_gen))
print(next(big_gen))
print(next(big_gen))

for val in big_gen:
    print(val)

# yield 生成器函数


def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1


gen = count_up(5)
print(next(gen))
print(next(gen))
print(next(gen))

for num in count_up(5):
    print(num)


def read_large_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


for line in read_large_file("students.json"):
    print(line)


def even_numbers(n):
    num = 0
    while num % 2 == 0:
        yield num
        num += 1


for num in even_numbers(10):
    print(num)
