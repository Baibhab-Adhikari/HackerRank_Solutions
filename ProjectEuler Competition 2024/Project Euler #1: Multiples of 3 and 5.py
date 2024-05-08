def sum_of_multiples(multiple, limit):
    n = (limit - 1) // multiple
    return multiple * n * (n + 1) // 2  # calculate sum of multiples


# Number of test cases
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())  # Input for each test case

    # Calculate sum of multiples of 3 or 5 using inclusion-exclusion principle
    total_sum = (sum_of_multiples(3, n) + sum_of_multiples(5, n) - sum_of_multiples(15, n))

    # Print sum for each test case
    print(total_sum)