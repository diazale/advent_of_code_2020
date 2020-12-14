"""
All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions
immediately up, down, left, right, or diagonal from the seat). The following rules are applied to
every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.

Reapply these rules iteratively
"""

f = open("input_20201211.txt", "r")
seats = [list(line.strip("\n")) for line in f.readlines() if line.strip()]
f.close()

def occupied_count(seats_, row_, col_):
    """
    :param seats_: Full list of seats
    :param seat_: Seat coordinate (row, col)
    :return: Check the square around a seat (the 8 positions). If 4+ are occupied (#), set it to empty (L)
    The 8 positions are row, col +/-1
    Edge cases: Literal edges (row = 0, max; col = 0, max)
    """
    neighbours = list()
    valid_rows = [0]
    valid_cols = [0]

    # Edge cases: Row is first or last
    # Edge cases: Col is first or last
    if row_!=0:
        # Row is non-zero. Okay to go up
        valid_rows.append(-1)
    if row_!=(len(seats_) - 1):
        # Row is not last. Okay to go down
        valid_rows.append(1)
    if col_!=0:
        # Col is non-zero, okay to go left
        valid_cols.append(-1)
    if col_!=len(seats_[0]) - 1:
        # Col is not last, okay to go right
        valid_cols.append(1)

    for r_ in valid_rows:
        for c_ in valid_cols:
            if not (r_==0 and c_==0):
                # Skip the seat itself
                try:
                    neighbours.append(seats_[row_ + r_][col_ + c_])
                except IndexError:
                    print("error", r, c)

    return neighbours.count("#")

# Part 1: Iterate until the seating becomes stable.
# How many seats become occupied?

cur_seats = seats.copy()
next_seats = list()

counter=0
changes = True
while changes:
    # Run this loop as long as there are changes
    # Assume there are no changes to start
    changes = False

    counter+=1

    print("Iteration", counter)

    for r in range(0, len(cur_seats)):
        row = list()
        counts = list()
        for c in range(0, len(cur_seats[r])):
            # Check how many neighbouring seats are occupied
            if cur_seats[r][c]!=".":
                # If it's a L or #, find number neighbours (nn) and change flag to True
                nn = occupied_count(cur_seats, r, c)
                counts.append(nn)

                if nn==0 and cur_seats[r][c]=="L":
                    # L with zero neighbours turns to #
                    row.append("#")
                    changes = True
                elif nn>=4 and cur_seats[r][c]=="#":
                    # # with 4+ neighbours turns to L
                    row.append("L")
                    changes = True
                else:
                    # no change made
                    row.append(cur_seats[r][c])

            elif cur_seats[r][c]==".":
                row.append(".")

        #print("curr row", cur_seats[r])
        #print("next row", row)
        #print("counts: ", counts)
        next_seats.append(row)

    #print()
    cur_seats = next_seats.copy()
    next_seats = list()

counter = 0
for r in range(0, len(cur_seats)):
    counter+=cur_seats[r].count("#")

print(counter)

# Part 2
# Continue looking in each direction for a free spot
