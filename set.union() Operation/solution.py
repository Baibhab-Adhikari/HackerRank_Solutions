n = int(input())  # no. of students for eng newspaper
eng_roll_set = input().split()  
b = int(input())  # no. of students for fr newspaper
fr_roll_set = input().split()

print(len(set(fr_roll_set).union(set(eng_roll_set))))  # print count of the union of the sets of english and french roll numbers