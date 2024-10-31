import random
from googletrans import Translator
from googletrans.constants import LANGUAGES

translator = Translator()


def translate(text, src, dest):
    return translator.translate(text, src=src, dest=dest).text


def detect_lang(text, flag="all"):
    detect = translator.detect(text)
    if flag == "lang":
        return "Language: " + detect.lang
    if flag == "confidence":
        return "Confidence: " + detect.confidence
    return "Language: " + detect.lang + ", confidence: " + str(detect.confidence)


def code_lang(lang):
    if lang in LANGUAGES:
        return LANGUAGES[lang]
    if lang in LANGUAGES.values():
        for code, name in LANGUAGES.items():
            if name == lang:
                return code
    return "Error: incorrect language or code"


def lang_list(out="screen", text=""):
    languages = dict(random.sample(list(LANGUAGES.items()), 5))
    res = [f"{'N':<5} {'Language':<15} {'ISO-639 code':<12} Text",
       "--------------------------------------------------"]
    for i, (code, language) in enumerate(languages.items(), start=1):
        translated = translate(text, "auto", code)
        res.append(f"{i:<5} {language:<15} {code:<12} {translated}")

    if out == "screen":
        print("\n".join(res))

    if out == "file":
        with open("lab3/languages_list_google", "w") as f:
            f.write("\n".join(res))


lang_list(text="hello", out="file")