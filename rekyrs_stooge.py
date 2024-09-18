import random


def stooge_rec(data, i=0, j=None):
    print(data)
    if j is None:
        j = len(data) - 1
    if data[j] < data[i]:
        data[i], data[j] = data[j], data[i]
    if j - i > 1:
        t = (j - i + 1) // 3
        stooge_rec(data, i, j - t)
        stooge_rec(data, i + t, j)
        stooge_rec(data, i, j - t)
    return data


def stooge(data):
    return stooge_rec(data, 0, len(data) - 1)


arr = []
for a in range(random.randint(3, 9)):
    arr.append((random.randint(0, 100)) + (random.randint(0, 100)) / 100)
print(arr)
print(stooge_rec(arr))