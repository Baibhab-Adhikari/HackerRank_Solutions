if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sorted_scores = sorted(list(arr), reverse=True)  # sort the list in descending order

    runner_up_score = None  # placeholder

    for score in sorted_scores:
        if score != sorted_scores[0]:  # if score not equal to the highest score
            runner_up_score = score  # reassign the runner up score
            break

    print(runner_up_score)