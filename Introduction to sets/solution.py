def average(array: list):
    # your code goes here
    distinct_array = set(array)  # making input array distinct by typecasting to set
    average = float(sum(distinct_array)) / len(distinct_array) # average value calculation
    return round(average, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)