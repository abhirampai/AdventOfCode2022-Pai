input_ranges = input.split("\n")

count = 0

for input_range in input_ranges:
  x_range, y_range = input_range.split(",")
  x_range_split = x_range.split("-")
  y_range_split = y_range.split("-")
  range_1 = [*range(int(x_range_split[0]),int(x_range_split[1])+1)]
  range_2 = [*range(int(y_range_split[0]), int(y_range_split[1])+1)]
  if(len(list(set(range_1) & set(range_2)))>0):
    count += 1

print(count)
