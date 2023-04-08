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
