slovo = list(input("Введите слово: "))
if len(slovo) < 3:
    print("Должно быть минимум 3 символа")
    exit()
abc = slovo[0:len(slovo)//2]
if len(slovo) % 2 == 0:
    ostalos = slovo[len(slovo)//2:]
else:
    ostalos = slovo[len(slovo)//2+1:]
for i in ostalos:
    if abc.pop() != i:
        print("Слово не палиндром")
        exit()
print("Слово является палиндромом")
