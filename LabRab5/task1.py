# Лабораторна робота №5

def SumOfElements(arr):
    return sum(numb for numb in arr if numb > 0 and numb % 3 == 0)

def getArray():
    quantity = int(input("Введіть кількість елементів у масиві: "))

    while True:
        array = list(map(int, input(f"Введіть {quantity} цілих чисел через пробіл: ").split()))

        if len(array) != quantity:
            print(f"Помилка: ви повинні ввести рівно {quantity} чисел. Спробуйте ще раз.")
        else:
            break

    return array

array = getArray()

result = SumOfElements(array)

print("Сума додатних елементів, що діляться на 3, дорівнює:", result)
