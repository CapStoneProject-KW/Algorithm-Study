import sys
sys.stdin = open("bj_11866_in.txt", "r")
input = sys.stdin.readline

'''
for문을 돌면서 하나씩 pop
pop 하는 인덱스는 modulo 연산으로

'''

N, K = map(int, input().split()) # [7, 3]

table = [i+1 for i in range(N)]

select = 0
result = []
for i in range(N):
  length = len(table) # 7

  next_select = select + K - 1

  select = next_select if next_select < length else (next_select % length)
  
  elem = table.pop(select)
  result.append(elem)

print('<', end='')
print(*result, sep=', ', end='')
print('>', end='')

