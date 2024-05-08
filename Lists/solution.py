if __name__ == '__main__':
    N = int(input())
    commands = []  # initialized an empty list to store the commands
    arr = []  # initialized an empty list

    # iterate through the given range to read commands
    for _ in range(N):
        command = input().split()  # input the commands from the user
        commands.append(command)  # append the split commands to the list

    # iterate through the commands
    for command in commands:
        # extract the command type
        cmd_type = command[0]

        if cmd_type == 'append':
            element = int(command[1])  # extract the element and type cast to int
            arr.append(element)

        elif cmd_type == 'pop':
            try:
                arr.pop()
            except ValueError:
                pass  # handle case where element not found

        elif cmd_type == 'sort':
            arr.sort()

        elif cmd_type == 'reverse':
            arr.reverse()

        elif cmd_type == 'insert':
            element = int(command[2])
            position = int(command[1])  # extract the position and type cast to int
            arr.insert(position, element)

        elif cmd_type == 'remove':
            element = int(command[1])
            try:
                arr.remove(element)
            except ValueError:
                pass  # handle case where element not found

        elif cmd_type == 'print':
            print(arr)
