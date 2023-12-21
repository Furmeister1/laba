from timeit import timeit

moe = """
from random import randint


def puzir(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


spisok = [randint(0, 1000) for x in range(100)]
puzir(spisok)
"""

nemoe = """
from random import randint

rand_arr = [randint(0, 1000) for x in range(100)]
rand_arr.sort()
"""

print("Время выполнения сортировки методом пузырька: ", timeit(moe, number=200) / 200)
print("Время ввыполнения стандартной сортировки: ", timeit(nemoe, number=200) / 200)
