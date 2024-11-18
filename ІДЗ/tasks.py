import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve, minimize
from scipy.linalg import solve
from scipy.interpolate import interp1d
from format_utils import format_number  # Імпортуємо функцію форматування


# Задача 1: Чисельне інтегрування
def integrate_function():
    # Введення функції користувачем
    func_input = input("Введіть функцію для інтегрування, використовуючи 'x' як змінну (наприклад, 'x**2 + 3*x + 1'): ")

    # Перетворюємо рядок на функцію через eval
    try:
        func = lambda x: eval(func_input)
    except:
        print("Некоректно введена функція.")
        return

    # Введення меж інтегрування
    a = float(input("Введіть нижню межу інтегрування: "))
    b = float(input("Введіть верхню межу інтегрування: "))

    # Інтегрування функції на відрізку [a, b]
    result, error = quad(func, a, b)

    # Форматування результату та похибки
    result_str = format_number(result)
    error_str = format_number(error)

    print(f"Інтеграл від {a} до {b} дорівнює {result_str}, похибка: {error_str}")


# Задача 2: Розв'язок нелінійного рівняння
def solve_equation():
    # Введення коефіцієнтів для рівняння
    a = float(input("Введіть коефіцієнт a для рівняння ax^3 + bx + c = 0: "))
    b = float(input("Введіть коефіцієнт b для рівняння ax^3 + bx + c = 0: "))
    c = float(input("Введіть коефіцієнт c для рівняння ax^3 + bx + c = 0: "))

    def equation(x):
        return a * x ** 3 + b * x + c  # Нелінійне рівняння

    # Введення початкового наближення
    x0 = float(input("Введіть початкове наближення для рівняння: "))

    # Розв'язок рівняння за допомогою fsolve
    solution = fsolve(equation, x0)

    # Форматування результату
    solution_str = format_number(solution[0])

    print(f"Розв'язок рівняння: x = {solution_str}")


# Задача 3: Мінімізація функції
def minimize_function():
    # Введення коефіцієнтів для функції
    a = float(input("Введіть коефіцієнт a для функції ax^2 + bx + c: "))
    b = float(input("Введіть коефіцієнт b для функції ax^2 + bx + c: "))
    c = float(input("Введіть коефіцієнт c для функції ax^2 + bx + c: "))

    def func(x):
        return a * x ** 2 + b * x + c  # Функція для мінімізації

    # Введення початкового значення для мінімізації
    x0 = float(input("Введіть початкове значення для мінімізації: "))

    # Мінімізація функції
    result = minimize(func, x0)

    # Форматування результату
    result_str = format_number(result.x[0])

    print(f"Мінімум функції досягається при x = {result_str}")


# Задача 4: Розв'язання системи лінійних рівнянь
def solve_linear_system():
    n = int(input("Введіть кількість рівнянь у системі: "))

    # Введення коефіцієнтів системи
    A = []
    for i in range(n):
        row = list(map(float, input(f"Введіть коефіцієнти {i + 1}-го рівняння через пробіл: ").split()))
        A.append(row)

    B = []
    for i in range(n):
        B.append(float(input(f"Введіть праву частину {i + 1}-го рівняння: ")))

    A = np.array(A)
    B = np.array(B)

    # Розв'язок системи лінійних рівнянь
    solution = solve(A, B)

    # Форматування результатів
    solution_str = [format_number(s) for s in solution]

    print("Розв'язок системи лінійних рівнянь:", solution_str)


# Задача 5: Інтерполяція Лагранжа
def lagrange_interpolation():
    n = int(input("Введіть кількість точок для інтерполяції: "))

    x_points = []
    y_points = []
    for i in range(n):
        x, y = map(float, input(f"Введіть координати {i + 1}-ї точки (x, y): ").split())
        x_points.append(x)
        y_points.append(y)

    # Створення інтерполяційної функції
    f = interp1d(x_points, y_points, kind='linear')

    # Введення точки для інтерполяції
    x_new = float(input("Введіть точку для інтерполяції: "))
    y_new = f(x_new)

    # Форматування результату
    y_new_str = format_number(y_new)

    print(f"Інтерпольоване значення в точці {x_new} = {y_new_str}")
