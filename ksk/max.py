def max (current_max, index, list):
    if current_max < list[index]:
        current_max = list[index]

    if index+1 == len(list):
        return current_max

    return max(current_max, index+1, list)

list = [17, 92, 18, 33, 58, 7, 33, 42]
print(max(list[0], 0, list))