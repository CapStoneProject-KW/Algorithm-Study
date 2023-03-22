import sys
from collections import defaultdict
sys.stdin = open("bj_16924_in.txt")
input = sys.stdin.readline
'''
return:
k
x, y, s
...
xk, yk, sk

(i, j)
cross = [(i,j-1), (i, j-2), (i, j+2)]
'''

def solution(point, size):
    i, j = point[0], point[1]
    count = 0
    answer = []

    for s in range(1, size+1):
        if MAP[i-s][j] == '*' and MAP[i][j-s] == '*' and \
            MAP[i+s][j] == '*' and MAP[i][j+s] == '*':
            # print(point,s)
        # if check[i-s][j] and check[i+s][j] and check[i][j-s] and check[i][j+s]:
            count += 1
            answer.append([i+1, j+1, s])
            check[i][j] = False
            check[i-s][j] = False
            check[i+s][j] = False
            check[i][j-s] = False
            check[i][j+s] = False
        else:
            # print(i, j, count, answer, 'else')
            # print(MAP[i-s][j], MAP[i][j-s], MAP[i+s][j], MAP[i][j+s])
            return count, answer
    # print(i, j, count, answer)
    # print('hi')
    return count, answer


N, M = map(int, input().split())

MAP = []
check = [[False]*M for _ in range(N)]
for i in range(N):
    MAP.append(list(input().strip()))
    for j in range(M):
        if MAP[i][j] == "*": 
            check[i][j] = True

count = 0
answer = []
for i in range(1, N-1):
    for j in range(1, M-1):
        if MAP[i][j] == "*":
            size = min(i, N-i-1, j, M-j-1)
            tmp_cnt, tmp_list = solution((i, j), size)
            # print(check)
            if tmp_list:
                answer.extend(tmp_list)
                count += tmp_cnt
print(check)
_sum = 0
for i in check:
    _sum += sum(i)

if _sum == 0:
    # 정상 수행
    print(count)
    for i in answer:
        print(i[0], i[1], i[2])
else:
    print(-1)
