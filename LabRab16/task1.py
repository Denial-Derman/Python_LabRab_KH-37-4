import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# Завантажуємо текст з Project Gutenberg
file_id = 'bryant-stories.txt'
text = nltk.corpus.gutenberg.raw(file_id)

# Токенізація тексту
tokens = [word for word in word_tokenize(text.lower()) if word.isalpha()]

# Підрахунок частоти слів
fdist = FreqDist(tokens)

# 10 найбільш вживаних слів до фільтрації
top_10_words = fdist.most_common(10)
print("10 найбільш вживаних слів до фільтрації:")
for word, count in top_10_words:
    print(f"{word}: {count}")

# Побудова стовпчастої діаграми до фільтрації
words, counts = zip(*top_10_words)
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='skyblue')
plt.title('10 найбільш вживаних слів до фільтрації')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Підрахунок частоти слів після фільтрації
fdist_filtered = FreqDist(filtered_tokens)

# 10 найбільш вживаних слів після фільтрації
top_10_filtered_words = fdist_filtered.most_common(10)
print("\n10 найбільш вживаних слів після фільтрації:")
for word, count in top_10_filtered_words:
    print(f"{word}: {count}")

# Побудова стовпчастої діаграми після фільтрації
words_filtered, counts_filtered = zip(*top_10_filtered_words)
plt.figure(figsize=(10, 6))
plt.bar(words_filtered, counts_filtered, color='lightcoral')
plt.title('10 найбільш вживаних слів після фільтрації')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()