k = input.split("\n")
elfsArray = []
acc = 0
for calories in k:
  if(calories==""):
    elfsArray.append(acc)
    acc=0
  else:
    acc+=int(calories)

elfsArray.sort(reverse=True)
x = elfsArray[0:3]
print(sum(x))
