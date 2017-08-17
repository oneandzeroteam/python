list = [17,92,13,22,55,40]

# print(max(list))

maxi = 0

for i in list:
    if maxi < i:
        maxi = i

print(list.index(maxi))
