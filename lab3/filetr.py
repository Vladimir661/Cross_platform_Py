import json
from translator.google_module import translate


def load_config():
    file = open("lab3/config.json", "r").read()
    return json.loads(file)


def read_file(file_name, max_chars, max_words, max_sentences):
    text = ""
    chars, words, sentences = 0, 0, 0

    with open(file_name, "r") as file:
        for line in file:
            chars += len(line)
            words += len(line.split(" "))
            sentences += line.count(".") + line.count("!") + line.count("?")
            text += line

            if chars > max_chars or words > max_words or sentences > max_sentences:
                break

    return text


config = load_config()
filename = config["filename"]
target_lang = config["language"]
output = config["output"]

file_content = read_file(
    filename, config["characters"], config["words"], config["sentences"])
translated = translate(file_content, "uk", target_lang)

if output == "screen":
    print(translated)
if output == "file":
    with open(output, "w") as out_file:
        out_file.write(translated)

    print("Ok")