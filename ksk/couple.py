name_list = input().split(' ')
length = len(name_list)

for i in range(length - 1):
    for j in range(i + 1, length):
        print(name_list[i] + " - " + name_list[j], end=", ")