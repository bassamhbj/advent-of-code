# Advent of Code 2022 Day 2 - Part 2

rock_points = 1
paper_points = 2
scissor_points = 3

lost_points = 0
draw_points = 3
win_points = 6

enemy_rock = 'A'
enemy_paper = 'B'
enemy_scissor = 'C'

loss_key = 'X'
draw_key = 'Y'
win_key = 'Z'

total_points = 0

with open('input.txt') as game_file:

  for line in game_file.readlines():
    options = str(line).split(" ")

    enemy_opt = options[0].strip()
    result_key = options[1].strip()

    if result_key == loss_key:
      total_points += lost_points

      if enemy_opt == enemy_rock:
        total_points += scissor_points
      elif enemy_opt == enemy_paper:
        total_points += rock_points
      elif enemy_opt == enemy_scissor:
        total_points += paper_points

    elif result_key == draw_key:
      total_points += draw_points

      if enemy_opt == enemy_rock:
        total_points += rock_points
      elif enemy_opt == enemy_paper:
        total_points += paper_points
      elif enemy_opt == enemy_scissor:
        total_points += scissor_points

    elif result_key == win_key:
      total_points += win_points

      if enemy_opt == enemy_rock:
        total_points += paper_points
      elif enemy_opt == enemy_paper:
        total_points += scissor_points
      elif enemy_opt == enemy_scissor:
        total_points += rock_points

print(f"Part 2 - Total points: { total_points }")