def swap_case(s):
    swapped = []  # empty list to store all the changes

    for char in s:
        if char.isupper():  # check if the character is in uppercase
            swapped.append(char.lower())
        elif char.islower():  # check if the character is in lowercase
            swapped.append(char.upper())
        else:
            swapped.append(char)  # append the punctuations
    return ''.join(swapped)  # join the changed characters


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)