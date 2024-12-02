def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

# Задание 1. Задача "Распаковка":
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# Задание 2. Распаковка параметров:
values_list = ["one", True, 3]
values_dict = {"a":5, "b":False, "c": "опоздал"}
print_params(*values_list)
print_params(**values_dict)

# Задание 3/. Распаковка + отдельные параметры:
values_list_2 = [25, "Температура"]
print_params(*values_list_2, 42)
print_params()
