from langdetect import detect, detect_langs

def LangDetect(txt):
    try:
        language = detect(txt)
        confidence = detect_langs(txt)[0].prob
        return language, confidence
    except Exception as e:
        return str(e)

text = "Bonjour, comment ça va?"
language, confidence = LangDetect(text)
print(f"Визначена мова: {language}, впевненість: {confidence:.2f}")
