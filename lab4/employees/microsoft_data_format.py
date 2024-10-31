import pandas as pd
from datetime import datetime


def calculate_age(birthday):
    today = datetime.today()
    birthday = datetime.strptime(birthday, "%d-%m-%Y")
    had_birthday_this_year = (today.month, today.day) < (
        birthday.month, birthday.day)
    return today.year - birthday.year - had_birthday_this_year


try:
    df = pd.read_csv("employees.csv")
except FileNotFoundError:
    print("CSV not found")
    exit(1)

df["Вік"] = df["Дата народження"].apply(calculate_age)

categories = {
    "younger_18": df[df["Вік"] < 18],
    "18-45": df[(df["Вік"] >= 18) & (df["Вік"] <= 45)],
    "45-70": df[(df["Вік"] > 45) & (df["Вік"] <= 70)],
    "older_70": df[df["Вік"] > 70]
}

with pd.ExcelWriter("employees.xlsx") as writer:
    df.to_excel(writer, sheet_name="all", index=False)
    columns = ["id", "Прізвище", "Ім’я",
               "По батькові", "Дата народження", "Вік"]

    for category, data in categories.items():
        data = data.copy()
        data["id"] = range(1, len(data) + 1)
        data.to_excel(writer, sheet_name=category, index=False,
                      columns=columns)


print("Ok")