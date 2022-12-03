import string

sum_of_priorities = 0
priority_groups = []

grouped_rucksacks = [input.split("\n")[i * 3:(i + 1) * 3] for i in range((len(input.split("\n")) + 3 - 1) // 3 )]

for rucksacks in grouped_rucksacks:              
  common_element = list(set(rucksacks[0]).intersection(rucksacks[1]).intersection(rucksacks[2]))
  sum_of_priorities += string.ascii_letters.index(common_element[0]) + 1

print(sum_of_priorities)
