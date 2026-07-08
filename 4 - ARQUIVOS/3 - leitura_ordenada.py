names = []

with open("names.txt", "r", encoding="utf-8") as file:
  for line in file:
    names.append(line.rstrip())

for name in names:
  print(name)