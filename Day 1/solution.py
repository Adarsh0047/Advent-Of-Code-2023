with open("input.txt", "r") as f:
    lines = f.readlines()
numbs = []
for line in lines:
    numb = []
    for char in line:
        if char.isdigit():
            numb.append(char)
    numbs.append(numb)
numbs = [(num[0],num[-1])for num in numbs]
numbs = [num[0]+num[-1] if len(num) > 1 else num[0] for num in numbs]
sum = 0
for num in numbs:
    sum += int(num)
print(sum)