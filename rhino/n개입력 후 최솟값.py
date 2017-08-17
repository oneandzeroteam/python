n = []

while True:
    n.append(int(input()))
    if input("계속입력: yes / 그만입력:no 입력 ") == "no":
        break

mini = n[0]

for i in n:
    if mini > i:
        mini = i

print(mini)
