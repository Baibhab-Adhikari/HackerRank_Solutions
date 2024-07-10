# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
# space separated input of n and m
n, m = map(int, input().split())
# Store words of group A with their indices
A = defaultdict(list)
for i in range(1, n + 1):
    letter = input()
    A[letter].append(i)
# Process words of group B and check against A
for _ in range(m):
    letter = input()
    if letter in A:
        print(" ".join(map(str, A[letter])))
    else:
        print("-1")