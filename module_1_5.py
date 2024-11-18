immutable_var = (1, 'two', True, (1, 2, 3), [1, 2, 3], {1, 2, 3})

print("Вывод кортежа")
print(immutable_var)
print("Вывод элементов кортежа")
print(*immutable_var)
print("Вывод элемента кортежа")
print(immutable_var[2])

# Так делать нельзя
# immutable_var[5] = 4

mutable_list = [1, 'two', True, (1, 2, 3), [1, 2, 3], {1, 2, 3}]

print("Вывод списка")
print(mutable_list)
print("Вывод элементов списка")
print(*mutable_list)
print("Вывод элемента списка")
print(mutable_list[2])

# Так делать можно
mutable_list[5] = 4
print("Вывод обновленного списка")
print(mutable_list)
