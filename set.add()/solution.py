# Enter your code here. Read input from STDIN. Print output to STDOUT

def stamps(array):
    return len(set(array))  # return count of distinct stamps
    
    
n = int(input())
arr = []  # empty list to store stamps
for stamp in range(n):  # input stamps upto defined range
    x = input()
    arr.append(x)  # append to list
    
print(stamps(arr))  # print output