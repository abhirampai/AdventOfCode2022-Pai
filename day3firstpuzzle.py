import string

sum_of_priorities = 0

for rucksacks in input.split("\n"):
  first_compartment = rucksacks[0:len(rucksacks)//2]
  second_compartment = rucksacks[len(rucksacks)//2:]
  common_element = list(set(first_compartment).intersection(second_compartment))
  sum_of_priorities += string.ascii_letters.index(common_element[0]) + 1

print(sum_of_priorities)
