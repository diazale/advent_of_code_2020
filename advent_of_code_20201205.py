"""
The first 7 characters will either be F or B;
these specify exactly one of the 128 rows on the plane (numbered 0 through 127).
Each letter tells you which half of a region the given seat is in.
Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63)
or the back (64 through 127).
The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane
(numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the
lower half, while R means to keep the upper half.

Every seat also has a unique seat ID: multiply the row by 8, then add the column.
"""

f = open("input_20201205.txt", "r")

seat_ids = list()

# Strings are apparently immutable, so transform them to lists
for line in f.readlines():
    seat_ids.append(line.strip("\n"))

f.close()

def convert_to_binary_string(in_str):
    """
    :param in_str: 10 characters. First 7 are F (0) and B (1), last 3 are R (1) or L (0)
    :return: Pair of binary strings
    """
    fb_ = in_str[:7]
    lr_ = in_str[-3:]
    return fb_.replace("F","0").replace("B","1"),  lr_.replace("R","1").replace("L","0")

def seat_id(fb_, lr_):
    """
    :param fb_: F/B value
    :param lr_: L/R value
    :return: Returns FB*8 + LR
    """
    return fb_*8 + lr_

# Part 1: What is the highest seat ID?
max_seat = 0
for seat in seat_ids:
    fb, lr = convert_to_binary_string(seat)
    sid = seat_id(int(fb,2), int(lr,2))
    if sid > max_seat:
        max_seat = sid

print(max_seat)
print()

# Part 2:
"""
It's a completely full flight, so your seat should be the only missing boarding pass in your list.
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft,
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
"""

numeric_ids = list()

# Enumerate the IDs of all existing seats
# Seats cannot be FFFFFFF or BBBBBBB
# So, find seats with a gap between IDs that are not FFFFFFF or BBBBBBB
for seat in seat_ids:
    fb, lr = convert_to_binary_string(seat)
    sid = seat_id(int(fb, 2), int(lr, 2))
    if not fb in ["FFFFFFF","BBBBBBB"]:
        numeric_ids.append(sid)

# Get the lowest and highest values
lowest = min(numeric_ids)
highest = max(numeric_ids)

# Find the difference between the two sets
print(set(list(range(lowest, highest))) - set(numeric_ids))

