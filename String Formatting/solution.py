
def print_formatted(number):

    width = len(bin(number)[2:])  # getting the width of the largest binary number

    for i in range(1, number+1):  # iterate upto the given number starting from 1

        dec = str(i)  # decimal
        octal = oct(i)[2:]  # octal (removed prefix via indexing)
        hexa = hex(i)[2:].upper()  # hexadecimal in uppercase (removed prefix via indexing)
        binary = bin(i)[2:]  # binary (removed prefix via indexing)

        # Printing output with adjustment based on the width

        print(f'{dec:>{width}}{octal:>{width}}{hexa:>{width}}{binary:>{width}}')


if __name__ == '__main__':

    n = int(input())
    print_formatted(n)
