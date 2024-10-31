from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


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

gender_count = df["Стать"].value_counts()
print("Кількість співробітників чоловічої і жіночої статі:")
print(gender_count)

gender_count.plot(
    kind="bar", title="Кількість співробітників чоловічої і жіночої статі")
plt.ylabel("Кількість")
plt.xticks(rotation=0)
plt.show()

df["Вік"] = df["Дата народження"].apply(calculate_age)
categories = {
    "younger_18": df[df["Вік"] < 18],
    "18-45": df[(df["Вік"] >= 18) & (df["Вік"] <= 45)],
    "45-70": df[(df["Вік"] > 45) & (df["Вік"] <= 70)],
    "older_70": df[df["Вік"] > 70]
}

category_counts = {category: len(data)
                   for category, data in categories.items()}


print("\nКількість співробітників кожної вікової категорії:")
for category, count in category_counts.items():
    print(f"{category}: {count} співробітників")

pd.Series(category_counts).plot(
    kind="bar", title="Кількість співробітників кожної вікової категорії")
plt.ylabel("Кількість")
plt.xticks(rotation=0)
plt.show()


print("\nКількість співробітників жіночої та чоловічої статі кожної вікової категорії:")
gender_by_category_combined = pd.DataFrame()

for category, data in categories.items():
    gender_by_category = data["Стать"].value_counts()
    gender_by_category_combined[category] = gender_by_category

    print(f"\nКатегорія {category}:")
    print(gender_by_category)

gender_by_category_combined.plot(
    kind="bar", title="Кількість співробітників жіночої та чоловічої статі кожної вікової категорії")
plt.ylabel("Кількість")
plt.xticks(rotation=0)
plt.show()