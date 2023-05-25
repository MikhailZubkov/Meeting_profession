list1 = list(map(str, input('введите через пробел элементы массива ').split()))
for i in range(len(list1)-1):
    if len(list1[i]) > 3:
        list1.pop(i)
print(list1)

#print([i for i in (list(map(str, input().split()))) if len(i) <= 3])