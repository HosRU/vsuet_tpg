glsWord = 0
SoglWord = 0

try:
    with open("data_task7.4.txt", encoding="utf-8") as fh:
        for line in fh:
            str = line.split()
            for elem in str:
                if elem.lower().startswith(("а", "о", "у", "э", "ы", "я", "ё", "е", "ю", "и")):
                    glsWord = glsWord + 1
                else:
                    SoglWord = SoglWord + 1
        if glsWord > SoglWord:
            print("Слов на гласную больше: ", glsWord)
        else:
            print("Слов на согласную больше: ", SoglWord)
except Exception as e:
    print("Ошибка: ", e)