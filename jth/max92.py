hello = [17, 92, 18, 33, 58, 7, 33, 42]
k = 0
for number in hello:
    if number >= k:
        k = number
    else:
        k = k
print(k)

#원래는 첫번째랑 두번째를 비교하고 싶었는데 range(len())를 쓰는 방법으로 두번째를 뭐라고 칭해야 할지 몰라서 그냥 이렇게 했어요!!
