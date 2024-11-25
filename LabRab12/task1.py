import json

students = [
    {"Прізвище": "Завдов'єв", "Ім'я": "Денис", "Адреса": "пр. Лушпи, 18", "Школа": 17, "Клас": 9, "День": "субота"},
    {"Прізвище": "Петренко", "Ім'я": "Петро", "Адреса": "вул. Лесі Українки, 25", "Школа": 7, "Клас": 9, "День": "неділя"},
    {"Прізвище": "Сидоренко", "Ім'я": "Оксана", "Адреса": "пр. Лушпи, 18", "Школа": 17, "Клас": 7, "День": "субота"},
    {"Прізвище": "Ковальчук", "Ім'я": "Олег", "Адреса": "вул. Лесі Українки, 25", "Школа": 7, "Клас": 7, "День": "субота"},
    {"Прізвище": "Гончаренко", "Ім'я": "Анна", "Адреса": "пр. Лушпи, 18", "Школа": 17, "Клас": 8, "День": "неділя"},
    {"Прізвище": "Іваненко", "Ім'я": "Іван", "Адреса": "вул. Герасима Кондратьєва, 136", "Школа": 1, "Клас": 10, "День": "неділя"},
    {"Прізвище": "Петренко", "Ім'я": "Петро", "Адреса": "пр. Лушпи, 18", "Школа": 17, "Клас": 9, "День": "субота"},
    {"Прізвище": "Сидоренко", "Ім'я": "Оксана", "Адреса": "вул. Герасима Кондратьєва, 136", "Школа": 1, "Клас": 8, "День": "неділя"},
    {"Прізвище": "Ковальчук", "Ім'я": "Олег", "Адреса": "вул. Герасима Кондратьєва, 136", "Школа": 1, "Клас": 10, "День": "неділя"},
    {"Прізвище": "Гончаренко", "Ім'я": "Анна", "Адреса": "пр. Лушпи, 36", "Школа": 23, "Клас": 8, "День": "субота"}
]

# Збереження початкових даних у файл
def save_data_to_json(json_file_name, data):
    with open(json_file_name, "wt", encoding="utf-8") as file:
        json_string = json.dumps({"students": data}, ensure_ascii=False, indent=4)
        file.write(json_string)

# Завантаження даних із JSON-файлу
def load_data(json_file_name):
    with open(json_file_name, "rt", encoding="utf-8") as file:
        return json.load(file)["students"]

# Додавання нового запису
def add_record(json_file_name, data):
    new_student = {
        "Прізвище": input("Прізвище: "),
        "Ім'я": input("Ім'я: "),
        "Адреса": input("Адреса: "),
        "Школа": int(input("Номер школи: ")),
        "Клас": int(input("Клас: ")),
        "День": input("День відвідування (субота/неділя): ").lower()
    }
    data.append(new_student)
    save_data_to_json(json_file_name, data)
    print("Новий запис додано.")

# Видалення запису
def remove_record(json_file_name, data):
    display_data(data)
    idx = int(input("Введіть номер запису для видалення: ")) - 1
    if 0 <= idx < len(data):
        removed = data.pop(idx)
        save_data_to_json(json_file_name, data)
        print(f"Запис видалено: {removed}")
    else:
        print("Некоректний номер запису.")

# Виведення даних
def display_data(data):
    for idx, student in enumerate(data):
        print(f"{idx}. {student}")

# Пошук записів за полем
def search_record(data):
    field = input("Поле для пошуку (Прізвище, Ім'я, Адреса, Школа, Клас, День): ")
    value = input(f"Введіть значення для пошуку в полі {field}: ")
    results = [student for student in data if str(student.get(field, "")).lower() == value.lower()]
    display_data(results) if results else print("Записів не знайдено.")

# Розв'язання задачі
def solve_task(data, results_json):
    print( "Завдання: \nВизначити прізвище, ім'я та адресу учнів, "
           "що навчаються у молодших (7-8) класах та відвідують гурток по суботах.")
    results = [
        {"Прізвище": student["Прізвище"], "Ім'я": student["Ім'я"], "Адреса": student["Адреса"]}
        for student in data if student["Клас"] in [7, 8] and student["День"] == "субота"
    ]
    ## Запис результатів у JSON файл
    with open(results_json, "wt", encoding="utf-8") as file:
        json_string = json.dumps({"students": results}, ensure_ascii=False, indent=4)
        file.write(json_string)

    print(f"Результати збережено у файл {results_json}.")

    with open(results_json, "rt", encoding="utf-8") as file:
        saved_results = json.load(file)

    # Виведення результатів
    print("\nРезультат завдання (учні 7-8 класів, які відвідують гурток по суботах):")
    if "students" in saved_results:
        display_data(saved_results["students"])
    else:
        print("Результати не знайдено у файлі.")


# Ім'я файлу для збереження даних
students_json = "students.json"
results_json = "results.json"

# Збереження перших даних
save_data_to_json(students_json, students)
print("\nВсі початкові дані збережено у фал students_json.")

# Завантаження даних для перевірки
students_data = load_data(students_json)

while True:
    print("\nМеню:")
    print("1) Вивести дані")
    print("2) Додати запис")
    print("3) Видалити запис")
    print("4) Знайти запис")
    print("5) Виконати завдання Варіант 6")
    print("0) Вийти")
    choice = input("Виберіть опцію: ")
    if choice == "1":
        display_data(students_data)
    elif choice == "2":
        add_record(students_json, students_data)
    elif choice == "3":
        remove_record(students_json, students_data)
    elif choice == "4":
        search_record(students_data)
    elif choice == "5":
        solve_task(students_data, results_json)
    elif choice == "0":
        print("Програма завершена.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")
