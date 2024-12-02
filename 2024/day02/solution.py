def is_safe(levels):
  if (len(levels) < 2):
    return True
  direction = 0
  for i in range(1, len(levels)):
    diff = levels[i - 1] - levels[i]
    if abs(diff) < 1 or abs(diff) > 3:
      return False
    if direction == 0:
      direction = -1 if diff > 0 else 1
    elif direction == 1 and diff > 0:
      return False
    elif direction == -1 and diff < 0:
      return False
  return True

def is_safe_with_removal(levels):
  for i in range(len(levels)):
    if is_safe(levels[:i] + levels[i + 1:]):
      return True
  return False


safe_levels = 0
safe_levels_with_removal = 0
with open("2024/day02/input.txt", 'r') as file:
  for reports in file:
    levels = [int(report) for report in reports.split()]
    if is_safe(levels):
      safe_levels += 1
    if is_safe_with_removal(levels):
      safe_levels_with_removal += 1

print("safe_levels", safe_levels)
print("safe_levels_with_removal", safe_levels_with_removal)