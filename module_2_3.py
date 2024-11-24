my_list = list(map(int,input("Введите числа через пробел: ").split()))
count = len(my_list)
k = -1
while k < count - 1 and my_list[k] >= 0:
    k += 1
    if my_list[k] < 0:
        break
    elif my_list[k] == 0:
        continue

    print(my_list[k])
