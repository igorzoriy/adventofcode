def next_step(x, y, direction, field):
    if direction == "UP":
        if y == 0:
            return True, None
        if field[y - 1][x] == "#":
            direction = "RIGHT"
        else:
            y -= 1
    elif direction == "RIGHT":
        if x == len(field[y]) - 1:
            return True, None
        if field[y][x + 1] == "#":
            direction = "DOWN"
        else:
            x += 1
    elif direction == "DOWN":
        if y == len(field) - 1:
            return True, None
        if field[y + 1][x] == "#":
            direction = "LEFT"
        else:
            y += 1
    elif direction == "LEFT":
        if x == 0:
            return True, None
        if field[y][x - 1] == "#":
            direction = "UP"
        else:
            x -= 1
    return False, (x, y, direction)

def find_path(field, start):
    path = set()
    direction = "UP"
    y, x = start

    while True:
        path.add(f"{x},{y}")
        end, next = next_step(x, y, direction, field)
        if end:
            return path
        x, y, direction = next

def check_for_loop(field, start):
    path = set()
    direction = "UP"
    y, x = start

    while True:
        step = f"{x},{y},{direction}"
        if step in path:
            return True
        path.add(step)
        end, next = next_step(x, y, direction, field)
        if end:
            return False
        x, y, direction = next



def part1(field, start):
    return len(find_path(field, start))

def part2(field, start):
    counter = 0
    path = find_path(field, start)
    for step in path:
        x, y = tuple(map(int, step.split(",")))
        field[y][x] = "#"
        if check_for_loop(field, start):
            counter += 1
        field[y][x] = "."
    return counter



with open("2024/day06/input.txt", "r") as file:
    lines = file.readlines()

    len_checker = None
    field = []
    y = 0
    guard = None

    for y, line in enumerate(lines):
        line = line.strip()
        if not len_checker:
            len_checker = len(line)
        elif len_checker != len(line):
            raise RuntimeError("Corrupted input file")

        row = []
        for x, ch in enumerate(line):
            if ch != "^":
                row.append(ch)
            else:
                guard = (y, x)
                row.append(".")
        field.append(row)


    print("part1", part1(field, guard))
    print("part2", part2(field, guard))

