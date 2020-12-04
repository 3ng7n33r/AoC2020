import re

with open("input.txt", "r") as f:
    lines = f.read().split("\n\n")
    
#%% part 1
    
checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
invalidpp = []
for passport in lines:
    for term in checks:
        if not re.search(term, passport):
            invalidpp.append(passport)
            break
print(len(lines)-len(invalidpp))

#%% part 2

checks = [r"\bbyr:\b1[0-9]{3}|\bbyr:\b200[012]",
          r"\biyr:\b201[0-9]|\biyr:\b2020",
          r"\beyr:\b202[0-9]|\beyr:\b2030",
          r"\bhgt:\b1([5-8][0-9]|9[0-3])cm|\bhgt:\b(59|6[0-9]|7[0-6])in",
          r"\bhcl:#\b[0-9a-f]{6}",
          r"\becl:\b(amb|blu|brn|gry|grn|hzl|oth)",
          r"\bpid:\b[0-9]{9}"]
    
invalidpp = []
for passport in lines:
    for term in checks:
        if not re.search(term, passport):
            invalidpp.append(passport)
            break

print(len(lines)-len(invalidpp))