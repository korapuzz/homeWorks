def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[:1])
    if len(str_number) == 1:
        if first == 0:
            return 1
        else:
            return first
    
    return first * get_multiplied_digits(int(str_number[1:]))

num = int(input("Введите число: "))
if num == 0:
    print("Это нуль")
else:
    print(get_multiplied_digits(num))
