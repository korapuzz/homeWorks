class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        #print(f"Строение {self.name} имеет {self.number_of_floors} этажей")

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


    def __len__(self):
        return int(self.number_of_floors)

    def __add__(self, other):
        return self.number_of_floors + other

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance (other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance (other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return not self.__gt__(other)


    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)
