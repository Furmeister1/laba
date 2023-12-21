def ap(p, pr, n):
    if n == 1:
        return p
    else:
        return ap(p+pr, pr, n - 1)


try:
    first = float(input("Введите первый член арифметической прогрессии: "))
    pribavlitel = float(input("Введите разность арифметической прогрессии: "))
    nomer = int(input("Введите номер арифметической прогрессии: "))
except ValueError:
    print("Введены некорректные данные")
    exit()

if nomer < 1:
    print("Введены некорректные данные")
    exit()

print(f"{nomer}-й член геометрической прогрессии = {ap(first, pribavlitel, nomer)}")
