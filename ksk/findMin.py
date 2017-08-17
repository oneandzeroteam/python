def find_small(n_list):
    minimum = n_list[0]
    for i in n_list[1:]:
        if i < minimum:
            minimum = i

    print(minimum)


li = list(map(int, input().split(' ')))
find_small(li)
