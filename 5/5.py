def makebinary (lines, converters):
    for i in range(len(lines)):
        for old, new in converters:
            lines[i] = lines[i].replace(old, new)
    return lines

def splitrowseat(lines, n):
    for i in range(len(lines)):
        lines[i] = [lines[i][j:j+n] for j in range(0, len(lines[i]), n)]
    return lines

with open("input.txt", "r") as f:
    lines = f.readlines()
    
converters = [("F", "0"), ("B", "1"), ("L", "0"), ("R", "1")]

lines = splitrowseat(makebinary(lines, converters), 7)

seatIDs = []
for row, seat in lines:
    seatIDs.append(int(row,2) * 8 + int(seat,2))
print(max(seatIDs))
    
#%% part 2

seatIDs.sort()
for i in range(len(seatIDs)):
    if seatIDs[i]+1 != seatIDs[i+1]:
        print(seatIDs[i]+1)
        break



