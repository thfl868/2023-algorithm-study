n, m = map(int, input().split())

array = []
for i in range(n):
	array.append(int(input())
    
#한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

d[0] = 0
for i in range(n): #i는 화폐단위
	for j in range(array[i], m+1): #j는 금액
    	if d[j - array[i]] != 10001 : 
        	d[j] = min(d[j], d[j - array[i]] + 1)
            
#계산된 결과 출력
if d[m] == 10001 : 
	print(-1)
else:
	print(d[m])

