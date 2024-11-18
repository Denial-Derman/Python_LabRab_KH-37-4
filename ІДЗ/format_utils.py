import numpy as np

# Функція для форматування чисел
def format_number(num):
    if abs(num) < 1e-4 or abs(num) > 1e4:
        # Якщо число надто велике або мале, використовуємо формат з множенням на 10
        exponent = int(np.floor(np.log10(abs(num))))
        mantissa = num / (10 ** exponent)
        return f"{mantissa:.4f} * 10^{exponent}"
    else:
        # В іншому випадку - стандартний десятковий формат з 4 знаками після коми
        return "{:.4f}".format(num)
