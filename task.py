# или можно так
# print([i for i in (list(map(str, input('введите элементы массива через пробел: ').split()))) if len(i) <= 3])
list1 = list(map(str, input('введите элементы массива через пробел: ').split()))
list2 = []
for i in range(len(list1)):
    if len(list1[i]) <= 3:
        list2.append(list1[i])
print(list2)
