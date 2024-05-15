def count_substring(string, sub_string):
    count = 0  # initialize count to keep track of occurrences
    start = 0  # Initialize a start index for searching
    while True:  # start an infinite loop
        index = string.find(sub_string, start)  # find the next occurrence of substring
        if index == -1:  # if no occurrences found then break
            break
        count += 1  # update counter
        start = index + 1  # update the searching index
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
