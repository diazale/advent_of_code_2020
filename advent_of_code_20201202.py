# Input follows: [min]-[max] [letter]: [password]
# Import the data
f = open("input_20201202.txt", "r")

in_data = list()

for line in f.readlines():
    line = line.replace("\n", "").replace(":", "").split()
    in_data.append(line)

f.close()

##### Part 1: How many passwords fall within the valid range?

counter = 0

for line in in_data:
    min_val = int(line[0].split("-")[0])
    max_val = int(line[0].split("-")[1])
    letter = line[1]
    password = line[2]

    if min_val <= password.count(letter) <= max_val:
        #print(min_val, max_val, letter, password, password.count(letter))
        counter+=1

print(counter)

##### Part 2: The letter must appear in exactly one position
# Note this is index 1, not 0

counter = 0

for line in in_data:
    pos_1 = int(line[0].split("-")[0]) - 1
    pos_2 = int(line[0].split("-")[1]) - 1
    letter = line[1]
    password = line[2]

    if (password[pos_1]==letter or password[pos_2]==letter) and password[pos_1]!=password[pos_2]:
        print(pos_1 + 1, pos_2 + 1, letter, password)
        counter+=1

print(counter)

print(password)
print(password[-3:])