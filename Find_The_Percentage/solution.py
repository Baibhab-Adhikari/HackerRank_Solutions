if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avg_list = student_marks[query_name]  # Fetch all the scores and store it in a list

    avg = 0  # initialise avg to 0
    total = 0  # initialize total to 0

    #  main logic for average calculation
    for i in avg_list:
        total += i
        avg = total / 3

    print(f'{avg:1.2f}')  # used f string literal with upto 2 decimal places precision