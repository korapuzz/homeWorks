from houseClass import House

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

h1 = h1 + 1
print(h1)
h1 += 5
print(h1)
h2 = 2 + h2
print(h2)
h2 += 3
print(h2)

print(h1 < h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 <= h2)
print(h1 == h2)
print(h1 != h2)
print(h1 == 5)
print(h2 == 25)

