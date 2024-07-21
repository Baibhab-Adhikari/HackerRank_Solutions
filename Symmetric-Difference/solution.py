# Enter your code here. Read input from STDIN. Print output to STDOUT
# input the value for sets
size = int(input())
a = set(map(int, input().split()))
size = int(input())
b = set(map(int, input().split()))
# calculate symmetric difference between the sets
diff = a.symmetric_difference(b)
# iterate through the sorted set and print 
for num in sorted(diff):
    print(num)