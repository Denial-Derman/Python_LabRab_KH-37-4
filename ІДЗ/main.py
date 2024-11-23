from tasks import numerical_integration, find_minimum, solve_linear_system, solve_differential_equation

print("\n>>* Програма для розв’язання задач чисельними методами з використанням SciPy *<<")
print("( В програмі наведені вже готові приклади )")

while True:
    print("\n<*> Меню <*>")
    print("1. Чисельне інтегрування <")
    print("2. Пошук мінімуму функції <")
    print("3. Розв'язання системи лінійних рівнянь <")
    print("4. Чисельне розв'язання диференціального рівняння <")
    print("0. Вийти з програми <")

    choice = input("Введіть номер методу: ").strip()

    # Вибір задачі
    if choice == "1":
        numerical_integration()
    elif choice == "2":
        find_minimum()
    elif choice == "3":
        solve_linear_system()
    elif choice == "4":
        solve_differential_equation()
    elif choice == "0":
        print("Програма завершена. Дякую за використання!")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")
