# find the two entries that sum to 2020 and then multiply those two numbers together.

import numpy as np
from numpy import loadtxt

values = loadtxt("input_20201201_1.txt")
print(values, values.shape)

sum_matrix = np.add.outer(values, values)

# Get the indices of values that sum to 2020
idx_sum_2020 = np.where(sum_matrix==2020)[1]

product = values[idx_sum_2020][0]*values[idx_sum_2020][1]
print(product)

##### Part 2: Same, but with 3 values, not 2
sum_matrix = np.add.outer(np.add.outer(values, values), values)

# Get the indices of values that sum to 2020
idx_sum_2020 = np.where(sum_matrix==2020)[1]

print(idx_sum_2020)

product = values[idx_sum_2020][0]*values[idx_sum_2020][1]*values[idx_sum_2020][2]
print(product)