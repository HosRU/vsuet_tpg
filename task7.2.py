try:
    resultSum = []
    with open("data_task7.1.txt", encoding="utf-8") as fh:
        for line in fh:
            resultSum.append(int(line))
        print("Сумма: " + str(sum(resultSum)))
        print("Максимум: " + str(max(resultSum)))
except Exception as e:
    print("Ошибка: ", e)