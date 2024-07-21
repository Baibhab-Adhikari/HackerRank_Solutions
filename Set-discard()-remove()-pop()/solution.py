# change language to Python3 to get the correct result
n = int(input())
s = set(map(int, input().split()))
# input the number of commands
N = int(input())
# iterate through the set and input commands
for command in range(N):
    cmd = input().split()
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "discard":
        s.discard(int(cmd[1]))
    elif cmd[0] == "remove":
        s.remove(int(cmd[1]))
    else:
        pass
# print the sum of elements remaining in the set
print(sum(s))