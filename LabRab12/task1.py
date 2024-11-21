import json

students  = [
    {"Прізвище": "Іваненко", "Ім'я": "Іван", "Адреса": "вул. Центральна, 12",
     "Номер школи": 5, "День відвідування": "субота", "Клас": 7},
    {"Прізвище": "Петренко", "Ім'я": "Петро", "Адреса": "вул. Київська, 22",
     "Номер школи": 10, "День відвідування": "неділя", "Клас": 8},
    {"Прізвище": "Сидоренко", "Ім'я": "Олена", "Адреса": "вул. Грушевського, 10",
     "Номер школи": 3, "День відвідування": "субота", "Клас": 7},
    {"Прізвище": "Коваленко", "Ім'я": "Оксана", "Адреса": "вул. Лесі Українки, 5",
     "Номер школи": 8, "День відвідування": "неділя", "Клас": 9},
    {"Прізвище": "Шевченко", "Ім'я": "Тарас", "Адреса": "вул. Шевченка, 1",
     "Номер школи": 7, "День відвідування": "субота", "Клас": 8},
    {"Прізвище": "Мельник", "Ім'я": "Юрій", "Адреса": "вул. Зелені Пагорби, 20",
     "Номер школи": 2, "День відвідування": "неділя", "Клас": 11},
    {"Прізвище": "Гончаренко", "Ім'я": "Марія", "Адреса": "вул. Дружби, 7",
     "Номер школи": 6, "День відвідування": "субота", "Клас": 8},
    {"Прізвище": "Романенко", "Ім'я": "Віталій", "Адреса": "вул. Полтавська, 13",
     "Номер школи": 4, "День відвідування": "неділя", "Клас": 10},
    {"Прізвище": "Бондаренко", "Ім'я": "Катерина", "Адреса": "вул. Лісова, 19",
     "Номер школи": 9, "День відвідування": "субота", "Клас": 7},
    {"Прізвище": "Демченко", "Ім'я": "Олександр", "Адреса": "вул. Набережна, 8",
     "Номер школи": 1, "День відвідування": "неділя", "Клас": 11}
]

# Ім'я JSON файлу для результатів
RESULT_FILE_NAME = "result.json"


def load_data():
    return students.copy()


def save_data(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def display_data(data):
    if not data:
        print("Дані відсутні.")
    else:
        for idx, student in enumerate(data, start=1):
            print(f"{idx}. {student}")

def add_record(data):
    surname = input("Прізвище: ")
    name = input("Ім'я: ")
    address = input("Адреса: ")
    school_number = input("Номер школи: ")
    visit_day = input("День відвідування (субота/неділя): ")
    grade = int(input("Клас (7-11): "))

    data.append({
        "Прізвище": surname,
        "Ім'я": name,
        "Адреса": address,
        "Номер школи": school_number,
        "День відвідування": visit_day,
        "Клас": grade
    })
    print("Запис додано!")


def remove_record(data):
    display_data(data)
    idx = int(input("Введіть номер запису для видалення: ")) - 1
    if 0 <= idx < len(data):
        removed = data.pop(idx)
        print(f"Видалено запис: {removed}")
    else:
        print("Некоректний номер запису.")


def search_record(data):
    field = input("Введіть поле для пошуку (Прізвище, Ім'я, Адреса, Номер школи, День відвідування, Клас): ")
    value = input(f"Введіть значення для пошуку в полі {field}: ")

    results = [student for student in data if str(student.get(field, "")).lower() == value.lower()]
    if results:
        print("Знайдені записи:")
        display_data(results)
    else:
        print("Нічого не знайдено.")


def solve_task(data):
    print("Завдання: \nВизначити прізвище, ім'я та адресу учнів, що навчаються у молодших (7-8) класах та відвідують гурток по суботах.")
    results = [
        {
            "Прізвище": student["Прізвище"],
            "Ім'я": student["Ім'я"],
            "Адреса": student["Адреса"]
        }
        for student in data
        if student["Клас"] in [7, 8] and student["День відвідування"].lower() == "субота"
    ]
    save_data(RESULT_FILE_NAME, results)
    print(f"Результат збережено у файл {RESULT_FILE_NAME}.")
    print(f"Результат з файлу:")
    display_data(results)


data = load_data()

while True:
    print("\nМеню:")
    print("1. Вивести дані-")
    print("2. Додати запис")
    print("3. Видалити запис")
    print("4. Знайти запис")
    print("5. Розв'язати задачу за варіантом")
    print("0. Вийти")
    choice = input("Виберіть опцію: ")
    if choice == "1":
        display_data(data)
    elif choice == "2":
        add_record(data)
    elif choice == "3":
        remove_record(data)
    elif choice == "4":
        search_record(data)
    elif choice == "5":
        solve_task(data)
    elif choice == "0":
        print("Програма завершена.")
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.")