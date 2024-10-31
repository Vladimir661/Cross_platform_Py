from translator.google_module import translate, detect_lang, code_lang, lang_list

text = "Добрий вечір"
print(translate(text, "uk", "en"))
print(detect_lang(text))
print(code_lang("uk"))
lang_list("screen", text)
lang_list("file", text)