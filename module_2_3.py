my_list = list(map(int,input("Введите числа через пробел: ").split()))
my_list.append(-1)
k = 0
while True:
    if my_list[k] < 0:
        break
    elif my_list[k] == 0:
        k += 1
        continue
    else:
        print(my_list[k])
        k += 1
