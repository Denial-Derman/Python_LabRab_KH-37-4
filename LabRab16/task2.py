import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = """
AI enables machines to perform tasks like decision-making, problem-solving, and learning.
"""

# Зберігаємо початковий текст в файл
input_file = 'original_text.txt'
with open(input_file, 'w') as file:
    file.write(text)

print(f"Початковий текст збережено у файлі '{input_file}'\n")

# Токенізація по словам
tokens = word_tokenize(text)
print("Токенізація по словам:")
print(tokens, "\n")

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]  # Лемматизація
stemmed_words = [stemmer.stem(word) for word in tokens]  # Стеммінг

print("Лемматизація слів:")
print(lemmatized_words, "\n")

print("Стеммінг слів:")
print(stemmed_words, "\n")

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Видалення стоп-слів:")
print(filtered_tokens, "\n")

# Видалення пунктуації
punctuation = set(string.punctuation)
tokens_without_punctuation = [word for word in filtered_tokens if word not in punctuation]
print("Видалення пунктуації:")
print(tokens_without_punctuation, "\n")

# Запис результатів в новий файл
output_file = 'processed_text.txt'
with open(output_file, 'w') as file:
    file.write("Початковий текст:\n")
    file.write(text + "\n\n")

    file.write("Токенізація по словам:\n")
    file.write(" ".join(tokens) + "\n\n")

    file.write("Лемматизація слів:\n")
    file.write(" ".join(lemmatized_words) + "\n\n")

    file.write("Стеммінг слів:\n")
    file.write(" ".join(stemmed_words) + "\n\n")

    file.write("Видалення стоп-слів:\n")
    file.write(" ".join(filtered_tokens) + "\n\n")

    file.write("Видалення пунктуації:\n")
    file.write(" ".join(tokens_without_punctuation) + "\n")

print(f"Оброблений текст збережено у файлі '{output_file}'")
