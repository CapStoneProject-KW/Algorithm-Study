import sys
sys.stdin = open("bj_11053_in.txt")
input = sys.stdin.readline
'''
어디서 많이 본 문제...?
for문 돌면서 해당 인덱스를 증가시키는 방식?
'''

def solution():
    num_list = [1] * N


    for i in range(1, N):
        max_value = 0
        for j in range(i):
            if A_list[i] > A_list[j]:
                max_value = max(max_value, num_list[j])  
        num_list[i] += max_value

    return max(num_list)


N = int(input())
A_list = list(map(int, input().split()))

print(solution())