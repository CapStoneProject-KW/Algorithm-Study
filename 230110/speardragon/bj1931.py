'''
1. N개 회의에 대한 사용표
2. 겹치지 않게 배치하여 최대 개수
3. 회의 끝 동시에 시작 가능
4. 시작하자마자 끝나는 경우도 있음

sol)
finish 정렬, 같으면 start로
하나씩 배치하되, 끝나는 시간을 기준으로 가장 빨리 시작할 수 있는 회의 배치
1) 첫번째건 그냥 배치
2) 첫번째거 f가 남은 것들의 s랑 비교
    f <= s 이면 count + 1
3) for (1, len(hall))
선택할 회의실 번호를 index로 
'''
import sys


def greedy(hall):
    selected_hall = 0
    result = [selected_hall]

    for i in range(1, len(hall)):
        if (hall[selected_hall][1] <= hall[i][0]):
            selected_hall = i
            result.append(selected_hall)

    return len(result)

input = sys.stdin.readline

max_n = int(input())

hall = []
for i in range(max_n):
        a, b = map(int, input().split())
        hall.append((a, b))
print(hall)

hall.sort(key = lambda x : (x[1], x[0])) # finish로 정렬
    

print(greedy(hall))


