try:
    resultSum = []
    with open("data_task7.3.txt", encoding="utf-8") as fh:
        for line in fh:
            if line.strip().isdigit():
                resultSum.append(int(str(line).strip()))
        print("Сумма: " + str(sum(resultSum)))
        print("Максимум: " + str(max(resultSum)))
except Exception as e:
    print("Ошибка: ", e)