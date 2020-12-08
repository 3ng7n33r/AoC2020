import re

with open("input.txt", "r") as f:
    lines = f.readlines()

def gameloop(lines):
    visited = set()
    set_noop = set()
    set_jump = set()
    
    i = 0
    acc = 0
    while i not in visited and i != len(lines):
        visited.add(i)
        if re.search('acc \+', lines[i]):
            acc += int(re.findall('\d+', lines[i])[0])
            i += 1
        elif re.search('acc \-', lines[i]):
            acc -= int(re.findall('\d+', lines[i])[0])
            i += 1
        elif re.search('jmp \+', lines[i]):
            set_jump.add(i)
            i += int(re.findall('\d+', lines[i])[0])
        elif re.search('jmp \-', lines[i]):
            set_jump.add(i)
            i -= int(re.findall('\d+', lines[i])[0])
        else:
            set_noop.add(i)
            i +=1
    return (acc, i, set_jump, set_noop, visited)

print (gameloop(lines)[0])

# %% part 2 783 too low

jumplist = sorted(gameloop(lines)[2])
noplist = sorted(gameloop(lines)[3])
visited = sorted(gameloop(lines)[4])

for jump in jumplist:
    newlines = lines.copy()
    newlines[jump] = newlines[jump].replace("jmp", "nop")
    if gameloop(newlines)[1] == len(lines):
        print(gameloop(newlines)[0], "Succes: jump in line", jump, "changed")
        break
    
for nop in noplist:
    newlines = lines.copy()
    newlines[nop] = newlines[nop].replace("nop", "jmp")
    if gameloop(newlines)[1] == len(lines):
        print(gameloop(newlines)[0], "Succes: nop in line", nop, "changed")
        break