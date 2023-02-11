import sys
# from math import abs
sys.stdin = open("bj_1449_in.txt", "r")
input = sys.stdin.readline
'''
길이가 L인 테이프 무한개
적어도 해당 위치 좌우 0.5만큼 간격을 줘야 물이 안샘
N: 물이 새는 곳 위치 갯수
그 담줄: 물이 세는 위치


'''


N, L = map(int, input().split())

leak_loc = list(map(int, input().split()))

print(leak_loc)

leak_loc.sort()

act = 0
count = 0
for i in range(len(leak_loc)):
  if act != i:
    continue
  for j in range(i+1, len(leak_loc)):
    if abs(leak_loc[i] - leak_loc[j]) >= L:
      act = j
      break

  count += 1

print(count)