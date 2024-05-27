#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):
    result = []  # empty list to store modified words
    cap_next = True  # bool flag -> true

    # iterate through each char in string

    for char in s:

        if char == " ":  # for whitespaces, append as is
            result.append(char)
            cap_next = True

        elif char.isalpha() and cap_next:  # for alphabets, append the capitalized version, bool flag -> false
            result.append(char.upper())
            cap_next = False

        else:  # for other char, append as is, bool flag -> false
            result.append(char)
            cap_next = False

    return "".join(result)  # join the modified words in the list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
