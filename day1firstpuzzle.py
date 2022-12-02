k = input.split("\n")
elfsArray = []
acc = 0
for calories in k:
  if(calories==""):
    elfsArray.append(acc)
    acc=0
  else:
    acc+=int(calories)

print(max(elfsArray))
