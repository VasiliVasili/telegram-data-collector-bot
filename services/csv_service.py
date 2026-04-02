import csv
from datetime import datetime

FILE_NAME = "data.csv"

def save_to_csv(data: dict):
    file_exists = False

    try:
        with open(FILE_NAME, "r", encoding="utf-8"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Дата", "Имя", "Телефон", "Комментарий"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data.get("name"),
            data.get("phone"),
            data.get("comment")
        ])