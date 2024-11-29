n = int(input())
k = (n + 1) // 2
answ = ""
for i in range(1, k):
    for j in range(2, n):
        if n % (i + j) == 0 and j > i:
            answ += str(i)+str(j)
print(answ)
