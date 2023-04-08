# (1) 7_kyu

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.

def square_digits(num):
    return int(''.join(str(int(d) ** 2) for d in str(num)))


# print(square_digits(9119))

# ----------------------------------------------------------------------------------------------------------------------

# (2) 7_kyu
# Create a function that returns the sum of the two lowest positive num_1 given an array of minimum
# 4 positive integers. No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
num_1 = [10, 343445353, 3453445, 3453545353453]  # should return 3453455.


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


# print(sum_two_smallest_numbers(num_1))

# ----------------------------------------------------------------------------------------------------------------------

# (3) 7_kyu
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter
# is non-negative


# def find_next_square(sq):
#     sqrt = sq ** 0.5
#     if sqrt == round(sqrt):
#         return round((sqrt + 1) ** 2)
#     return -1


def find_next_square(sq):
    return (sq ** .5 + 1) ** 2 if (sq ** .5) % 1 == 0 else -1


# print(find_next_square(114))
# print(find_next_square(121))

# ----------------------------------------------------------------------------------------------------------------------

# (4) 7_kyu

# Complete the function that accepts a string parameter, and reverses each word in the string.
# All spaces in the string should be retained.
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text: str):
    return ' '.join(x[::-1] for x in text.split(" "))


# print(reverse_words("This is an example!"))

# ----------------------------------------------------------------------------------------------------------------------

# (5) 7_kyu

# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013).
# Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known
# for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out
# how contractions are expected to be in the example below.
# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes
# from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string: str):
    return ' '.join(x.capitalize() for x in string.split(" "))

# from C_W
# import string
# toJadenCase = string.capwords

# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# ----------------------------------------------------------------------------------------------------------------------

# (6) 7_kyu
