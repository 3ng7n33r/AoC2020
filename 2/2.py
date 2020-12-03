import re

with open("input.txt", "r") as f:
        lines = f.readlines()

# %% part 1        
validpw1 = 0
for line in lines:        
        result = re.findall('^(\d+)-(\d+) (\w): (\w+)', line)
        minchar, maxchar, char, pw = int(result[0][0]), int(result[0][1]), result[0][2], result[0][3]
        count = 0
        for i in pw:
            if i == char:
                count+=1
        if minchar <= count <= maxchar:
            validpw1+=1
            
# %% part 2

validpw2 = 0
for line in lines:        
        result = re.findall('^(\d+)-(\d+) (\w): (\w+)', line)
        charpos1, charpos2, char, pw = int(result[0][0]), int(result[0][1]), result[0][2], result[0][3]

        if (pw[charpos1-1] == char) != (pw[charpos2-1] == char):
            validpw2+=1            
            entries = list(map(lambda l: correct_entry(*process_line(l)), lines[0:-1]))