n = input().split(' ')  #순규오빠 코드 참조
n = list(set(n))
s = " "
result = []

'''
from itertools import combinations
print(list(combinations(n,2)))
'''

print(n)

for i in range(0,len(n)):
    for j in range(0,len(n)):
            if n.index(n[i]) > n.index(n[j]):
                s = n[i] + "-" + n[j]
                result.append(s)

print(result)
