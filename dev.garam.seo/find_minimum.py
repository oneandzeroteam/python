#find_minimum

NumberLists = list( int(x) for x in input("input numbers.").split(' '))

print ("the NumberLists is: ", NumberLists)

minimum = NumberLists[0]
for i in NumberLists :
	if minimum > i:
		minimum = i

print ("the minimum number of list is : ", minimum)

