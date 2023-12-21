import os

imyafayla = "очередь.txt"
if not (os.path.isfile(imyafayla) and os.path.isfile(imyafayla)):
    print("Файл не существует")
    exit()
if os.path.splitext(imyafayla)[-1] != ".txt" or os.path.splitext(imyafayla)[-1] != ".txt":
    print("Файлы должены иметь формат .txt")
    exit()
ochered = list()
with open(imyafayla, 'r', encoding="utf-8") as fayl:
    for stroka in fayl:
        ochered.append(stroka.split(", "))
true_ochered = list()
konec = list()

while len(konec) < len(ochered):
    for i in range(len(ochered)):
        if not (i in konec) and ochered[i]:
            true_ochered.append(ochered[i].pop(0).replace("\n", ""))
            konec.append(i)
print(", ".join(true_ochered))

for i in range(len(true_ochered)):
    true_ochered.pop(0)

