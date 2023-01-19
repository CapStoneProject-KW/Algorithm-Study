'''
나이순 정렬
- 예상 알고리즘 분류: 정렬

1. 우선순위: 나이 -> 가입순
'''

import sys

sys.stdin = open("bj_10814_in.txt", "r")
input = sys.stdin.readline

N = int(input())

infoList = [input().strip().split() for _ in range(N)]
# print(infoList)

newList = [[i, int(infoList[i][0]), infoList[i][1]] for i in range(N)]
# print(newList)

newList.sort(key=lambda x: (x[1], x[0]))
# print(newList)

for i in range(N):
  print(newList[i][1], newList[i][2])

'''
나이를 int로 바꾸지 않아 string으로 정렬을 해서 계속 틀렸음
'''


'''
sol2)
import sys

sys.stdin = open("bj_10814_in.txt", "r")
input = sys.stdin.readline

N = int(input())

infoList = [input().strip().split() for _ in range(N)]

midList = list(enumerate(infoList))

midList.sort(key=lambda x: (x[1][0], x[0]))

for i in midList:
  print(i[1][0], i[1][1])


'''


'''
import sys

sys.stdin = open("bj_10814_in.txt", "r")
input = sys.stdin.readline

N = int(input())

# infoList = list(enumerate(input().strip().split()) for i in range(N))

infoList = [input().strip().split() for _ in range(N)]

resultTuple = list(tuple(enumerate(infoList)))


# infoList = [entry for entry in enumerate(input().strip())]

print(resultTuple)
resultTuple.sort(key=lambda x: (x[1][0], x[0]))

for i in range(N):
  print(resultTuple[i][1][0], resultTuple[i][1][1])

'''

