numbers = 1,5,7,8,4,34,6,7,4,5

try:
    with open("data_task7.1.txt", "w", encoding="utf-8") as fh:
        for elem in numbers:
            fh.write(str(elem) + "\n")
except Exception as e:
    print("Ошибка: ", e)