"""
The form asks a series of 26 yes-or-no questions marked a through z.

Individual answers are on new lines
Group answers are separated by blanks
"""

f = open("input_20201206.txt", "r")
in_data = f.read()
f.close()

groups = in_data.split("\n\n")
answer_length = 0

# Part 1: Find the unique number of letters per group
for group in groups:
    unique_answers = set()

    for person in group.split("\n"):
        unique_answers |= set(person)

    answer_length+=len(unique_answers)

print(answer_length)

answer_length = 0

# Part 2: Find the shared number of letters per group
for group in groups:
    shared_answers = set("abcdefghijklmnopqrstuvwxyz")

    for person in group.split("\n"):
        shared_answers &= set(person)

    answer_length+=len(shared_answers)

print(answer_length)