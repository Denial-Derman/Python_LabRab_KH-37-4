import tasks
import utils

print("Ласкаво просимо до програми для розв'язування задач з чисельними методами!")
while True:
    print("\nВиберіть задачу:")
    print("1. Чисельне інтегрування")
    print("2. Розв'язок нелінійного рівняння")
    print("3. Мінімізація функції")
    print("4. Розв'язок системи лінійних рівнянь")
    print("5. Інтерполяція Лагранжа")
    print("0. Вихід")

    choice = int(input("Введіть номер задачі: "))

    if choice == 1:
        tasks.integrate_function()
    elif choice == 2:
        tasks.solve_equation()
    elif choice == 3:
        tasks.minimize_function()
    elif choice == 4:
        tasks.solve_linear_system()
    elif choice == 5:
        tasks.lagrange_interpolation()
    elif choice == 0:
        print("До побачення!")
        break
    else:
        print("Некоректний вибір, спробуйте ще раз.")