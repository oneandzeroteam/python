#FindSameName


namesList = []
slicedNamesList = []
sameNamesList = []
sameNamesSet = []

namesList = input ("input the names: ")
#print (namesList)

slicedNamesList = namesList.split(" ")
print (slicedNamesList)

for i in range (0, len(slicedNamesList)):
	if (slicedNamesList.count(slicedNamesList[i]) >= 2):
		sameNamesList.append(slicedNamesList[i])
print (set(sameNamesList))
