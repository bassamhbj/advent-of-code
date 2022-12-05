# Advent of Code 2022 Day 3 - Part 1

with open('input.txt') as sack_file:

  total_priority = 0

  priority_dic = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14,
    "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
  }

  for line in sack_file.readlines():
    content_len = len(str(line))
    
    items_per_compartment = int((content_len - 1) / 2)

    compartment_1 = str(line)[0:items_per_compartment]
    compartment_2 = str(line)[items_per_compartment:(content_len - 1)]

    for item in compartment_1:
      if item in compartment_2:
        print(item)

        if item.isupper():
          priority = priority_dic[item.lower()] + len(priority_dic)
          print(priority)
          total_priority += priority
        else:
          priority = priority_dic[item.lower()]
          print(priority)
          total_priority += priority

        break

print(f"Part 2 - Total priority: { total_priority }")