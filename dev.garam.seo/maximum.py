#maximum.py

list = [17, 92, 18, 33 ,58, 7, 33, 43]

maximum = 0 
index = 0
j = 0
for i in list :
	if i>=maximum:
		maximum = i
		index = j  
	j = j + 1

print (maximum)
print (index)



