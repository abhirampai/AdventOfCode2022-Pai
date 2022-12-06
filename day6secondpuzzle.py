processed_input_list = [{
  "value": input[x:x + 14],
  "index_of_last_element": x + 14
} for x in range(0,
                 len(input) - 14)]

for processed_input in processed_input_list:
  if (len(set(processed_input["value"])) == len(processed_input["value"])):
    print(processed_input["value"])
    print(processed_input["index_of_last_element"])
    break
