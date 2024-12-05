def reorder(rules, update):
    reordered = []
    while len(update):
        for i in reversed(range(len(update))):
            current = update[i]
            if current in rules and rules[current] & set(update[0:i]):
                continue
            else:
                update.pop(i)
                reordered.insert(0, current)
                break
    return reordered

def calculate(rules, updates):
    result = 0
    reordered_result = 0
    for update in updates:
        correct = True
        prev = set([update[0]])
        for i in range(1, len(update)):
            current = update[i]
            if current in rules and prev & rules[current]:
                correct = False
                break
            prev.add(current)
        if correct:
            result += update[len(update) // 2]
        else:
            reordered = reorder(rules, update)
            reordered_result += reordered[len(reordered) // 2]
    return result, reordered_result


with open("2024/day05/input.txt", "r") as file:
    is_rules = True
    rules = {}
    updates = []

    for line in file:
        if line == "\n":
            is_rules = False
            continue
        if is_rules:
            X, Y = tuple(map(int, line.split("|")))
            rules.setdefault(X, set()).add(Y)
        else:
            updates.append(list(map(int, line.split(","))))

    part1, part2 = calculate(rules, updates)
    print("part1", part1)
    print("part2", part2)

