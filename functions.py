import math
from variables_and_constants import constant1, constant2


def calculate_value(x, y):
    return 21.5 + x * math.sin(4 * math.pi * x) + y * math.cos(20 * math.pi * y)


def calculate_decimal_array_from_binary_data(vector):
    final_vector = []

    for value in vector:
        value1 = -3 + int(value[0:18], 2) * constant1
        value2 = 4.1 + int(value[18:33], 2) * constant2
        final_vector.append([value1, value2])

    return final_vector
