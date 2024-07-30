# Lesson_PS03. Парсинг HTML с помощью BeautifulSoup.

Файл ДЗ hw_PS03.py

Этот код реализует игру, в которой пользователю нужно угадать русское слово по его определению. Вот подробное описание работы кода:
1. Импорт библиотек:
``` python
from bs4 import BeautifulSoup
import requests
from googletrans import Translator
```
Код использует библиотеку BeautifulSoup для парсинга HTML, requests для выполнения HTTP-запросов и googletrans для перевода слов.
2. Функция get_russian_word:
```python
def get_russian_word():
    """Получает случайное слово с сайта и переводит его на русский язык,
    также переводит определение слова."""
    url = "https://randomword.com/"
    try:
        translator = Translator()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        russian_word = translator.translate(english_word, dest="ru").text
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        russian_word_definition = translator.translate(word_definition, dest="ru").text

        return {
            "russian_words": russian_word,
            "russian_word_definition": russian_word_definition
        }

    except Exception as e:
        print(e)
```
- Определяет URL https://randomword.com/ для получения случайного слова.
- Создает объект переводчика Translator.
- Выполняет HTTP-запрос к указанному URL и получает HTML-страницу.
- Парсит HTML-страницу, извлекая случайное английское слово и его определение.
- Переводит английское слово и его определение на русский язык.
- Возвращает словарь с русским словом и его определением.
