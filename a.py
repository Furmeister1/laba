def gp(p, z, n):
    if n == 1:
        return p
    else:
        return gp(p*z, z, n - 1)


try:
    first = float(input("Введите первый член геометрической прогрессии: "))
    znamenatel = float(input("Введите знаменатель геометрической прогрессии: "))
    nomer = int(input("Введите номер геометрической прогрессии: "))
except ValueError:
    print("Введены некорректные данные")
    exit()

if nomer < 1:
    print("Введены некорректные данные")
    exit()

print(f"{nomer}-й член геометрической прогрессии = {gp(first, znamenatel, nomer)}")
