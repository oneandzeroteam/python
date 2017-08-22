#factorial.py

factorial = 1
number = int (input ("input the number wanted to factorial: "))
print (number)

if (number == 1):
		factorial = 1
else :
	for i in range (1, number+1):
		factorial = factorial * i

print (factorial)