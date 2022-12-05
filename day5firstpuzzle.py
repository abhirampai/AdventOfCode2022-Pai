import re

def pop_and_insert(count, src, dest):
  for i in range(0, count):
    element_to_be_inserted = crate_stacks[src - 1].pop(0)
    crate_stacks[dest - 1].insert(0, element_to_be_inserted)
    
for instruction in instructions.split("\n"):
  count, src, dest = list(map(int, re.findall(r'\d+', instruction)))
  pop_and_insert(count, src, dest)

output = ""
for stacks in crate_stacks:
  output += stacks[0]

print(output)
