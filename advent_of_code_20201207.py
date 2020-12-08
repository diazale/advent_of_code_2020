"""
Input is a list of bag colours and what they contain

e.g.

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

from collections import defaultdict

f = open("input_20201207.txt", "r")
in_data = f.read()
f.close()

bag_rules = in_data.split("\n")

# Part 1
# Find out how many bag colours can eventually contain at least one shiny gold bag
# 1. First identify the bags that contain shiny gold bags
# 2. Then identify those that contain bags from (1)
# 3. Continue until all bags have been identified

core_rule = "shiny gold"
core_rules = list()
core_rules.append(core_rule)
rule_count = 0

for core_rule in core_rules:
    # Go through all the bag rules that contain "shiny gold" or contain something that contains it
    # These are our "core rules"
    for rule in bag_rules:
        # Cycle through all the bag rules we have
        if core_rule in rule:
            # If the current rule contains a core rule, append it to the existing core rule
            # Increment the counter (since it contains a shiny gold rule)
            # Remove the current rule from the list so we don't pick it up again
            print(rule)
            print(core_rules[-1])
            rule_count+=1
            core_rules.append(rule.split(" bag")[0])
            bag_rules.remove(rule)

print(rule_count)

# Part 2: Identify how many bags a shiny gold bag must contain
# In our data, we start with:
# shiny gold bags contain 1 shiny coral bag, 5 posh white bags, 3 wavy cyan bags.

f = open("input_20201207.txt", "r")
in_data = f.read()
f.close()

bag_rules = in_data.split("\n")

def parse_rule(in_str):
    # Rules are written as:
    # 1 rule: "[colour] bags contain [N] [other colour] bags
    # 2+ rule: "[colour bags contain [N1] [colour bags], [N2] [other colour bags], ... [Nk] [last colour bags]"
    # Get rid of "contain " at the start
    # Get rid of period at the end
    temp_str = in_str.split(",")
    temp_str[0] = (temp_str[0].split(" contain "))[1]
    temp_str = [t.strip(" .") for t in temp_str]
    return temp_str

def rule_colour(in_str):
    return in_str.split(" bags contain")[0].strip()

def parse_subrule(in_str):
    # Two cases:
    # [Colour] bags contain no other bags.
    # Or each element is [N] [colour] [bag(s)]
    # Returns a tuple of colour and number
    if "no other bags" in in_str:
        # Base case
        num = 0
        col = in_str.split(" bags contain no other bags")[0]
    else:
        # Recursive case: Return
        num = int(in_str.split()[0].strip(" "))
        col = " ".join(in_str.split()[1:-1])
    return col, num

colour_rules = defaultdict()

for rule in bag_rules:
    if "no other bags" in rule:
        # If there are no other bags, this rule has nothing associated with it
        # {"dull chartreuse":[]}
        colour_rules[rule_colour(rule)] = []
    else:
        # If there are rules associated with this, list them
        # {"light beige": [("dim purple", 4), ("posh red", 1), ("clear aqua", 4), ("striped coral", 1)]}
        colour_rules[rule_colour(rule)] = [parse_subrule(subrule) for subrule in parse_rule(rule)]

def count_bags(colour_rules_):
    sumval = 1

    if len(colour_rules) > 0:
        for subrule_ in colour_rules_:
            sumval += subrule_[1] * count_bags(colour_rules[subrule_[0]])
    return sumval

count = 0
# Starting with the rule for shiny gold bags, count all the bags
c = "shiny gold"
print(count_bags(colour_rules[c]) - 1)