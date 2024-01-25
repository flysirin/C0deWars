# (1) 6_kyu

# Write a function that takes an integer as input, and returns the number of bits that are equal to one
# in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


def count_bits(n: int):
    return bin(n).count('1')


# print(count_bits(1234))

# ----------------------------------------------------------------------------------------------------------------------

# (2) 6_kyu

# from preloaded import MORSE_CODE
# ('.-... ---...   -..-. --...'), '&: /7')
# str_morse = '.-... ---...   -..-. --...'

# def decode_morse(morse_code: str):
#     morse_words = morse_code.strip().split("   ")
#     return ' '.join(''.join(MORSE_CODE[y] for y in x.split(" ")) for x in morse_words)
#
# print(decode_morse(str_morse))

# ----------------------------------------------------------------------------------------------------------------------

# (3) 6_kyu

# Enough is enough!
# Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want
# to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motif usually
# repeats. He isn't fond of seeing the Eiffel tower 40 times.
# He tells them that he will only sit for the session if they show the same motif at most N times. Luckily, Alice
# and Bob are able to encode the motif as a number. Can you help them to remove numbers such that their list
# contains each number only up to N times, without changing the order?
#
# Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
# For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the
# next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to
# [1,2,3,1,2,3].
# With list [20,37,20,21] and number 1, the result would be [20,37,21].


# def delete_nth(order: list, max_e: int):
#     set_num = set(order)
#     order.reverse()
#     for num in set_num:
#         while order.count(num) > max_e:
#             order.remove(num)
#     order.reverse()
#     return order
#
# # from cw
# def delete_nth_cw(order,max_e):
#     ans = []
#     for o in order:
#         if ans.count(o) < max_e: ans.append(o)
#     return ans
#
# print(delete_nth([1,2,3,1,2,1,2,3], 2))


# ----------------------------------------------------------------------------------------------------------------------

# (4) 6_kyu

# 89 is the first integer with more than one digit that fulfills the property partially introduced in the title
# of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 89 = 8 ** 1 + 9 ** 2
# The next number in having this property is 135:

# 135 = 1 ** 1 + 3 ** 2 + 5 ** 3

# We need a function to collect these numbers, that may receive two integers  a, b that defines the range [a,b]
# (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

# Let's see some cases (input -> output):
# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

# If there are no numbers of this kind in the range [a,b] the function should output an empty list.
# 90, 100 --> []


# def sum_dig_pow(a: int, b: int):  # range(a, b + 1) will be studied by the function
#     ans_list = []
#     for i in range(a, b + 1):
#         test_num = 0
#         for index, num in enumerate(list(str(i)), 1):
#             test_num += int(num) ** index
#         if i == test_num:
#             ans_list.append(i)
#     return ans_list
#
#
# # form cw
# def dig_pow(n):
#     return sum(int(x) ** y for y, x in enumerate(str(n), 1))
#
#
# def sum_dig_pow_2(a, b):
#     return [x for x in range(a, b + 1) if x == dig_pow(x)]


# ----------------------------------------------------------------------------------------------------------------------

# (5) 6_kyu


