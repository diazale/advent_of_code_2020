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
bag_count = 0

core_rules = list()
core_rules_multiplier = list()
core_rules.append("shiny gold")
core_rules_multiplier.append(1)

# Two types of rules: plural and singular
# "shiny gold bags contain 1 shiny coral bag, 5 posh white bags, 3 wavy cyan bags."
# "dim yellow bags contain 3 striped white bags."

# Identify the first set of rules and build out from there?
for core_rule in core_rules:
    for rule in bag_rules:
        if rule[:len(core_rule)]==core_rule:
            # Sub-rules are identified by the word "contain" or "contains"
            print(rule)