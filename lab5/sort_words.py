import string

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            first_sentence = text.split('.')[0].strip()
            print("Перше речення:", first_sentence)
            return text
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return None

def sort_words(text):
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    
    uk_words = [word for word in words if any('\u0400' <= char <= '\u04FF' for char in word)]
    en_words = [word for word in words if all('\u0000' <= char <= '\u007F' for char in word)]
    
    uk_words_sorted = sorted(set(uk_words))
    en_words_sorted = sorted(set(en_words))
    
    return uk_words_sorted, en_words_sorted

def main():
    file_path = 'lab5/input.txt'
    text = read_first_sentence(file_path)
    if text:
        uk_words, en_words = sort_words(text)
        
        print("\nУкраїнські слова (відсортовані):")
        print(uk_words)
        
        print("\nАнглійські слова (відсортовані):")
        print(en_words)
        
        total_words = len(uk_words) + len(en_words)
        print("\nКількість слів:", total_words)

if __name__ == "__main__":
    main()
