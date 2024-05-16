if __name__ == '__main__':
    s = input()

    # Check if s contains alphanumeric characters
    print(any(c.isalnum() for c in s))

    # Check if s contains alphabetical characters
    print(any(c.isalpha() for c in s))

    # Check if s contains digits
    print(any(c.isdigit() for c in s))

    # Check if s contains lowercase characters
    print(any(c.islower() for c in s))

    # Check if s contains uppercase characters
    print(any(c.isupper() for c in s))

