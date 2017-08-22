#  입력받기
name_list = input().split(' ')

#  중복되는 값 빼고 리스트 생성
name_set = list(set(name_list))

#  딕셔너리에 키값으로 이름 밸류값으로 0 생성
name_count = {name_set[i] : 0 for i in range(len(name_set)) }

#  중복되는 이름을 담을 리스트 생성
duplicate_name_list = []

#  이름이 나오면 카운트 1 증가
for name in name_list:
    if name in name_set:
        name_count[name] += 1
        #  카운트가 2이면 중복이름리스트에 값 추가
        if name_count[name] == 2:
            duplicate_name_list.append(name)

#  출력
print(duplicate_name_list)
