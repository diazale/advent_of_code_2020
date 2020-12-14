"""
The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer
input values. After staring at them for a few minutes, you work out what they probably mean:
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
"""

import re

def parse_direction(in_str):
    """
    :param in_str: Input string (letter followed by numbers)
    :return: Tuple with letters followed by numbers
    """
    return in_str[0], list(map(int, re.findall(r'\d+', in_str)))[0] # return first number

def turn(cur_dir, new_dir, degrees):
    """
    :param in_dir: current direction
    :param direction: direction to turn
    :param degrees: degrees to turn
    :return:
    """
    # Possible turns: 0, 90, 180, 270
    #                 N   E   S   W
    #                 E   S   W   N
    #                 S   W   N   E
    #                 W   N   E   S

    # Make everything a right turn
    # 90 left = 270 right
    # 180 left = 180 right
    # 270 left = 90 right
    # Add 180 and take mod 360 later
    if new_dir=="L":
        if degrees==90:
            degrees = 270
        elif degrees==270:
            degrees = 90

    degrees = degrees % 360

    if degrees==90:
        if cur_dir=="N":
            return "E"
        elif cur_dir=="E":
            return "S"
        elif cur_dir=="S":
            return "W"
        elif cur_dir=="W":
            return "N"
    elif degrees==180:
        if cur_dir=="N":
            return "S"
        elif cur_dir=="E":
            return "W"
        elif cur_dir=="S":
            return "N"
        elif cur_dir=="W":
            return "E"
    elif degrees==270:
        if cur_dir=="N":
            return "W"
        elif cur_dir=="E":
            return "N"
        elif cur_dir=="S":
            return "E"
        elif cur_dir=="W":
            return "S"

f = open("input_20201212.txt", "r")
directions = [line.strip("\n") for line in f.readlines() if line.strip()]
f.close()

# Part 1: Figure out where the navigation instructions lead.
# What is the Manhattan distance between that location and the ship's starting position?
# Might be worth it to set this up as vector math
distance_ns = 0
distance_ew = 0

prev_dir="E"

for direction in directions:
    action = parse_direction(direction)[0]
    value = parse_direction(direction)[1]

    if action=="N":
        distance_ns+=value
    elif action=="S":
        distance_ns-=value
    elif action=="E":
        distance_ew+=value
    elif action=="W":
        distance_ew-=value
    elif action in ["L","R"]:
        prev_dir = turn(prev_dir, action, value)
    elif action=="F":
        if prev_dir=="N":
            distance_ns+=value
        elif prev_dir=="S":
            distance_ns-=value
        elif prev_dir=="E":
            distance_ew+=value
        elif prev_dir=="W":
            distance_ew-=value

    print(action, value)
    print("NORTH:", distance_ns, "EAST:", distance_ew)

print(abs(distance_ns) + abs(distance_ew))

#1244 is too low