a = 8
b = 16

numbers = [x for x in range(min(a, b), max(a, b)+1)]
for num in numbers:
    print(num, end=' ')

numbers.sort(reverse=True)
for num in numbers:
    print(num)