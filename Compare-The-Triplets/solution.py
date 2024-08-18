#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a: list[int], b: list[int]) -> list[int]:
    # Write your code here
    SIZE: int = 3  # constant
    # variable initialisations
    final_score: list[int] = []
    alice: int = 0
    bob: int = 0
    # point counter main loop
    for i in range(SIZE):
        if a[i] > b[i]:
            alice += 1
        elif b[i] > a[i]:
            bob += 1
        else:
            pass

    # append the final scores
    final_score.append(alice)
    final_score.append(bob)
    return final_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
