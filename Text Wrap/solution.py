import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)  # textwrap.fill() is required to solve this.


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
