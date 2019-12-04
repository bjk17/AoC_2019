#!/usr/bin/env python


def split_number_to_digits(n):
    return (
        n // 100000 % 10,
        n // 10000 % 10,
        n // 1000 % 10,
        n // 100 % 10,
        n // 10 % 10,
        n % 10
    )


def adjacent_numbers(n):
    # Two adjacent digits are the same
    d = split_number_to_digits(n)
    return d[0]==d[1] or d[1]==d[2] or d[2]==d[3] or d[3]==d[4] or d[4]==d[5]


def increasing_digits(n):
    d = split_number_to_digits(n)
    return d[0] <= d[1] <= d[2] <= d[3] <= d[4] <= d[5]


problem_input = "178416-676461"
a, b = map(int, problem_input.split('-'))

print(sum(
    adjacent_numbers(n) and increasing_digits(n) for n in range(a, b + 1)
))
