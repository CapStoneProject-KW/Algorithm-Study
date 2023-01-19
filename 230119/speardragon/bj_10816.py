'''
숫자 카드 2
예상 알고리즘 분류: Searching
시간초과 -> hash

1. N: 상근이가 가진 숫자 카드 갯수
2. M: 상근이가 M이라는 숫자 카드를 얼마나 가지고 있는지
3. 출력: 각 M에 대해 몇 개 가지고 있는지 출력

sol) 덱을 돌면서 searchingList에 값들이 있는지
'''
import sys
from collections import Counter

global NList, MList



sys.stdin = open("bj_10816_in.txt", "r")
input = sys.stdin.readline

N = int(input())
NList = list(map(int, input().split()))

M = int(input())
MList = list(map(int, input().split()))

dict_N = Counter(NList)

# print(MList)
result = [dict_N[i] for i in MList]
print(*result)



'''
sol1) 시간초과
sys.stdin = open("bj_10816_in.txt", "r")
input = sys.stdin.readline

N = int(input())
NList = list(map(int, input().split()))

M = int(input())
MList = list(map(int, input().split()))

# sol(0, len(NList)-1)

countN = [NList.count(i) for i in MList]

print(*countN)
'''