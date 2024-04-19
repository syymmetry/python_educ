from collections import Counter
import re

def count_words(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.split()
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0]
    least_common_word = word_counts.most_common()[-1]
    return most_common_word, least_common_word

if __name__ == "__main__":
    text = input("Введите текст: ")
    most_common, least_common = count_words(text)
    print(f"Чаще всего повторялось слово '{most_common[0]}' - {most_common[1]} раз(а)")
    print(f"Меньше всего повторялось слово '{least_common[0]}' - {least_common[1]} раз(а)")