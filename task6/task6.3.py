# Дан список ФИО. Найти наиболее часто встречаемое отчество.
# Если отчества нет, человек не учитывается в подсчете.
try:
    n = int(input("Введите кол-во человек: "))
    middle_names = {}

    for i in range(n):
        fio = input("Введите ФИО через пробел: ").split()
        middle_name = fio[2]
        middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
except IndexError as err:
    print("Ошибка: " + str(err))

print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
print("В расчете участвовало человек:", n)