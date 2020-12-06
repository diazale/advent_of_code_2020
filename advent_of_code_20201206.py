"""
The form asks a series of 26 yes-or-no questions marked a through z.

Individual answers are on new lines
Group answers are separated by blanks
"""

f = open("input_20201206.txt", "r")

answers = list()

for line in f.readlines():
    answers.append(line.strip("\n"))

f.close()

# Part 1: Count the sum of unique answers given by each group
unique_answers = 0
answer_set = set()

for a in answers:
    if len(a) > 0:
        answer_set.update(a)
    else:
        unique_answers+=len(answer_set)
        answer_set = set()

# Final item
unique_answers+=len(answer_set)
#print(unique_answers)

# Part 2: Count the sum where everyone answered the same
# So, same as before, but with set intersections?
answer_set = set()
shared_answers = 0
group_answers = list()
first = True

for a in answers:
    print(a)

    if first:
        # First person in a group
        # Update the set with whatever this element is
        answer_set.update(a)
        first = False
    elif a=="":
        # If it's a new line, we're on a new group
        # Reset the indicator variable and add the number of shared answers
        first = True
        shared_answers+=len(answer_set)
        print(len(answer_set), shared_answers)
        answer_set = set()
    else:
        # Otherwise intersect the elements within our set
        answer_set = answer_set & set(a)

shared_answers+=len(answer_set)
print(shared_answers)