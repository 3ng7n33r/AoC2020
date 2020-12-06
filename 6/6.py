with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n\n")
#%%
def countUnique(lines): # takes a list of strings and returns a list of int counting unique chars per string    
    uniqueAns = []
    for line in lines:
        tempset = set()
        for char in line:
            if char.isalpha():
                tempset.add(char)
        uniqueAns.append(len(tempset))
    return uniqueAns

print(sum(countUnique(lines)))

#%% part 2

def countEvery(lines): # takes a list of strings and returns a list of int counting answers
    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")
    
    everyAnswer = []
    for line in lines:
        sets = []
        for answer in line:
            tempset = set()
            for char in answer:
                if char.isalpha():
                    tempset.add(char)
            sets.append(tempset)
        everyAnswer.append(len(set.intersection(*sets)))
    return everyAnswer

print(sum(countEvery(lines)))
    