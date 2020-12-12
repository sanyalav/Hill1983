import json
import re

def read_data_from_file():
    with open("data.json", "r") as file:
        data = json.load(file)
        return data
data = read_data_from_file()
print("0)", data)

def sort_by_surname(person):
    pattern = r"\w+$"
    surname = re.findall(pattern, person["name"])
    return surname
new_data_1 = sorted(data, key=sort_by_surname)
print("1)", new_data_1)

def sort_by_death_date(person):
    pattern = r"[0-9]+"
    if "BC" in person["years"]:
        death_dates = -1 * int((re.findall(pattern, person["years"]))[1])
    else:
        death_dates = int((re.findall(pattern, person["years"]))[1])
    return death_dates
new_data_2 = sorted(data, key=sort_by_death_date)
print("2)", new_data_2)

def sort_by_text_words(person):
    text_words = len(person["text"].split())
    return text_words
new_data_3 = sorted(data, key=sort_by_text_words)
print("3)", new_data_3)