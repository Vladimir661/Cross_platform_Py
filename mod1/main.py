import json
import os
from helper import translate, triangle_area

data_file = "MyData.json"

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def save_data(data):
    with open(data_file, 'w') as f:
        json.dump(data, f)
    print(translate("saved_to_file", data["language"]).format(file_name=data_file))

def main():
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as f:
                data = json.load(f)
            lang = data.get("language", "uk")
            print(translate("language", lang))
            a1, b1, c1 = data["triangle1"]
            a2, b2, c2 = data["triangle2"]
        except (json.JSONDecodeError, KeyError):
            print("Некоректні дані в файлі MyData.")
            data = None
    else:
        data = None

    if not data:
        print("Введіть мову інтерфейсу (uk або en): ")
        lang = input().strip().lower()
        if lang not in ["uk", "en"]:
            lang = "uk"

        print(translate("enter_triangle_sides", lang).format(a="a1", b="b1", c="c1"))
        a1, b1, c1 = map(float, input().split())
        print(translate("enter_triangle_sides", lang).format(a="a2", b="b2", c="c2"))
        a2, b2, c2 = map(float, input().split())
        data = {
            "triangle1": [a1, b1, c1],
            "triangle2": [a2, b2, c2],
            "language": lang
        }
        save_data(data)

    if not (is_valid_triangle(a1, b1, c1) and is_valid_triangle(a2, b2, c2)):
        print("Один або обидва трикутники не можуть існувати з заданими сторонами.")
        return

    area1 = triangle_area(a1, b1, c1)
    area2 = triangle_area(a2, b2, c2)

    print(f"{translate('area_of_triangle', lang).format(area=area1)}")
    print(f"{translate('area_of_triangle', lang).format(area=area2)}")
    if area1 > area2:
        print(translate("larger_area", lang))
    elif area1 < area2:
        print(translate("smaller_area", lang))
    else:
        print(translate("equal_area", lang))

if __name__ == "__main__":
    main()
