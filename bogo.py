arr = []
import random

for a in range(random.randint(2, 10000)):
    arr.append(random.randint(0, 100))
print(arr)


def is_sorted(array):
    length = len(array)
    for i in range(0, length - 1):
        if (array[i] > array[i + 1]):
            return False
    return True


def random_permutation(array):
    length = len(array)
    for i in range(0, length):
        rnd = random.randint(0, length - 1)
        temp = array[i]
        array[i] = array[rnd]
        array[rnd] = temp
        print(array)


def bogo_sort(array):
    while (not (is_sorted(array))):
        random_permutation(array)

print(bogo_sort(arr))
