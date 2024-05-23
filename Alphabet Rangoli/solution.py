
def print_rangoli(N):

    max_char = ord('a') + N - 1  # get character corresponding to the integer input
    lines = []  # empty list to store the lines

    for i in range(N):
        letters = [chr(max_char - j) for j in range(i + 1)]  # forming the letter pattern
        line = '-'.join(letters + letters[-2::-1])  # join letters with hyphens
        hyphens = '-' * (2 * (N - i - 1))  # calculate hyphen for padding based on the previous line
        lines.append(hyphens + line + hyphens)  # append to lines with correct pattern formatting

    for line in lines:  # top half with middle line
        print(line)

    for line in lines[-2::-1]:  # bottom half without middle line
        print(line)


# Main driver code

if __name__ == '__main__':

    # error handling
    N = 0
    while N > 26 or N < 1:
        N = int(input())
    print_rangoli(N)
