#!/usr/bin/python3
"""Technical interview Preparation at ALX_SE"""



def get_value(ch):
    arr = [
            ['I', 1],
            ['V', 5],
            ['X', 10],
            ['L', 50],
            ['C', 100],
            ['D', 500],
            ['M', 1000]
        ]
    for x in arr:
        if ch == x[0]:
            return x[1]
    return 0


def roman_to_int(roman_string):
    """Converts a roman umeral to an integer

    Args:
        roman_string: The roman numeral to convert

    Return:
        return the integer equivalent of roman_string

    """
    res = 0
    former_value = 'A'

    if type(roman_string) != str or not roman_string:
        return res

    for i in range(len(roman_string)):
        val_1 = get_value(roman_string[i])
        val_2 = get_value(former_value)
        if val_2 < val_1:
            val_1 -= val_2
            res += (val_1 - val_2)
        else:
            res += val_1

        former_value = roman_string[i]

    return res
