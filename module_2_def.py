# Как в рекомендациях к заданию
'''def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
'''

# Так корече будет
def get_matrix(n, m, value):
    matrix = [[value for j in range(m)] for i in range(n)]
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Привык матрицу выводить как матрицу
print(*result1, sep="\n")
print()
print(*result2, sep="\n")
print()
print(*result3, sep="\n")
