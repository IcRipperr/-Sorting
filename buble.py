import random

arr =[]
vibor = input("Случайные числа?")
if vibor.capitalize() == "Да":
    for a in range(9):
        arr.append((random.randint(0, 100)) + (random.randint(0, 100)) / 100)
else:
    for a in range(9):
        arr.append (int(input("Введите число: ")))
def bublesort(lst):
    for passesLeft in range(len(lst)-1,0,-1):
        for index in range(passesLeft):
            if lst[index]>lst[index + 1]:
                lst[index], lst[ index + 1] = lst[ index + 1], lst[index]
                print(lst)
    return lst
print(bublesort(arr))
