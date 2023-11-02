student_records = {
    "Ivan": {"Math": 5, "Science": 6, "English": 5},
    "Pesho": {"Math": 4, "Science": 4, "English": 3},
    "Gosho": {"Math": 6, "Science": 6, "English": 4}
}

print(student_records["Ivan"])
print(student_records["Ivan"]["Math"])
print()

for name, value in student_records.items():
    print(f"*** {name} ***")
    for subject, score in value.items():
        print(f"{subject} - {score}")
    print()


# Iterating nested dicts

shopping_list = {
    "foods": {"nuts": "almonds"},
    "drinks": {"soft": "lemonade", "wine": "merlot"}
}

for key , value in shopping_list.items():
    for nested_key, nested_value in value.items():
        print(f"{nested_value} bought")
        shopping_list[key][nested_key] = "bought"

print(shopping_list)