# read data
with open('2025_day1_input.txt') as file:
    lines = file.readlines()

# define the lists
l1 = []
l2 = []

for line in lines:
    values = line.split()
    l1.append(int(values[0]))
    l2.append(int(values[1]))

# sort the lists
l1.sort()
l2.sort()

# find pairwise differences
d = [abs(l1-l2) for l1, l2 in zip(l1, l2)]

# find the sum
sum(d)