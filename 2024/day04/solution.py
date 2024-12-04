

def part1(t):
  count = 0
  width = len(t)
  height = len(t[0])
  word = "XMAS"

  for y in range(width):
    for x in range(height):
      ch = t[y][x]
      if ch != "X":
        continue

      if y >= 3 and "".join([t[y][x], t[y - 1][x], t[y - 2][x], t[y - 3][x]]) == word: # up
        count += 1
      if y + 3 < height and "".join([t[y][x], t[y + 1][x], t[y + 2][x], t[y + 3][x]]) == word: # down
        count += 1
      if x + 3 < width and "".join([t[y][x], t[y][x + 1], t[y][x + 2], t[y][x + 3]]) == word: #left
        count += 1
      if x > 2 and "".join([t[y][x], t[y][x - 1], t[y][x - 2], t[y][x - 3]]) == word: #right
        count += 1
      if x >= 3 and y >= 3 and "".join([t[y][x], t[y - 1][x - 1], t[y - 2][x - 2], t[y - 3][x - 3]]) == word: # left up
        count += 1
      if x + 3 < width and y >= 3 and "".join([t[y][x], t[y - 1][x + 1], t[y - 2][x + 2], t[y - 3][x + 3]]) == word: # right up
        count += 1
      if x + 3 < width and y + 3 < height and "".join([t[y][x], t[y + 1][x + 1], t[y + 2][x + 2], t[y + 3][x + 3]]) == word: # right down
        count += 1
      if x >= 3 and y + 3 < height and "".join([t[y][x], t[y + 1][x - 1], t[y + 2][x - 2], t[y + 3][x - 3]]) == word: # left down
        count += 1

  return count

def part2(t):
  count = 0
  width = len(t)
  height = len(t[0])
  words = (["MAS", "SAM"])

  for y in range(1, width - 1):
    for x in range(1, height - 1):
      ch = t[y][x]
      if ch != "A":
        continue

      w1 = "".join([t[y - 1][x - 1], t[y][x], t[y + 1][x + 1]])
      w2 = "".join([t[y + 1][x - 1], t[y][x], t[y - 1][x + 1]])
      if w1 in words and w2 in words:
        count += 1

  return count

with open("2024/day04/input.txt", 'r') as file:
  input = file.read()
  table = []
  row = []
  for ch in input.strip():
    if ch == "\n":
      table.append(row)
      row = []
    else:
      row.append(ch)
  table.append(row)
  print("part1", part1(table))
  print("part2", part2(table))