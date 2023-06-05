def calculate_average_of_a_list01(*numbers):
    '''Essa função realiza a media em indeterminados parâmetros'''
    avarege = (sum(numbers)) // len(numbers)
    return avarege

# print(calculate_average_of_a_list01(1, 2, 3, 4, 5))

def calculate_average_of_a_list02(numbers):
    '''Essa função realiz a media em uma lista passada como parâmetro'''
    total = 0
    for number in numbers:
        total += number
    return total // len(numbers)

# print(calculate_average_of_a_list02([1, 2, 3, 4, 5]))