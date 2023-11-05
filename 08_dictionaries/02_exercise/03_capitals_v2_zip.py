countries = input().split(", ")
capitals = input().split(", ")
final_information = dict(zip(countries, capitals))
# print(final_information)
for country, capital in final_information.items():
    print(f"{country} -> {capital}")