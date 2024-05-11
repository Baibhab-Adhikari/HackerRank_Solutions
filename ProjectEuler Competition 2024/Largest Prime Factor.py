#!/bin/python3
import math

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        factors = []  # placeholder list for prime factors

        for i in range(2, int(math.sqrt(n)) + 1):  # check divisibility from 2 upto the square root of the number.
            while n % i == 0:  # check if divisible
                factors.append(i)  # append prime factors into the factors list
                n //= i  # update n after each iteration

        if n > 1:
            factors.append(n)

        # Print the largest prime factor
        print(max(factors))
