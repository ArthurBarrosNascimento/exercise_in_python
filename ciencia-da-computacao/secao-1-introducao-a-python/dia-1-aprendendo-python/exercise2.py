def calculate_average_of_a_list01(*numbers):
    avarege = (sum(numbers)) // len(numbers)
    return avarege

# print(calculate_average_of_a_list01(1, 2, 3, 4, 5))

def calculate_average_of_a_list02(numbers):
    total = 0
    for number in numbers:
        total += number
    return total // len(numbers)

# print(calculate_average_of_a_list02([1, 2, 3, 4, 5]))