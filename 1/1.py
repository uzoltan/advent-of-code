import os
import sys

with open(os.path.join(sys.path[0], 'input.txt')) as file:
    depth_measurements = file.readlines()
    depth_measurements = [int(measurement) for measurement in depth_measurements]

depth_increase_count = 0
for idx, value in enumerate(depth_measurements[1:], 1):
    if value > depth_measurements[idx-1]:
        depth_increase_count += 1

print(depth_increase_count)


prev_value = 999_999_999
depth_increase_count = 0
for idx, value in enumerate(depth_measurements[:-2]):
    current_value = value + depth_measurements[idx+1] + depth_measurements[idx+2]
    if current_value > prev_value:
        depth_increase_count += 1
    prev_value = current_value

print(depth_increase_count)
