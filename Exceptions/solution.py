# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

# using loop to take input as per the number of test cases and use the try except block iteratively
for i in range(t):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")
