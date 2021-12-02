import os
import sys

with open(os.path.join(sys.path[0], 'input.txt')) as file:
    commands = file.readlines()

###########################
depth = 0
horizontal_pos = 0
for command in commands:
    direction, value = command.split(' ')
    val = int(value)
    if direction == 'forward':
        horizontal_pos += val
    if direction == 'down':
        depth += val
    if direction == 'up':
        depth -= val

print(depth*horizontal_pos)
############################
depth = 0
horizontal_pos = 0
aim = 0
for command in commands:
    direction, value = command.split(' ')
    val = int(value)
    if direction == 'down':
        aim += val
    if direction == 'up':
        aim -= val
    if direction == 'forward':
        horizontal_pos += val
        depth += aim*val

print(depth*horizontal_pos)

