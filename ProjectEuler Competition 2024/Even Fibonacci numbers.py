def fibonacci(n=0):  # default n = 0
    response = [0, 2]  # initialized a list with the smallest two even fibonacci numbers

    while True:
        next_number = response[-1] * 4 + response[-2]  # every third term of the sequence is even

        if next_number > n:
            return sum(response)
        response.append(next_number)  # keeping track of all the even numbers in the sequence


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    print(fibonacci(n))  # display the result
