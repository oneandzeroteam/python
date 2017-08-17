#1의 제곱부터 n의 제곱까지의 합을 구하시오.

i = 1
ii = 1
n = int(input("Number : "))
j = 0

while i <= n:
    if i <= n:
      ii = i*i
      j = j + ii
      i = i + 1
    elif i > n:
        j = j + ii
        break

print(j)
