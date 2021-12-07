import os
import sys
from dataclasses import dataclass
from typing import Dict, List

with open(os.path.join(sys.path[0], 'input.txt')) as file:
    lines = file.readlines()


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


vents: Dict[Coordinate, Coordinate] = {}
for line in lines:
    coordinates = line.split('->')
    start = coordinates[0].split(',')
    start_coord = Coordinate(int(start[0]), int(start[1]))
    end = coordinates[1].split(',')
    end_coord = Coordinate(int(end[0]), int(end[1]))
    vents[start_coord] = end_coord


def get_only_vertical_or_horizontal_vents(vents: Dict[Coordinate, Coordinate]):
    good_vents = {}
    for start, end in vents.items():
        if start.x == end.x or start.y == end.y:
            good_vents[start] = end
    return good_vents


good_vents = get_only_vertical_or_horizontal_vents(vents)


def add_to_heat_map(heat_map: Dict[Coordinate, int], fix_number: int, changing_numbers: List[int], x_is_fix: bool):
    for number in changing_numbers:
        if x_is_fix:
            coord = Coordinate(fix_number, number)
        else:
            coord = Coordinate(number, fix_number)
        if coord in heat_map:
            heat_map[coord] += 1
        else:
            heat_map[coord] = 1
    return heat_map


heat_map: Dict[Coordinate, int] = {}
for start, end in good_vents.items():
    if start.x == end.x:
        if end.y > start.y:
            changing_numbers = list(range(start.y, end.y+1))
            heat_map = add_to_heat_map(heat_map, start.x, changing_numbers, True)
        else:
            changing_numbers = list(range(end.y, start.y+1))
            heat_map = add_to_heat_map(heat_map, start.x, changing_numbers, True)
    else:
        if end.x > start.x:
            changing_numbers = list(range(start.x, end.x+1))
            heat_map = add_to_heat_map(heat_map, start.y, changing_numbers, False)
        else:
            changing_numbers = list(range(end.x, start.x+1))
            heat_map = add_to_heat_map(heat_map, start.y, changing_numbers, False)

dangerous_areas = [k for k, v in heat_map.items() if v > 1]
print(len(dangerous_areas))
###########################################################

full_heat_map = heat_map
for start, end in vents.items():
    if start.x == end.x or start.y == end.y:
        continue
    if start.x > end.x:
        x_range = list(range(start.x, end.x-1, -1))
    else:
        x_range = list(range(start.x, end.x+1))
    if start.y > end.y:
        y_range = list(range(start.y, end.y-1, -1))
    else:
        y_range = list(range(start.y, end.y+1))
    for idx, value in enumerate(x_range):
        coord = Coordinate(value, y_range[idx])
        if coord in full_heat_map:
            full_heat_map[coord] += 1
        else:
            full_heat_map[coord] = 1

dangerous_areas = [k for k, v in full_heat_map.items() if v > 1]
print(len(dangerous_areas))
