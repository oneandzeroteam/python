n = input().split(' ')  #순규오빠 코드 참조
n = list(set(n))
s = " "
result = []

'''
from itertools import combinations
print(list(combinations(n,2)))
'''

for i in range(1,len(n)):
    for j in range(i,len(n)):      
            s = n[i-1] + "-" + n[j]
            result.append(s)


print(n)
print(result)

