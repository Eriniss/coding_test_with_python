# 거스름돈

# 문제 요점
# 가장 큰 화폐 단위부터 돈을 거슬러 주는 것. 즉, 뒤의 경우와 상관없이 가장 큰 수부터 차감해 간다.

# 문제 풀이
# 화폐단위를 배열로 지정한다. 지정된 배열의 숫자를 내림차순으로 나열한다.
# 배열을 순회하며 거스름돈과 비교한다. 만약, 화폐단위가 거스름돈보다 크다면 else구문으로 넘어간다.

change = 1260
monetary_unit = [500, 100, 50, 10]
count = 0 

for coin in monetary_unit:
    count += change // coin # 몫을 count에 더한다.
    change %= coin # 화폐단위로 나눈 잔돈의 나머지를 change에 새로 할당한다.

print(count)