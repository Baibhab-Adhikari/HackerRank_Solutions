# Enter your code here. Read input from STDIN. Print output to STDOUT


def main() -> None:
    # english newspaper input
    n: int = int(input())  # noqa: F841
    engRollNum: set = set(map(int, input().split()))
    # french newspaper input
    m: int = int(input())  # noqa: F841
    frRollNum: set = set(map(int, input().split()))
    # function call
    result: int = setDifferenceLength(engRollNum, frRollNum)
    print(result)


def setDifferenceLength(eng: set, fr: set) -> int:
    # returns the length of the set generated by set.difference()
    return len(eng.symmetric_difference(fr))


if __name__ == "__main__":
    main()
