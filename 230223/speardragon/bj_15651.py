import sys
from itertools import combinations_with_replacement as H
from itertools import product as P
sys.stdin = open("bj_15651_in.txt", "r")
input = sys.stdin.readline


# N, M = map(int, input().split())

# num_list = [i for i in range(1, N+1)]

# # print(list(H(num_list, M)))
# for h in H(num_list, M):
#     print(*h)


N, M = map(int, input().split())

num_list = [i for i in range(1, N+1)]

for p in P(num_list, repeat=M):
    print(*p)



def solution(ans):
    if len(ans) == M:
        print(*ans)
        return 

    for i in range(1, N+1):
        ans.append(i)
        solution(ans)
        ans.pop()

N, M = map(int, input().split())

solution([])