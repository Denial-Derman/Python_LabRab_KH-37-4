from scipy.integrate import quad, solve_ivp
from scipy.optimize import minimize
from scipy.linalg import solve
import numpy as np
from format_utils import format_number


# Чисельне інтегрування
def numerical_integration():
    print("\n<*> Чисельне інтегрування <*>")
    print("Функція: f(x) = sin(x)")
    print("Інтервал: [0, π]")

    def f(x):
        return np.sin(x)

    try:
        result, error = quad(f, 0, np.pi)
        print(f"Результат інтегрування: {format_number(result)}")
        print(f"Оцінка похибки: {format_number(error)}")
    except Exception as e:
        print(f"Помилка під час обчислення інтегралу: {e}")


# Пошук мінімуму функції
def find_minimum():
    print("\n<*> Пошук мінімуму функції <*>")
    print("Функція: f(x, y) = x^2 + y^2")

    def func(x):
        return x[0] ** 2 + x[1] ** 2

    initial_guess = [1, 1]

    try:
        # BFGS квазі-Ньютонів метод оптимізації.
        result = minimize(func, initial_guess, method='BFGS')
        x_min = format_number(result.x[0])
        y_min = format_number(result.x[1])
        fun_min = format_number(result.fun)
        print(f"Мінімум функції знаходиться в точці: ({x_min}, {y_min})")
        print(f"Значення функції у мінімумі: {fun_min}")
    except Exception as e:
        print(f"Помилка під час пошуку мінімуму: {e}")


# Розв'язання системи лінійних рівнянь
def solve_linear_system():
    print("\n<*> Розв'язання системи лінійних рівнянь <*>")
    print("Система рівнянь: ")
    print("| 2x + y = 5")
    print("| x + 3y = 7")

    A = [[2, 1], [1, 3]]
    b = [5, 7]

    try:
        solution = solve(A, b)
        x_sol = format_number(solution[0])
        y_sol = format_number(solution[1])
        print(f"Розв'язок системи: x = {x_sol}, y = {y_sol}")
    except Exception as e:
        print(f"Помилка під час розв'язання системи рівнянь: {e}")


# Чисельне розв'язання диференціального рівняння
def solve_differential_equation():
    print("\n<*> Чисельне розв'язання диференціального рівняння <*>")
    print("Рівняння: y' = -2y")
    print("Початкова умова: y(0) = 1")
    print("Інтервал: [0, 5]")

    def dydx(t, y):
        return -2 * y

    y0 = [1]
    t_span = (0, 5)

    try:
        solution = solve_ivp(dydx, t_span, y0, t_eval=[0, 1, 2, 3, 4, 5])
        print("Розв'язок рівняння:")
        for t, y in zip(solution.t, solution.y[0]):
            t_formatted = format_number(t)
            y_formatted = format_number(y)
            print(f"t = {t_formatted}, y = {y_formatted}")
    except Exception as e:
        print(f"Помилка під час розв'язання диференціального рівняння: {e}")
