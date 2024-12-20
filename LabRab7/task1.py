# Дані про учнів
students = {
    "0170": {"Прізвище": "Завдов'єв", "Ім'я": "Денис", "Адреса": "пр. Михайла Лушпи, 18", "Номер школи": 17, "Клас": 9},
    "0070": {"Прізвище": "Петренко", "Ім'я": "Петро", "Адреса": "вул. Лесі Українки, 25", "Номер школи": 7, "Клас": 9},
    "0171": {"Прізвище": "Сидоренко", "Ім'я": "Оксана", "Адреса": "пр. Михайла Лушпи, 18", "Номер школи": 17, "Клас": 11},
    "0071": {"Прізвище": "Ковальчук", "Ім'я": "Олег", "Адреса": "вул. Лесі Українки, 25", "Номер школи": 7, "Клас": 10},
    "0172": {"Прізвище": "Гончаренко", "Ім'я": "Анна", "Адреса": "пр. Михайла Лушпи, 18", "Номер школи": 17, "Клас": 8},
    "0010": {"Прізвище": "Іваненко", "Ім'я": "Іван", "Адреса": "вул. Герасима Кондратьєва, 136", "Номер школи": 1, "Клас": 10},
    "0173": {"Прізвище": "Петренко", "Ім'я": "Петро", "Адреса": "пр. Михайла Лушпи, 18", "Номер школи": 17, "Клас": 9},
    "0011": {"Прізвище": "Сидоренко", "Ім'я": "Оксана", "Адреса": "вул. Герасима Кондратьєва, 136", "Номер школи": 1, "Клас": 11},
    "0012": {"Прізвище": "Ковальчук", "Ім'я": "Олег", "Адреса": "вул. Герасима Кондратьєва, 136", "Номер школи": 1, "Клас": 10},
    "0230": {"Прізвище": "Гончаренко", "Ім'я": "Анна", "Адреса": "пр. Михайла Лушпи, 36", "Номер школи": 23, "Клас": 8}
}

# Функція для виведення всіх записів
def display_students():
    for key, data in students.items():
        print(f"Ключ: {key} - {data}")

# Функція для додавання нового запису
def add_student(key, surname, name, address, school_number, grade):
    try:
        students[key] = {
            "Прізвище": surname,
            "Ім'я": name,
            "Адреса": address,
            "Номер школи": int(school_number),
            "Клас": int(grade)
        }
        print(f"Запис з ключем ({key}) додано.")
    except ValueError:
        print("Помилка: Номер школи та клас повинні бути числовими значеннями.")

# Функція для видалення запису
def delete_student(key):
    if key in students:
        del students[key]
        print("Запис видалено.")
    else:
        print("Запис з таким Ключем не знайдено.")

# Функція для виведення словника за відсортованими ключами
def display_sorted():
    for key in sorted(students.keys()):
        print(f"Ключ: {key} - {students[key]}")

# Функція для пошуку учнів з певної школи, які навчаються у 10-11 класах
def find_students(school_number):
    senior_students = []
    try:
        school_number = int(school_number)
        for key, data in students.items():
            if data["Номер школи"] == school_number and data["Клас"] in [10, 11]:
                senior_students.append((key, (data["Прізвище"], data["Ім'я"], data["Адреса"])))
        return senior_students
    except ValueError:
        print("Помилка: Номер школи повинен бути числом.")
        return []

# Реалізації програми
print("<*> Програма запущена <*>\n")
print("* Правило написання ключа *"
      "\nКлюч  пишеться за правилом: \nПерше число: 0; \n"
      "Друге число: номер школи, якщо номер однозначний, то пишеться з 0 (Наприклад:05)\n"
      "Третє число: порядковий номер згадування школи в словнику*")

while True:
    choice = input("\n> Введіть 1, для виведення даних словника\n"
                   "> Введіть 2, для додавання нового запису\n"
                   "> Введіть 3, для видалення запису із словника\n"
                   "> Введіть 4, для виведення вмісту словника за відсортованими ключами\n"
                   "> Введіть 5, для визначення даних учнів, що навчаються у визначеній школі в старших (10-11) класах\n"
                   "> Введіть 0, щоб закінчити\n"
                   "> Введення пункту: ")

    if choice == '1':
        print("* Виведення даних словника *")
        display_students()

    elif choice == '2':
        print("* Додавання нового запису *")
        key = input("Ключ: ")
        surname = input("Прізвище: ")
        name = input("Ім'я: ")
        address = input("Адреса: ")

        while True:
            try:
                school_number = int(input("Номер школи: "))
                break
            except ValueError:
                print("Помилка: Номер школи повинен бути числом. Спробуйте ще раз.")

        while True:
            try:
                grade = int(input("Клас: "))
                break
            except ValueError:
                print("Помилка: Клас повинен бути числом. Спробуйте ще раз.")
        add_student(key, surname, name, address, school_number, grade)

    elif choice == '3':
        print("* Видалення запису із словника *")
        key = input("Введіть ключ учня: ")
        delete_student(key)

    elif choice == '4':
        print("* Виведення вмісту словника за відсортованими ключами *")
        display_sorted()

    elif choice == '5':
        print("* Визначення даних учнів, що навчаються у визначеній школі в старших (10-11) класах *")
        while True:
            try:
                school_number = int(input("Номер школи: "))
                break
            except ValueError:
                print("Помилка: Номер школи повинен бути числом. Спробуйте ще раз.")
        senior_students = find_students(school_number)
        print(f"Учні старших класів зі школи №{school_number}:")
        for key, data in senior_students:
            print(f"Ключ: {key} - Прізвище: {data[0]}, Ім'я: {data[1]}, Адреса: {data[2]}")

    elif choice == '0':
        print("<*> Програма завершена <*>")
        break
    else:
        print("Незареєстрована дія. Спробуйте ще раз.")