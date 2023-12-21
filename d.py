def iz_10v2(c, otricat=False):
    if c != abs(c):
        otricat = True
        c = abs(c)
    if c == 0 and otricat:
        return '-'
    elif c == 0:
        return ''
    return iz_10v2(c // 2, otricat) + str(c % 2)

try:
    choperevodit = int(input("Введите целое число в десятичной системе счисления: "))
except ValueError:
    print("Введены некорректные данные")
    exit()
print(iz_10v2(choperevodit))
