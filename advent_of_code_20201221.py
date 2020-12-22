"""
You start by compiling a list of foods (your puzzle input), one food per line.
Each line includes that food's ingredients list followed by some or all of the allergens the food contains.


"""
from collections import defaultdict

f = open("input_20201221.txt", "r")
in_data = [line.strip("\n") for line in f.readlines() if line.strip()]
f.close()

# Each line is split into foreign ingredients separated by spaces and then "(contains [english])"
foreign_words = list()
potential_allergens = defaultdict(set)

for d in in_data:
    foreign, english = d.split("(contains ")
    foreign = foreign.split()
    english = english.split(",")
    english = [e.strip() for e in english]
    english[-1] = english[-1].strip(")")

    foreign_words.append(foreign)
    #print(foreign)
    #print(english)

    for allergen in english:
        if allergen in potential_allergens.keys():
            # If the allergen already has a set of ingredients, do an intersection
            potential_allergens[allergen] = potential_allergens[allergen].intersection(set(foreign))
        else:
            # Otherwise do an addition
            #print(foreign)
            potential_allergens[allergen].update(foreign)

# Part 1: Figure out which ingredients are not allergens and count them
# From the above we've determined all potential allergens, but not exactly which is which
allergens = set()
for k in potential_allergens.keys():
    allergens.update(potential_allergens[k])
    #print(k, potential_allergens[k])

non_allergens = 0
# Count the ingredients that are not allergens
for foreign in foreign_words:
    # Get the length non-allergens
    non_allergens += len(set(foreign) - allergens)

# Part 2: Find the length of the comma-separated list of allergens
# First figure out which ingredients are allergens
known_allergens = set()
allergen_translations = dict()

for k in potential_allergens.keys():
    print(k, potential_allergens[k])

print()
print("Determining allergens")

while len(known_allergens) < (len(potential_allergens.keys())):
    for k in potential_allergens.keys():
        # Loop through each English allergen
        if len(potential_allergens[k])==1:
            #print(k, potential_allergens[k])
            # If there is exactly one item, then we have determined its translation
            # Add it to the known allergens
            known_allergens.update(potential_allergens[k])
            allergen_translations[k] = list(potential_allergens[k])[0]
        elif len(potential_allergens[k]) > 1 and len(known_allergens) > 0:
            # Otherwise, if we know at least one allergen, remove it
            potential_allergens[k] -= known_allergens

print()

print("Translations:")

for k in allergen_translations.keys():
    print(k, allergen_translations[k])

canonical_ingredients = str()

for k in sorted(list(allergen_translations.keys())):
    canonical_ingredients+=allergen_translations[k] + ","

canonical_ingredients = canonical_ingredients[:-1]
print(canonical_ingredients)