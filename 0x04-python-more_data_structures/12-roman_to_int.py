#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    A function converts a Roman numeral to an integer.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    last_value = 0

    for i in range(len(roman_string) - 1, -1, -1):
        current_value = roman_map[roman_string[i]]

        if current_value >= last_value:
            result += current_value
        else:
            result -= current_value

        last_value = current_value

    return result
