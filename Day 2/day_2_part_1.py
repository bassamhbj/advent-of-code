# Advent of Code 2022 Day 2 - Part 1

rock_points = 1
paper_points = 2
scissor_points = 3

lost_points = 0
draw_points = 3
win_points = 6

enemy_rock = 'A'
enemy_paper = 'B'
enemy_scissor = 'C'

my_rock = 'X'
my_paper = 'Y'
my_scissor = 'Z'

total_points = 0

with open('input.txt') as game_file:

  for line in game_file.readlines():
    options = str(line).split(" ")

    enemy_opt = options[0].strip()
    my_opt = options[1].strip()

    if my_opt == my_rock:
      total_points += rock_points

      if enemy_opt == enemy_rock:
        total_points += draw_points
      elif enemy_opt == enemy_scissor:
        total_points += win_points

    elif my_opt == my_scissor:
      total_points += scissor_points

      if enemy_opt == enemy_scissor:
        total_points += draw_points
      elif enemy_opt == enemy_paper:
        total_points += win_points
    
    elif my_opt == my_paper:
      total_points += paper_points

      if enemy_opt == enemy_paper:
        total_points += draw_points
      elif enemy_opt == enemy_rock:
        total_points += win_points


print(f"Part 1 - Total points: { total_points }")