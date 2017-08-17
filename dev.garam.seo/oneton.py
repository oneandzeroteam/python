#oneton.py

# add one to n

n = int(input())

def sigma(n):
	sigma = 0
	for i in range (1, n):
		sigma = sigma + i 
	return sigma


sigma = sigma(n)
print (sigma)
