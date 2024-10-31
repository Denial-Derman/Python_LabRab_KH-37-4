def average(A):
    print("Заданий список за замовченням:", A)

    # Фільтрація від'ємних елементів
    negative_elements = [x for x in A if x < 0]

    if negative_elements:
        average = sum(negative_elements) / len(negative_elements)
        print("Середнє арифметичне від'ємних елементів:", average)
    else:
        print("Від'ємні елементи у списку відсутні.")

# Задати список безпосередньо
numbers = [43, -15, 2, -8, 10, 4, -1, -5, 20, 13]
average(numbers)
