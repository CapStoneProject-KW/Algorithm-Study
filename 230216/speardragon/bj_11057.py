import sys
sys.stdin = open("bj_11057_in.txt", "r")
input = sys.stdin.readline
from copy import deepcopy
'''
idea: sort를 해도 그대로
memo[] = 오르막 개수

f(1)=10

f(2)=55
00 01 02 03 04 ~ 09
11 12 13 14 
22 23 24
33
44
55
...
99

f(3)
000~999
000 001 002 003
011 012



889 899
999


f(4)
0000 0001

'''


def solution(memo):

  tmp = deepcopy(memo)

  for _ in range(N):
    #print(memo)
    for i in range(10):
        total = 0
        for j in range(0, i+1):
          # print(tmp, tmp[j],i)
          total += tmp[j]

        memo[i] = total
        # print(memo,tmp)
    tmp = deepcopy(memo)
  
  print(tmp[-1] % 10007)
  
      

N = int(input())
# _memo = [0] * (1001)
# _memo = [i for i in range(1, 11)]
_memo = [1 for i in range(10)]

solution(_memo)

'''
tmp = memo를 하면 같은 obejct를 가리키기 때문에 deepcopy를 사용
or 새로 만들기
'''