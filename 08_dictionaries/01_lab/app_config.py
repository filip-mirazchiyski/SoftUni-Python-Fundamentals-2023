app_configuration = {
    "database_host": "local_host",
    "database_port": 3306,
    "database_user": "myuser",
    "database_password": "pass_example",
    "database_name": "sqlDB"
}

for key in app_configuration.keys():
    print(key)
print()
for value in app_configuration.values():
    print(value)
print()
for k, v in app_configuration.items():
    print("Key:", k)
    print("Value:", v)
print()
if "database_host" in app_configuration.keys():
    print("Database host is a key in the dictionary")