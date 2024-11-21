import pandas as pd
import matplotlib.pyplot as plt

file_path = "comptagevelo2011.csv"
df = pd.read_csv(file_path)

# Перетворення дати
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Фільтрація даних за 2011 рік
df_2011 = df[df['Year'] == 2011]

if df_2011.empty:
    print("Дані за 2011 рік відсутні.")
else:
    monthly_counts = df_2011.groupby('Month').sum(numeric_only=True).sum(axis=1)

    if monthly_counts.empty:
        print("Немає даних для підрахунку місячної активності.")
    else:
        # Визначення найбільш популярного місяця
        popular_month = monthly_counts.idxmax()
        popular_count = monthly_counts.max()

        print(f"\nНайбільш популярний місяць: {popular_month}")
        print(f"Кількість велосипедистів у цьому місяці: {popular_count}")

        # Побудова графіку
        plt.figure(figsize=(10, 6))
        monthly_counts.plot(kind='bar', color='#483D8B', edgecolor='black')
        plt.title('Кількість велосипедистів по місяцях у 2011 році')
        plt.xlabel('Місяць')
        plt.ylabel('Кількість велосипедистів')
        plt.xticks(range(12), ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
                               'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'], rotation=45)
        plt.tight_layout()
        plt.show()
