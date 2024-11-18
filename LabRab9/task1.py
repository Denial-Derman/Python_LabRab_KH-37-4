def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("Файл", file_name, "не було відкрито!")
        return None
    else:
        print("Файл", file_name, "було відкрито!")
        return file


file1_name = "TF9_1.txt"
file2_name = "TF9_2.txt"

# а) Створення файлу TF9_1
file_1_w = Open(file1_name, "w")
if file_1_w != None:
    # Список рядків для запису
    lines = [
        "Перший рядок коротко",
        "На вулиці світить сонце і співають птахи",
        "Читання книг відкриває двері у нові світи",
        "Програмування — це мистецтво і наука водночас",
        "Ранковий чай приносить натхнення",
        "Дуже довгий рядок, який точно має бути обрізаний до 20 символів",
        "Короткий рядок",
        "Рядок, що розповідає про космічні пригоди",
        "Технології змінюють світ щодня",
        "Рядок з довжиною менше двадцяти символів"
    ]

    # Об'єднуємо рядки списку та записуємо у файл
    file_1_w.write("\n".join(lines))

    print("Інформацію успішно додано до TF9_1.txt!")
    file_1_w.close()
    print("Файл TF9_1.txt було закрито!")

# б) Обробка рядків і запис у TF9_2
file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")
# file_2_w = Open("C:/file2_name", "w")

if file_2_r != None and file_2_w != None:
    for line in file_2_r:
        line = line.strip()
        if len(line) < 20:
            file_2_w.write(f">{line.ljust(20)}<\n")
        else:
            file_2_w.write(f">{line[:20]}<\n")
    file_2_r.close()
    file_2_w.close()
    print("Файли було закрито!")

# в) Читання і друк TF9_2
print("Нова послідовність:")
file_3_r = Open(file2_name, "r")
if file_3_r != None:
    for line in file_3_r:
        print(line.strip())
    file_3_r.close()
    print("Файл TF9_2.txt закрито!")
