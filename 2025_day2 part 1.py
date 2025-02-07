# read data
with open('2025_day2_input.txt') as file:
    raw = file.readlines()

lines = []

# define list of lists
for line in raw:
    values = line.split()
    values = [int(x) for x in values] # list comprehension
    lines.append(values)

# not functional yet
results = []

for line in lines:
    for i, num in enumerate(line):
        d = []
        if(i < len(line)-1):
            d.append(num - line[i+1])
            if(max(abs(x) for x in d) < 4 and ( all(x > 0 for x in d) or all(x < 0 for x in d) )):
                results.append("safe")
            else:
                results.append("unsafe")
        else:
            results.append("unsafe")

results

len([x for x in results if x == "safe"])