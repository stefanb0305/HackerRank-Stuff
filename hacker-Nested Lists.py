amount = int(raw_input())
list = []
for _ in range(amount):
    name = raw_input()
    score = float(raw_input())
    sublist = []
    sublist.append(name)
    sublist.append(score)
    list.append(sublist)


min = list[0][1]
newlist = []

grades = []
for d in range(amount):
    grades.append(list[d][1])


sortedgrades = sorted(grades)
secondlow = sortedgrades[1]
counter = 0


ma =2
while counter < 1:
    if secondlow > sortedgrades[0]:
        counter += 1
    else:
        secondlow = sortedgrades[ma]
        ma += 1


for i in range(amount):
    if list[i][1] == secondlow:
        newlist.append(list[i][0])
        
newlist = sorted(newlist)
for l in newlist:
    print l

        
