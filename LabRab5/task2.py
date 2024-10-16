# Лабораторна робота №5

n = 7

a = [[n - abs(i - j) for i in range(n)] for j in range(n)]

for r in a:
        print(*r)