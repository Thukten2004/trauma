def sum_of_digit(n):
    if n<10:
        return n
    else:
        last_digit = n%10
        remaining_digit = n//10

        return last_digit +     sum_of_digit(remaining_digit)
print(sum_of_digit(123))