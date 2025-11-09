def ceasar(text, shift):
    try:
        lettersUpper = [chr(i) for i in range(ord('А'), ord('П') + 1)]
        lettersLower = [chr(i) for i in range(ord('а'), ord('я') + 1)]

        result = []
        
        for word in text:
            if word in lettersLower:
                index = lettersLower.index(word)
                newIndex = (index + shift) % len(lettersLower)
                result.append(lettersLower[newIndex])

            elif word in lettersUpper:
                index = lettersUpper.index(word)
                newIndex = (index + shift) % len(lettersUpper)
                result.append(lettersUpper[newIndex])

            else:
                result.append(word)
        return ''.join(result) 
    
    except ValueError as err:
        print("Ошибка: ", err)

text = "ПрограММиРОВание С++"
shift = 5

encoded = ceasar(text, shift)
decoded = ceasar(encoded, -shift)

print("Зашифрованная строка:", encoded)
print("Расшифрованная строка:", decoded)
