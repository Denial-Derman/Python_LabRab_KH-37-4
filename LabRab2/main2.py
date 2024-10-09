from def_sport import sport

print("Функція 2: ")
M = int(input("Введіть значення M: "))
K = int(input("Введіть значення K: "))

if M <= 0 or K <= 0:
  print("Функція 2 повторне введення: ")
  M = int(input("Введіть значення M: "))
  K = int(input("Введіть значення K: "))

days_needed = sport(M, K)
print(f"Спортсмен пробіжить більше 50 км через {days_needed} днів.")
