k = (17, 92, 18, 33, 58, 7, 33, 42)
i = 0
for n in k:
    if n[i] > n[i+1]:
        i=i+1
    elif n[i] < n[i+1]:
        print (n)

