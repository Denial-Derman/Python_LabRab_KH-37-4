import csv
import matplotlib.pyplot as plt

file_path = 'Laba_14.csv'

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
    return header, data

def get_country_data(data, country_name):
    for row in data:
        if row[0] == country_name:
            return row
    return None

def plot_line_chart(years, country1_data, country2_data, country1_name, country2_name):
    plt.figure(figsize=(10, 6))
    plt.plot(years, country1_data, label=country1_name, marker='o', color='blue')
    plt.plot(years, country2_data, label=country2_name, marker='s', color='green')
    plt.xlabel("Рік")
    plt.ylabel("Значення показника")
    plt.title("Динаміка показника для двох країн")
    plt.legend()
    plt.grid(alpha=0.6)
    plt.show()

def plot_bar_chart(years, country_data, country_name):
    plt.figure(figsize=(10, 6))
    plt.bar(years, country_data, color='orange', label=country_name)
    plt.xlabel("Рік")
    plt.ylabel("Значення показника")
    plt.title(f"Показник для {country_name}")
    plt.legend()
    plt.grid(axis='y', alpha=0.6)
    plt.show()

header, data = read_csv(file_path)

years = [int(col.split(' ')[0]) for col in header[4:] if col]

country1_name = "Ukraine"
country2_name = "Poland"

country1_row = get_country_data(data, country1_name)
country2_row = get_country_data(data, country2_name)

if country1_row and country2_row:
    country1_data = [float(value) if value != '..' else None for value in country1_row[4:]]
    country2_data = [float(value) if value != '..' else None for value in country2_row[4:]]

    valid_years = [year for year, val1, val2 in zip(years, country1_data, country2_data) if
                   val1 is not None and val2 is not None]
    country1_filtered = [val for val in country1_data if val is not None]
    country2_filtered = [val for val in country2_data if val is not None]

    plot_line_chart(valid_years, country1_filtered, country2_filtered, country1_name, country2_name)

    chosen_country_name = input("Введіть назву країни для побудови стовпчастої діаграми: ")

    chosen_country_row = get_country_data(data, chosen_country_name)

    if chosen_country_row:
        chosen_country_data = [float(value) if value != '..' else None for value in chosen_country_row[4:]]
        chosen_filtered_data = [val for val in chosen_country_data if val is not None]

        plot_bar_chart(valid_years, chosen_filtered_data, chosen_country_name)
    else:
        print(f"Країна '{chosen_country_name}' не знайдена у даних.")
else:
    print("Дані для однієї з країн не знайдено.")
