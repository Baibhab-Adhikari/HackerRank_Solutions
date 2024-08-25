# Enter your code here. Read input from STDIN. Print output to STDOUT


def captain_room(x: list[int]) -> int:
    x.sort()  # sorting the elements of the room list
    room_counts = {}  # empty dict for keeping track of room number counts
    # iterating through the rooms
    for room in x:
        # if room present in dict, increment counter
        if room in room_counts:
            room_counts[room] += 1
        # else add room to dict with counter = 1
        else:
            room_counts[room] = 1
    # return room with only one count
    for room, count in room_counts.items():
        if count == 1:
            return room


def main() -> None:
    k: int = int(input())
    rooms: list[int] = list(map(int, input().split()))
    result: int = captain_room(rooms)
    print(result)


if __name__ == "__main__":
    main()
