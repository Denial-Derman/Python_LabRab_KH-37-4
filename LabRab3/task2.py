# Завдання 2
# Задано слово. Визначити суму ASCII кодів символів слова.

line = str(input("Введіть любе слово: "))

#генератор списку
sumLine=sum(ord(char) for char in line)

print(f"Сума ASCII кодів символів '{line}':", sumLine)
