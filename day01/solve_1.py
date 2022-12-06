
# Data ingesting
data = []
# file = "day01/test.txt"
file = "day01/input.txt"
with open(file, 'r') as f:
    elf = []
    for line in f.readlines():
        if line != '\n':
            elf.append(int(line.strip()))
        else:
            data.append(tuple(elf))
            elf = []
    data.append(tuple(elf))
    data = tuple(data)

# Solution finding
totals = [sum(x) for x in data]
print(f"Highest elf calories: {max(totals)}")
