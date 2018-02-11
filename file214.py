fhand = open("contacts214.txt")
count = 0
for line in fhand:
    if line.startswith("to"):
        print(line)
