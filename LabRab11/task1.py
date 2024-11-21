import csv

# Зчитування та виведення CSV файлу
def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')  # Роздільник кома
            data = list(reader)

            # Вивести перші кілька рядків, щоб перевірити дані
            print("Заголовки:", reader.fieldnames)

            # Вивести дані для всіх країн
            for row in data:
                print(row['Country Name'], ': ', row['2015 [YR2015]'], ', ', row['2019 [YR2019]'])
            return data
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return []

# Пошук даних за країнами
def search_data(data, years, countries):
    header = ['Country Name'] + years  # Формуємо заголовки для результатів
    results = [header]  # Додати заголовок до результатів
    for row in data:
        if row['Country Name'] in countries:
            filtered_row = [row['Country Name']] + [row[year] for year in years]
            results.append(filtered_row)
    return results

# Запис у новий CSV файл
def save_csv(file_path, data):
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')  # Використовуємо той самий роздільник
            writer.writerows(data)
        print(f"Дані збережено у файл {file_path}")
    except Exception as e:
        print(f"Помилка запису у файл: {e}")

# Основний код
input_file = "Laba11.csv"
data = read_csv(input_file)

if not data:
    exit()

# Роки для пошуку
years = ["2015 [YR2015]", "2019 [YR2019]"]

# Країни для пошуку
print("\nПошук даних для введених назв країн")
countries = input("Введіть назви країн через кому (наприклад, Ukraine, Germany): ").split(", ")

# Пошук даних
results = search_data(data, years, countries)

# Перевірка, чи є результати
if len(results) > 1:
    print("\nРезультати пошуку:")
    for row in results:
        print(row)

    # Запис результатів у новий файл
    output_file = "search_results.csv"
    save_csv(output_file, results)
else:
    print("Результати не знайдено для введених країн.")