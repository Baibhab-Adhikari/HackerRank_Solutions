if __name__ == '__main__':
    n = int(input())  # n represent the number of elements inside the tuple
    t = tuple(int(x) for x in input().split())  # type cast str input to int and store in tuple
    print(hash(t))  # display the output

# please set the interpreter to pypy for the correct hash(t) value
