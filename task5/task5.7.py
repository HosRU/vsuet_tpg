numbers = 4,5,7,2,5,454,3,7,9,0
count = 0
result = 0
while True:
    count = count + 1
    result += numbers[count]
    if numbers[count] == 0:
        break

print("Сумма введенных чисел:", result)