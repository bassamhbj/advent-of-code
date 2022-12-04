# Advent of Code 2022 Day 1 Part 1

cal_per_elf = []

with open('input.txt') as calories_file:
  total_cal = 0

  for line in calories_file.readlines():
    if not line.strip():
      cal_per_elf.append(total_cal)
      total_cal = 0
      continue
    else:
      total_cal += int(line)

list.sort(cal_per_elf, reverse=True)

max_cal_top_1 = cal_per_elf[0]
max_cal_top_2 = cal_per_elf[1]
max_cal_top_3 = cal_per_elf[2]

print(f"Part 1 - Top 1 max calories: {max_cal_top_1}")
print(f"Part 2 - Total Top 3 calories: { max_cal_top_1 + max_cal_top_2 + max_cal_top_3 }")

