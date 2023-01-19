'''
단어 정렬
- 예상 알고리즘 분류: 정렬(sorting)

1. 알파벳 정렬(우선순위)
  ㄴ 길이
  ㄴ 사전 순
길이로 했는데 또 다시 사전 순으로 하면 길이로 했던게 의미가 없어진다.
sort()는 위 과정이 적용 됨

2. 같은 단어가 여러개 있으면 한 번만 출력

sol)
중복 방지로 set사용
sort함수로 lambda (length, chr)
같은 길이 -> 
'''

import sys

sys.stdin = open("bj_1181_in.txt", "r")

input = sys.stdin.readline

N = int(input())

wordList = list(set(input().strip() for _ in range(N)))

wordList.sort(key= lambda x: (len(x), x))

# result = []
# for i in range(len(wordList)):
#   result.append((len(wordList[i]), i))
# print(result)

# wordList.sort(key= lambda x: len(x))

print(*wordList, sep='\n')
# for i in range(len(wordList)):
#   print(wordList[i])



'''
sol2)
import sys

def sol(N, wordList):
  # print(N)
  for i in range(N-1):
    for j in range(N - 1 - i):
      # print(j)
      if len(wordList[j]) > len(wordList[j+1]):
        wordList[j], wordList[j+1] = wordList[j+1], wordList[j]
        continue
      check = (len(wordList[j]) == len(wordList[j+1])) and (wordList[j] > wordList[j+1])

      if check:
        wordList[j], wordList[j+1] = wordList[j+1], wordList[j]


  for i in wordList:
    print(i)



sys.stdin = open("bj_1181_in.txt", "r")

N = int(input())

wordList = list(set(input() for _ in range(N)))

# wordList.sort(key=lambda x: len(x), reverse=False)


# print('no' > 'it')
sol(len(wordList), wordList)

'''



'''
sol1)
import sys

def sol(N, wordList):
  # print(N)
  for i in range(N-1):
    for j in range(N - 1 - i):
      # print(j)
      check = (len(wordList[j]) == len(wordList[j+1])) and (wordList[j] > wordList[j+1])

      if check:
        wordList[j], wordList[j+1] = wordList[j+1], wordList[j]


  for i in wordList:
    print(i)



sys.stdin = open("bj_1181_in.txt", "r")

N = int(input())

wordList = list(set(input() for _ in range(N)))

wordList.sort(key=lambda x: len(x), reverse=False)


# print('no' > 'it')
sol(len(wordList), wordList)

'''