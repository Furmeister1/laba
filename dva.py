import os

imyafayla = "слова.txt"
if not (os.path.isfile(imyafayla) and os.path.isfile(imyafayla)):
    print("Файл не существует")
    exit()
if os.path.splitext(imyafayla)[-1] != ".txt" or os.path.splitext(imyafayla)[-1] != ".txt":
    print("Файлы должены иметь формат .txt")
    exit()

with open(imyafayla, encoding='utf-8') as strochki:
    strochki = strochki.readlines()
strochki.sort(key=lambda x: x.count('а'), reverse=True)

for i in strochki:
    print(i.replace("\n", ""))
