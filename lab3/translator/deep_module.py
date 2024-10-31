import random
from deep_translator import GoogleTranslator
from langdetect import detect_langs, DetectorFactory
DetectorFactory.seed = 0


def translate(text, src, dest):
    translator = GoogleTranslator(source=src, target=dest)
    return translator.translate(text)


def detect_lang(text, flag="all"):
    language = detect_langs(text)[0]

    if flag == "lang":
        return f"Language: {language.lang}"
    if flag == "confidence":
        return f"Confidence: {language.prob}"
    return f"Language: {code_lang(language.lang)}, confidence: {language.prob}"


def code_lang(lang):
    languages = GoogleTranslator().get_supported_languages(as_dict=True)

    if lang in languages:
        return languages[lang]
    if lang in languages.values():
        for code, name in languages.items():
            if name == lang:
                return code
    return "Error: incorrect language or code"


def lang_list(out="screen", text=""):
    translator = GoogleTranslator()
    languages = dict(random.sample(
        list(translator.get_supported_languages(as_dict=True).items()), 5))
    res = [f"{'N':<5} {'Language':<15} {'ISO-639 code':<12} Text",
       "--------------------------------------------------"]
    for i, (code, language) in enumerate(languages.items(), start=1):
        translated = translate(text, "auto", code)
        res.append(f"{i:<5} {language:<15} {code:<12} {translated}")

    if out == "screen":
        print("\n".join(res))

    if out == "file":
        with open("lab3/languages_list_deep", "w") as f:
            f.write("\n".join(res))


lang_list(text="hello", out="screen")