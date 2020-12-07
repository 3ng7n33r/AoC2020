import re

with open("input.txt", "r") as f:
    lines = f.readlines()
    
result = 0
bags = []
colors = ["shiny gold"]

for color in colors:
    for line in lines:
        bag, contained = line.replace(" bags", "").split(" contain ")
        if re.findall(color, contained):
            if bag not in colors:
                colors.append(bag)
                result += 1

#%% part 2 WIP

result2 = 1
colors = ["shiny gold"]

for color in colors:
    for line in lines:
        bag, contained = line.replace(" bags", "").split(" contain ")
        if re.findall(color, bag):
            colors.append(contained.split(","))
