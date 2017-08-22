#combination.py

namesList = input ("input the names: ")
slicedNamesList = namesList.split(" ")

#remove duplicate name
setSlicedNamesList=set(slicedNamesList)
unsetSlicedNamesList = list (setSlicedNamesList)
print (unsetSlicedNamesList)

for i in range (1, len(unsetSlicedNamesList)):
	for j in range (i, len(unsetSlicedNamesList)):
		print (unsetSlicedNamesList[i-1] + "-" + unsetSlicedNamesList [j])








