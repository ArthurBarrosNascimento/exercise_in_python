def count_par_numbers(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count


print(count_par_numbers([1, 2, 3, 4]))
