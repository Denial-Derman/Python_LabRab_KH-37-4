# Лабораторна робота 4

# Основний текст
text="Мрії — це крила, що ведуть до нових вершин. Вони дарують натхнення і силу досягати більше!"
print("Текст:\n", text) # Вивід тексту
length=len(text) # Довжина тексту
print("Довжин текста: ", length)

# Вбудовані функції
# Завдов'єв Денис
def cetnerText():
    width = 100  # Ширина поля відносно якого відцентровується текст
    centring= text.center(width) # Повертає вирівнювання рядка по центру
    return centring

def lowerCase():
    lowerCase=text.lower() # Конвертування рядка у нижній регістр
    return lowerCase

def upperCase():
    upperCase=text.upper() # Конвертування рядка у верхній регістр
    return upperCase
# Наступний студент має використати swapcase(), rindex(), find()

# main
print("Центрування:\n", cetnerText())
print("Нижній регістр:\n", lowerCase())
print("Верхній регістр:\n", upperCase())
