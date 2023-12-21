abc = list(input("Введите строку: "))
for i in range(len(abc)):
    abc.append(abc.pop(-(i+1)))
print("".join(abc))
