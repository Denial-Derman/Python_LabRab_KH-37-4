import math

def equation(a, b):
    z = math.sin(a + b) * math.sin(a - b)
    return z

def sport(M, K):
    target_distance = 50
    current_distance = M
    days = 1

    while current_distance <= target_distance:
        current_distance += current_distance * (K / 100)
        days += 1

    return days

print("Функція 1: ")
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
result = equation(a, b)
print(f"Значення виразу z = {result} ")

print("Функція 2: ")
M = int(input("Введіть значення M: "))
K = int(input("Введіть значення K: "))

if M <= 0 or K <= 0:
    print("Функція 2 повторне введення: ")
    M = int(input("Введіть значення M: "))
    K = int(input("Введіть значення K: "))

days_needed = sport(M, K)
print(f"Спортсмен пробіжить більше 50 км через {days_needed} днів.")