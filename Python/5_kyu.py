# (1) 5_kyu
# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that
# range must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"


def rgb(r, g, b):
    to_hex = lambda x: f"{hex((x // 255) * 255 | (x % 255)).split('0x')[1].rjust(2, '0')}" if x > 0 else "00"
    return (to_hex(r) + to_hex(g) + to_hex(b)).upper()

#
# from CW
# def rgb_2(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))


# ----------------------------------------------------------------------------------------------------------------------


# (2) 5_kyu
