def sigma(num):
    if num == 1:
        return 1
    else:
        return num + sigma(num-1)

number = int(input())
print(sigma(number))