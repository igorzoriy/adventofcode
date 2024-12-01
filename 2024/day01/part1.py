left = []
right = []

with open("input.txt", 'r') as file:
  for line in file:
    l, r = map(int, line.strip().split())
    left.append(l)
    right.append(r)

left.sort()
right.sort()

distance = 0
for l, r in zip(left, right):
  distance = distance + abs(l - r)

print("distance", distance)

rhash = {}
for r in right:
  if r in rhash:
    rhash[r] += 1
  else:
    rhash[r] = 1

similarity = 0
for l in left:
  if l in rhash:
    similarity += l * rhash[l]

print("similarity", similarity)