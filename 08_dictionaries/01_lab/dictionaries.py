user_credential = {
    "user1": "Filip",
    "user2": "Adriana",
}
print(user_credential)


student = dict(name="Ivan", age=33, major="Computer Science")
print(student)

student = dict([("name", "Ivan"), ("age", 33), ("major", "Computer Science")])
print(student)

keys = ["name", "age", "major"]
values = ["Ivan", 33, "Computer Science"]
student = dict(zip(keys, values))
print(student)

my_dict = {"name": "Plamen Ivanov", "age": 44, "occupation": "Engineer"}
name = my_dict.get("name") # = my_dict["name]
age = my_dict.get("age") # = my_dict["age"]
phone = my_dict.get("phone")

print(name)
print(age)
print(phone)

my_dict["phone"] = +359887735218
print(my_dict)