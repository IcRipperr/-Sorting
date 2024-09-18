lst =[]
import random
for a in range(10):
    lst.append(random.randint(0, 100))

def bublesort(lst):
    for passesLeft in range(len(lst)-1,0,-1):
        for index in range(passesLeft):
            if lst[index]>lst[index + 1]:
                lst[index], lst[ index + 1] = lst[ index + 1], lst[index]
                print(lst)
    return lst
print(bublesort(lst))
