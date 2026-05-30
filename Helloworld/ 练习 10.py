def even_numbers(n):
    num = 0
    while num <= n:
        if num % 2 == 0:
            yield num
        num += 1


for num in even_numbers(10):
    print(num)
