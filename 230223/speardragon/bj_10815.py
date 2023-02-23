import sys
import bisect
sys.stdin = open("bj_10815_in.txt", "r")
input = sys.stdin.readline

def solution(ordered_list, target):
    index = bisect.bisect_left(ordered_list, target)

    if index < len(ordered_list) and ordered_list[index] == target:
        return 1
    else:
        return 0



N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))


for m in M_list:
    print(solution(N_list, m), end=' ')