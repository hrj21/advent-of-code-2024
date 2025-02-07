# read data
with open('2025_day2_input.txt') as file:
    raw = file.readlines()

lines = []

# define list of lists
for line in raw:
    values = line.split()
    values = [int(x) for x in values] # list comprehension
    lines.append(values)

# iterate over each line and pair of adjacent values
results = []

for line in lines:
    d = []
    # find differences between adjacent values
    for i, num in enumerate(line):        
        if(i < len(line)-1):
            d.append(num - line[i+1])
    # mark as safe if abs difference <4, and all values positive or negative
    if(max(abs(x) for x in d) < 4 and ( all(x > 0 for x in d) or all(x < 0 for x in d) )):
        results.append("safe")
    # otherwise mark as unsafe
    else:
        results.append("unsafe")

# find number of safe results
len([x for x in results if x == "safe"])
