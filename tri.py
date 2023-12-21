import os

imyafayla = "челики.txt"
if not (os.path.isfile(imyafayla) and os.path.isfile(imyafayla)):
    print("Файл не существует")
    exit()
if os.path.splitext(imyafayla)[-1] != ".txt" or os.path.splitext(imyafayla)[-1] != ".txt":
    print("Файлы должены иметь формат .txt")
    exit()

with open(imyafayla, encoding='utf-8') as chelovechki:
    chelovechki = chelovechki.readlines()

names = [(i.split(' ')[0], i.split(" ")[1][:-1]) for i in chelovechki]

sort = sorted(names, key=lambda x:  (x[0], x[1]))
print(sort)
