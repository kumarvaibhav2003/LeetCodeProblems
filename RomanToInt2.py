    # Python program to convert Roman to Integers
"""
Split the Roman Numeral string into Roman Symbols (character).
Convert each symbol of Roman Numerals into the value it represents.
Take symbol one by one from starting from index 0
	If current value of symbol is greater than or equal to the value of next symbol, then add this value to the running total.
	else subtract the value of current symbol with value of next symbol and then add it to the running total.
"""


# Function to returns value of each Roman symbol
def mapping(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1


def romanToInt(str):
    res = 0
    i = 0

    while i < len(str):

        # Getting value of symbol s[i]
        s1 = mapping(str[i])

        if i + 1 < len(str):

            # Getting value of symbol s[i + 1]
            s2 = mapping(str[i + 1])

            # Comparing both values
            if s1 >= s2:

                # Value of current symbol is greater or equal to the next symbol
                res = res + s1
                i = i + 1
            else:

                # Value of current symbol is less than the next symbol
                res = res + s2 - s1
                i = i + 2  # because we consumed two symbols like IV or CM

        # This is for single symbol like I, V, X, C,M
        else:
            res = res + s1
            i = i + 1

    return res


# print(romanToInt("XCIV"))

print(romanToInt("VXIID"))
