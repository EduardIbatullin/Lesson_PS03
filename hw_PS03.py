from bs4 import BeautifulSoup
import requests
from googletrans import Translator


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


word_game()
