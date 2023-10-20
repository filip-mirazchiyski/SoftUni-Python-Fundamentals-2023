people = int(input())
capacity = int(input())
full_courses = people // capacity
if people % capacity > 0:
    full_courses += 1
print(full_courses)
