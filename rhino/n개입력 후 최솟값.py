n = []

while True:
    n.append(int(input()))
    if input("계속? y / n ") == "n":
        break

mini = n[0]

for i in n:
    if mini > i:
        mini = i

print(mini)
