n = []

while True:
    n.append(int(input()))
    if input("계속입력? y / n ") == "n":
        break

mini = n[0]

for i in n:
    if mini > i:
        mini = i

print(mini)
