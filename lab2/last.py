from langdetect import detect, detect_langs
from googletrans import Translator, LANGUAGES

def LangDetect(txt):
    try:
        language = detect(txt)
        confidence = detect_langs(txt)[0].prob
        return language, confidence
    except Exception as e:
        return str(e)

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

def CodeLang(lang):
    LANGUAGES_DICT = {
        "en": "English",
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "ru": "Russian",
        "zh-cn": "Chinese (Simplified)",
        "zh-tw": "Chinese (Traditional)",
        "ja": "Japanese",
        "ko": "Korean",
    }
    
    if lang in LANGUAGES_DICT.keys():
        return LANGUAGES_DICT[lang]
    elif lang in LANGUAGES_DICT.values():
        return list(LANGUAGES_DICT.keys())[list(LANGUAGES_DICT.values()).index(lang)]
    else:
        return "Невідома мова."

txt = "Доброго дня. Як справи?"
lang = "en"

print(txt)
detected_lang, confidence = LangDetect(txt)
print(f"Detected(lang={detected_lang}, confidence={confidence:.2f})")
translated_text = TransLate(txt, lang)
print(translated_text)
print(CodeLang(lang))
