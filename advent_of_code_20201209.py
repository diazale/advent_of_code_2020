"""
XMAS starts by transmitting a preamble of 25 numbers.
After that, each number you receive should be the sum of any two of the 25 immediately previous numbers.
The two numbers will have different values, and there might be more than one such pair.

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble)
which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?
"""
import itertools

f = open("input_20201209.txt", "r")
numbers = [int(line.strip("\n")) for line in f.readlines() if line.strip()]
f.close()

# Part 1: Find the first number that is not the sum of two of the previous twenty-five
# 25c2 = 300 combinations, so brute force is inefficient
# Try it anyway lol

invalid = 0
invalid_idx = 0

for n in range(24, len(numbers)-1):
    num_list = numbers[n-24:n+1]
    pairs = list(itertools.product(num_list, num_list))
    sums = [p[0] + p[1] for p in pairs]

    if not numbers[n+1] in sums:
        invalid = numbers[n+1]
        invalid_idx = n+1
        print(invalid_idx, invalid)

# Part 2: Find contiguous set of at least two numbers that sum to the invalid number
# The value we want is the sum of the smallest and largest number in this contiguous set

sub_list = numbers[:invalid_idx-1] # Subset our list. This probably doesn't work in general but it does here

class BreakLoop(Exception): pass
list_length = 2

try:
    for list_length in range(2, 50):
        print(list_length)
        for i in range(0, len(sub_list) - list_length + 1):
            if sum(sub_list[i:i+list_length])==invalid:
                raise BreakLoop
except BreakLoop:
    print(sub_list[i:i + list_length])
    print(min(sub_list[i:i + list_length]) + max(sub_list[i:i + list_length]))