def calc(antennas, width, height, nearest):
  antinodes = set()
  for coordinates in antennas.values():
    for x1, y1 in coordinates:
      for x2, y2 in coordinates:
        if x1 == x2 and y1 == y2:
          continue
        dx = x2 - x1
        dy = y2 - y1
        rx = x2
        ry = y2
        while True:
          rx += dx
          ry += dy
          if rx < 0 or rx >= width or ry < 0 or ry >= height:
            break
          else:
            antinodes.add((rx, ry))
          if nearest:
            break
    if not nearest:
      antinodes.update(coordinates)
  return len(antinodes)


with open("2024/day08/input.txt", 'r') as file:
  antennas = {}
  width = 0
  height = 0
  for y, line in enumerate(file):
    height = y + 1 if y + 1 > height else height
    line = line.strip()
    for x, ch in enumerate(line):
      if not width:
        width = len(line)
      if ch == ".":
        continue
      antennas.setdefault(ch, []).append((x, y))

  print("part1", calc(antennas, width, height, True))
  print("part2", calc(antennas, width, height, False))