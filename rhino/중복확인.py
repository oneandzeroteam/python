n = []
output = []

while True:
    n.append(input())
    if input("계속입력? y / n ") == "n":
        break

for i in n:
    if n.count(i) >= 2:
        output.append(i)

print(list(set(output)))    
    



'''
nn = list(set(n))
print(nn)

'''
'''
for i in n:
    print(i)
    if i not in nn:
        output.append(" ")

print(output)

'''
'''
output = n - nn
print(output)
'''



