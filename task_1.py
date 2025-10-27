print("Введите название футбольной команды: ")
nameTeam = input()
print(nameTeam + " - чемпион!")

lenStr = "Длинна строки = " + str(len(nameTeam))
print(lenStr)

teamLower = nameTeam.lower()
print(teamLower)
print(lenStr)

if "п" in teamLower: print(True) 
else: print(False)

print("Количество вхождений буквы: " + str(teamLower.count("а")))
