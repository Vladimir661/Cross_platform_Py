import math

def translate(text, lang="uk"):
    translations = {
        "uk": {
            "enter_triangle_sides": "Введіть величини сторін трикутника ({a}, {b}, {c}): ",
            "saved_to_file": "Дані збережено в файл {file_name}",
            "area_of_triangle": "Площа трикутника: {area:.2f}",
            "larger_area": "Площа першого трикутника більше другого.",
            "smaller_area": "Площа другого трикутника більше першого.",
            "equal_area": "Площі трикутників рівні.",
            "language": "Мова: Українська"
        },
        "en": {
            "enter_triangle_sides": "Enter the sides of the triangle ({a}, {b}, {c}): ",
            "saved_to_file": "Data saved to file {file_name}",
            "area_of_triangle": "Area of triangle: {area:.2f}",
            "larger_area": "The area of the first triangle is larger than the second.",
            "smaller_area": "The area of the second triangle is larger than the first.",
            "equal_area": "The areas of the triangles are equal.",
            "language": "Language: English"
        }
    }
    return translations.get(lang, translations["uk"]).get(text, text)

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))
