def check_employee_hapiness():
    hapiness_list = list(map(int, input().split()))
    hapiness_factor = int(input())

    improved_hapiness = [hapiness * hapiness_factor for hapiness in hapiness_list]
    average_hapiness = sum(improved_hapiness) / len(improved_hapiness)
    happy_count = sum(hapiness >= average_hapiness for hapiness in improved_hapiness)
    total_count = len(improved_hapiness)

    message = "happy" if happy_count >= total_count / 2 else "not happy"
    result = f"Score: {happy_count}/{total_count}. Employees are {message}!"
    return result

print(check_employee_hapiness())