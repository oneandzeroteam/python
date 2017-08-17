def sigmaSquare(num):
    if num == 1:
        return 1
    else:
        return num * num + sigmaSquare(num - 1)


number = int(input())
print(sigmaSquare(number))
