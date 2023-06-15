def fizzbuzz(n):
    numbers = []
    for number in range(1, n + 1):
        if number % 3 == 0:
            numbers.append('Fizz')
        else:
            numbers.append(number)
    return numbers
