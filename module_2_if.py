try:
    first = int(input("Введите первое  число: "))
    second = int(input("Введите второе число: "))
    third = int(input("Введите третье число: "))
except ValueError:
    print("Пожалуйста, вводите только числа")
else:
    if first == second == third:
        print(3)
    elif first == second or first == third or second == third:
        print(2)
    else:
        print(0)
