def calc(left, right, operator):
  result = None
  if operator == "+":
    result = left + right
  elif operator == "*":
    result = left * right
  elif operator == "|":
    result = int(f"{left}{right}")
  else:
    exit(f"Unknown operator {operator}")
  return result


def check_equation(result, operands, operators):
  if len(operands) < 2:
    exit("Too less operands")

  stack = [(0, operands)]
  while len(stack):
    intermediate, operands = stack.pop()
    if intermediate == 0:
      stack.append((operands[0], operands[1:]))
      continue
    if len(operands) == 1:
      if any(calc(intermediate, operands[0], o) == result for o in operators):
        return True
    else:
      for o in operators:
        stack.append((calc(intermediate, operands[0], o), operands[1:]))
  return False


def calculate_sum(equations, operators):
  sum  = 0
  for result, operands in equations:
    if check_equation(result, operands, operators):
      sum += result
  return sum

with open("2024/day07/input.txt", 'r') as file:
  equations = []
  for line in file:
    l, r = line.split(':')
    result = int(l)
    operands = list(map(int, r.split( )))
    equations.append((result, operands))

  print("part1", calculate_sum(equations, "+*"))
  print("part2", calculate_sum(equations, "+*|"))

