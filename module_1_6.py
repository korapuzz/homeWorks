my_dict = {"Петров": [3, 4, 5, 4], "Леонов": [4, 5, 5, 5], "Серов": [3, 4, 4, 4],
           "Бабак": [5, 4, 4, 4], "Карпов": [3, 4, 2, 4],
           "Иванов": [3, 2, 3, 4], "Горохов": [4, 4, 5, 4]
           }
print("Работа со словарями.")
print("Оценки по предметам:")
print(my_dict)
print("Оценки Петрова:")
print(my_dict["Петров"])
print("Оценки Глухова:")
print(my_dict.get("Глухов"))
my_dict["Арбузов"] = [4, 5, 5, 4]
my_dict["Якушкин"] = [3, 4, 5, 2]
print("Добавили студентов:")
print(my_dict)

print("Удалили студента:")
rez = my_dict.pop("Леонов")
print(rez)
print("Итоговый словарь: ")
print(my_dict)


print("Работа с множествами.")
my_set = {1, 7, "word", 15, "title", (1, 2, 3), 3, "word"}
print("Исходное множество:")
print(my_set)
print("Добавляем элементы:")
my_set.update([8, "turtle", False])
print(my_set)
print("Удаляем элемент:")
my_set.discard(15)
print(my_set)