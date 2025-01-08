from math import pi
class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, *sides):
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = [0, 0, 0]

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides (self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides) # должен возвращать периметр фигуры.

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__calculate_radius()

    def __calculate_radius(self):
        return self.get_sides()[0] / (2 * pi)

    def get_square(self):
        radius = self.__calculate_radius()
        return pi * (radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calculate_height()

    def __calculate_height(self):
        sides = self.get_sides()
        s = sum(sides) / 2
        area = (s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** 0.5
        base = sides[0]
        return 2 * area / base

    def get_square(self):
        sides = self.get_sides()
        s = sum(sides) / 2
        return (s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        sides = [sides[0]] * self.sides_count if len(sides) == 1 else [1] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        # Volume of the cube = side^3, we assume all sides are equal
        side = self.get_sides()[0]
        return side ** 3


#Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
