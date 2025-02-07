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

# count number of times each item in l1 appears in l2
reps = []

for value in l1:
    reps.append(l2.count(value) * value)

# find the sum
sum(reps)