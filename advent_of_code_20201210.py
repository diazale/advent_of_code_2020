"""
Each of the inputs is a "joltage" level for an adapter in your bag
Adapters can take in any joltage 1-3 levels below its rating
The device has a built-in adapter that is 3 levels above the highest rated adapter in the bag
The charging outlet has a joltage of 0
"""

import numpy as np

f = open("input_20201210.txt", "r")
joltages = [int(line.strip("\n")) for line in f.readlines() if line.strip()]
f.close()

# Part 1: Chain all the adapters together from smallest to largest
# Find the number of 1/2/3 level differences
# Multiply the number of 1-jolt differences by 3-jolt differences

# Sort the data and pad it with a zero and a max + 3 value
joltages_sorted = sorted(joltages)
joltages_sorted.insert(0,0)
joltages_sorted.append(max(joltages_sorted) + 3)

diffs = np.diff(np.array(joltages_sorted))
print(np.where(diffs==1)[0].shape[0]*np.where(diffs==3)[0].shape[0])

# Part 2: How many possible valid combinations of adapters are there?
# A combination is valid as long as all differences remain at 3 or less
# If we drop a 3, this is automatically invalid as the difference will now be > 3 (except the ending 3)
# When is it valid to drop a joltage (based on difference)
# 3: Only when it is the last value, since this is dynamic (element idx [-2] takes over [-1])
# 2: Only when the following diff is 1 or 2
# 1: 