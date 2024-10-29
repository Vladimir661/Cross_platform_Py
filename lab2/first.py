from googletrans import Translator, LANGUAGES

def TransLate(text, lang):
    translator = Translator()
    
    lang_code = None
    if lang in LANGUAGES.values():
        lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)]
    elif lang in LANGUAGES.keys():
        lang_code = lang
    else:
        return "Помилка: Невідома мова."
    
    try:
        translated = translator.translate(text, dest=lang_code)
        return translated.text
    except Exception as e:
        return f"Помилка при перекладі: {str(e)}"

text_to_translate = "Hello, how are you?"
language = "es"
result = TransLate(text_to_translate, language)
print(result)
