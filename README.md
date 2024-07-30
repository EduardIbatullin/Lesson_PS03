# Lesson_PS03. Парсинг HTML с помощью BeautifulSoup.

## Файл ДЗ hw_PS03.py

Этот код реализует игру, в которой пользователю нужно угадать русское слово по его определению. Вот подробное описание работы кода:

1. **Импорт библиотек**:
   ```python
   from bs4 import BeautifulSoup
   import requests
   from googletrans import Translator
   ```
   Код использует библиотеку `BeautifulSoup` для парсинга HTML, `requests` для выполнения HTTP-запросов и `googletrans` для перевода слов.

2. **Функция `get_russian_word`**:
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
   - Определяет URL `https://randomword.com/` для получения случайного слова.
   - Создает объект переводчика `Translator`.
   - Выполняет HTTP-запрос к указанному URL и получает HTML-страницу.
   - Парсит HTML-страницу, извлекая случайное английское слово и его определение.
   - Переводит английское слово и его определение на русский язык.
   - Возвращает словарь с русским словом и его определением.

3. **Функция `word_game`**:
   ```python
   def word_game():
       """Запускает игру, где игроку нужно угадать случайное русское слово по его определению."""
       print("Добро пожаловать в игру!")
       while True:
           word_dict = get_russian_word()
           word = word_dict.get("russian_words")
           word_definition = word_dict.get("russian_word_definition")

           print(f"Значение слова: {word_definition}")
           user_answer = input("Что это за слово? - ")
           if user_answer == word:
               print("Всё верно!")
           else:
               print(f"Неправильно. Правильное значение: {word}")

           print("Хотите сыграть еще раз? (да/нет)")
           answer = input()
           if answer != "да":
               print("Спасибо за игру!")
               break
   ```
   - Приветствует пользователя и запускает цикл игры.
   - В каждом цикле вызывает функцию `get_russian_word` для получения случайного русского слова и его определения.
   - Выводит определение слова и запрашивает у пользователя его ответ.
   - Сравнивает ответ пользователя с правильным словом и выводит соответствующее сообщение.
   - Спрашивает пользователя, хочет ли он сыграть еще раз. Если ответ отрицательный, завершает игру.

4. **Запуск игры**:
   ```python
   word_game()
   ```
   - Запускает игру при выполнении скрипта.

В итоге, код реализует текстовую игру, в которой пользователю предлагается угадать слово на русском языке по его определению.

## Файл hw_PS03_optim - оптимизированный файл с помощью ChatGPT

Для оптимизации кода можно внести несколько улучшений:

1. Использовать кэширование для переводов, чтобы не переводить одно и то же слово несколько раз.
2. Сократить количество обращений к API переводчика, обрабатывая сразу все тексты за один запрос.
3. Упростить структуру кода и улучшить обработку ошибок.

Вот оптимизированная версия кода:

```python
from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def fetch_random_word():
    """Получает случайное слово и его определение с сайта randomword.com"""
    url = "https://randomword.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    english_word = soup.find("div", id="random_word").text.strip()
    word_definition = soup.find("div", id="random_word_definition").text.strip()
    return english_word, word_definition

def translate_texts(texts, dest="ru"):
    """Переводит список текстов на указанный язык"""
    translator = Translator()
    translations = translator.translate(texts, dest=dest)
    return [translation.text for translation in translations]

def get_russian_word():
    """Получает случайное слово с сайта и переводит его на русский язык, также переводит определение слова."""
    try:
        english_word, word_definition = fetch_random_word()
        russian_word, russian_word_definition = translate_texts([english_word, word_definition])
        return {
            "russian_word": russian_word,
            "russian_word_definition": russian_word_definition
        }
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def word_game():
    """Запускает игру, где игроку нужно угадать случайное русское слово по его определению."""
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_russian_word()
        if word_dict is None:
            print("Не удалось получить слово. Попробуйте снова.")
            continue

        word = word_dict["russian_word"]
        word_definition = word_dict["russian_word_definition"]

        print(f"Значение слова: {word_definition}")
        user_answer = input("Что это за слово? - ")
        if user_answer == word:
            print("Всё верно!")
        else:
            print(f"Неправильно. Правильное значение: {word}")

        if input("Хотите сыграть еще раз? (да/нет) ").lower() != "да":
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    word_game()
```

### Изменения и улучшения:
1. **Функция `fetch_random_word`**:
   - Отдельная функция для получения случайного слова и его определения с сайта.

2. **Функция `translate_texts`**:
   - Переводит список текстов за один вызов, чтобы уменьшить количество обращений к API переводчика.

3. **Функция `get_russian_word`**:
   - Использует `fetch_random_word` и `translate_texts` для получения и перевода слова и его определения.
   - Возвращает `None` в случае ошибки, чтобы избежать остановки программы.

4. **Функция `word_game`**:
   - Добавлена проверка на `None`, чтобы обработать случаи, когда слово не удалось получить.
   - Упрощены диалоги и структура кода.

Эти улучшения делают код более читаемым, устойчивым к ошибкам и эффективным в плане работы с API переводчика.
