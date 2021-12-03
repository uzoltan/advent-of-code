import copy
import os
import sys
from pprint import pprint
from typing import List

with open(os.path.join(sys.path[0], 'input.txt')) as file:
    binary_strings = [string.strip() for string in file.readlines()]

##########################################

most_common_bits = ''
least_common_bits = ''
zeroes = 0
ones = 0
for i in range(len(binary_strings[0])):
    for num in binary_strings:
        if num[i] == '0':
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        most_common_bits = most_common_bits + '0'
        least_common_bits = least_common_bits + '1'
    else:
        most_common_bits = most_common_bits + '1'
        least_common_bits = least_common_bits + '0'
    zeroes = 0
    ones = 0

gamma_rate = int(most_common_bits, 2)
epsilon_rate = int(least_common_bits, 2)
print(gamma_rate * epsilon_rate)

#################################################


def common_bit_in_position(index: int, binary_strings: List[str], equal: int, most_common: bool) -> int:
    zeroes = 0
    ones = 0
    for num in binary_strings:
        if num[index] == '0':
            zeroes += 1
        else:
            ones += 1
    if ones > zeroes:
        if most_common:
            return 1
        else:
            return 0
    elif ones == zeroes:
        return equal
    else:
        if most_common:
            return 0
        else:
            return 1


oxygen_list = copy.deepcopy(binary_strings)
co2_list = copy.deepcopy(binary_strings)
for i in range(len(binary_strings[0])):
    if len(oxygen_list) > 1:
        oxygen_common_bit = common_bit_in_position(i, oxygen_list, 1, True)
        oxygen_list = [num for num in oxygen_list if int(num[i]) == oxygen_common_bit]

    if len(co2_list) > 1:
        co2_common_bit = common_bit_in_position(i, co2_list, 0, False)
        co2_list = [num for num in co2_list if int(num[i]) == co2_common_bit]

print(int(oxygen_list[0], 2) * int(co2_list[0], 2))



