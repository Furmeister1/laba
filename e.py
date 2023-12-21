def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)


def nok(a, b):
    return (a * b) // nod(a, b)


try:
    cifra1 = int(input("Введите первое натуральное число: "))
    cifra2 = int(input("Введите второе натуральное число: "))
except ValueError:
    print("Введены некорректные данные")
    exit()
if cifra1 < 1 or cifra2 < 1:
    print("Введены некорректные данные")
    exit()
print(nok(cifra1, cifra2))
