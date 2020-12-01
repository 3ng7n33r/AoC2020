with open("input.txt", "r") as f:
        nums = f.read().strip().split("\n")

for number1 in nums:
    for number2 in nums:
        for number3 in nums:
            if int(number1) + int(number2) + int(number3)== 2020:
                print(int(number1)*int(number2)*int(number3))