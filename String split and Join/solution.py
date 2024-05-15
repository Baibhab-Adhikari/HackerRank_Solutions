def split_and_join(line):
    a = line.split()  # split the strings at whitespaces
    return '-'.join(a)  # return string joined by "-"


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
