LANGUAGES = {
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

def CodeLang(lang):
    if lang in LANGUAGES.keys():
        return LANGUAGES[lang]
    elif lang in LANGUAGES.values():
        return list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)]
    else:
        return "Невідома мова."

print(CodeLang("English"))
print(CodeLang("es"))
