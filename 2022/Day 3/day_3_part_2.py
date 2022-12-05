# Advent of Code 2022 Day 3 - Part 2

with open('input.txt') as sack_file:

  total_priority = 0

  priority_dic = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
    "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
  }

  sack_to_check = ''
  sack_count = 1
  repeated_items = []
  items = []

  for line in sack_file.readlines():    
    sack = str(line)

    if sack_count == 1:
      sack_to_check = sack

    elif sack_count == 2:
      for item in sack_to_check:
        if item in sack:
          repeated_items.append(item)

    elif sack_count == 3:
      for item in repeated_items:
        if item in sack:          
          if item.isupper():
            priority = priority_dic[item.lower()] + len(priority_dic)
            print(priority)
            total_priority += priority
          else:
            priority = priority_dic[item.lower()]
            print(priority)
            total_priority += priority

          break
    
    sack_count += 1

    if sack_count > 3:
      repeated_items = []
      sack_count = 1
    
print(f"Part 2 - Total priority: { total_priority }")