def mutate_string(string, position, character):
    lst = list(string)  # type cast str to list
    lst[position] = character  # change character at given index
    string = ''.join(lst)  # join all the elements in the list
    return string  # return altered string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
