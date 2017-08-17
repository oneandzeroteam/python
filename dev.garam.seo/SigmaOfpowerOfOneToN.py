#sigmaOfPowerOfOnetoN

n = int (input("input the n "))

def sigmaOfPower(n):
	sigmaOfPower = 0
	for i in range (1, n+1):
		sigmaOfPower = sigmaOfPower + pow(i,2)
	return sigmaOfPower

sigmaOfPower = sigmaOfPower(n);
print (sigmaOfPower)