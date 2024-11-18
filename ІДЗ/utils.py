# Перевірка, чи введено число
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Введено некоректне значення, спробуйте ще раз.")