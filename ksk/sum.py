def sum (n):
    if n > 1:
        return n + sum(n-1)
    return 1


print(sum(int(input())))