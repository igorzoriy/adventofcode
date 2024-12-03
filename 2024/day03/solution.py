import re

def calculate(input, adv_mode = False):
  state = "I"
  left = ""
  right = ""
  result = 0
  enadled = True

  for ch in input:
    if state == "I":
      if ch == "m":
        state = "M"
      elif ch == "d" and adv_mode:
        state = "D"
      continue

    if state == "M":
      state = "U" if ch == "u" else "I"
      continue

    if state == "U":
      state = "L" if ch == "l" else "I"
      continue

    if state == "L":
      if ch == "(":
        state = "("
        left =  ""
        right = ""
      else:
        state = "I"
      continue

    if state == "(":
      if ch.isdigit():
        left += ch
      elif ch == ",":
        state = ","
      else:
        state = "I"
      continue

    if state == ",":
      if ch.isdigit():
        right += ch
      elif ch == ")":
        if enadled:
          result += int(left) * int(right)
        state = "I"
      else:
        state = "I"

    if state == "D":
      state = "O" if ch == "o" else "I"
      continue

    if state == "O":
      if ch == "(":
        state = "DO("
      elif ch == "n":
        state = "N"
      else:
        state = "I"
      continue

    if state == "DO(":
      if ch == ")":
        enadled = True
      state = "I"

    if state == "N":
      state = "'" if ch == "'" else "I"
      continue

    if state == "'":
      state = "T" if ch == "t" else "I"
      continue

    if state == "T":
      state = "DONT(" if ch == "(" else "I"
      continue

    if state == "DONT(":
      if ch == ")":
        enadled = False
      state = "I"

  return result

with open("2024/day03/input.txt", 'r') as file:
  input = file.read()
  print("part1", calculate(input))
  print("part2", calculate(input, True))