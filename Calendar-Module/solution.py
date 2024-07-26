# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
# input the date
date = tuple(map(int, input().split()))
# tuple unpacking
m, d, y = date
# print day in uppercase
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
