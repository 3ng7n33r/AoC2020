import re

with open("input.txt", "r") as f:
    lines = f.readlines()
    
visited = set()

i = 0
acc = 0
while i not in visited:
    visited.add(i)
    if re.search('acc \+', lines[i]):
        acc += int(re.findall('\d+', lines[i])[0])
        i += 1
    elif re.search('acc \-', lines[i]):
        acc -= int(re.findall('\d+', lines[i])[0])
        i += 1
    elif re.search('jmp \+', lines[i]):
        i += int(re.findall('\d+', lines[i])[0])
    elif re.search('jmp \-', lines[i]):
        i -= int(re.findall('\d+', lines[i])[0])
    else:
        i +=1
print (acc)
    