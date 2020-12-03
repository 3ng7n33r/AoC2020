with open("input.txt", "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
        
def checktree(i, x, y, line):
    if not i%y:
        col = ((i/y)*x) % (len(line))
        if line[int(col)] == "#":
            return True            
        else:         
            return False
    else:    
        return False

# %% part1        
treecount = 0

for i in range(len(lines)):
    if checktree(i, 1, 2, lines[i]):
        treecount += 1

# %% part 2

xypart2 = [(1,1), (3,1), (5,1), (7,1), (1,2)]
treecount2 = 1

for xy in xypart2:
    x,y = xy
    treecount = 0
    for i in range(len(lines)):
        if checktree(i, x, y, lines[i]):
            treecount += 1
    treecount2 = treecount2 * treecount
