nList = [17, 92, 18, 33, 58, 7, 33, 43]

maximum = nList[0]
maxIndex = 0
for i in range(1, len(nList)):
    if nList[i] > maximum:
        maximum = nList[i]
        maxIndex = i

print(maxIndex)
