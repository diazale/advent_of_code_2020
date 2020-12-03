# We're given a grid of dots and hashes, and traverse it from the top left to bottom right
# We traverse it by going right 3 and down 1
# When we hit the right edge, repeat the line that we're on

# Every time we hit a tree, increment the counter

# Import the data
f = open("input_20201203.txt", "r")

tree_map = list()

# Strings are apparently immutable, so transform them to lists
for line in f.readlines():
    tree_map.append(list(line.strip("\n")))

f.close()

def count_trees(tree_map_, lr_, ud_):
    """
    :param tree_map_: The tree map
    :param lr_: Left-right increment
    :param ud_: Up-down increment
    :return: Count of trees encountered
    """
    tree_count_ = 0 # initialize the tree count
    lr_coord_ = 0 # initialize left-right coord

    # Move down the list
    for ud_coord_ in range(0, len(tree_map_), ud_):
        # Each row supports wrapping, so take the modulo of the length of the line
        lr_coord_ = lr_coord_ % len(tree_map_[ud_coord_])

        if tree_map_[ud_coord_][lr_coord_]=="#":
            tree_count_ += 1

        lr_coord_+=lr_

    return tree_count_

# Part 1: slope is down 1, right 3
print(count_trees(tree_map, lr_=3, ud_=1))

# Part 2: Given five sets of slopes, find the product of the numbers of trees in each
coords = [(1,1),(3,1),(5,1),(7,1),(1,2)]
prod = 1

for coord in coords:
    num_trees = count_trees(tree_map, lr_=coord[0], ud_=coord[1])
    print(num_trees)
    prod = prod*num_trees

print(prod)