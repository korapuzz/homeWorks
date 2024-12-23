class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        #print(f"Строение {self.name} имеет {self.number_of_floors} этажей")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")

    def __bool__(self):
        res = True
        if self.number_of_floors < 9:
            res = False
        return res

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for k in range (new_floor):
                print(k + 1)

h1 = House('ЖК Эльбрус', 6)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

# __bool__  Экспериментирую
if h1:
    print("Высотка")
else:
    print("Не высотка")

if h2:
    print("Высотка")
else:
    print("Не высотка")
