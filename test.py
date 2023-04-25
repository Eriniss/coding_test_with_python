# 배열 안에 데이터 삭제

arr = [1, 4, 6, 8, 8, 9]
remove_set = [4, 8]
result = []

result = [i for i in arr if i not in remove_set]

print(result)
