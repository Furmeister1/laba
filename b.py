def sum_gp(p, z, n):
    if n == 0:
        return 0
    else:
        return p + sum_gp(p * z, z, n - 1)


try:
    first = float(input("Введите первый член геометрической прогрессии: "))
    znamenatel = float(input("Введите знаменатель геометрической прогрессии: "))
    nomer = int(input("Введите номер геометрической прогрессии: "))
except ValueError:
    print("Введены некорректные данные")
    exit()

if nomer < 0:
    print("Введены некорректные данные")
    exit()

print(f"Сумма {nomer} членов геометрической прогрессии = {sum_gp(first, znamenatel, nomer)}")
