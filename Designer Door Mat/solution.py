# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    def print_pattern(N, M):
        # top half
        for i in range((N - 1) // 2):
            pattern_count = 2 * i + 1
            hyphens = (M - (pattern_count * 3)) // 2
            row = '-' * hyphens + '.|.' * pattern_count + '-' * hyphens
            print(row)

        # center line
        welcome = "WELCOME"
        welcome_length = len(welcome)
        hyphens_each_side = (M - welcome_length) // 2
        center_line = '-' * hyphens_each_side + welcome + '-' * hyphens_each_side
        print(center_line)

        # bottom half
        for i in range((N - 1) // 2 - 1, -1, -1):
            pattern_count = 2 * i + 1
            hyphens = (M - (pattern_count * 3)) // 2
            row = '-' * hyphens + '.|.' * pattern_count + '-' * hyphens
            print(row)


    N, M = map(int, input().split())

    print_pattern(N, M)

