import sys
import math
sys.stdin = open("bj_18111_in.txt", "r")
input = sys.stdin.readline
from collections import Counter

'''
NxM 집터 -> 땅 높이 일정하게

ret: running time, height of ground

for문을 돌면서 
1. 평평하게 만들기
2. 빈 곳 채우기

한 원소에 대해 다른 모든 것들을 그 갯수로 바꾸기

sol1) 시간 초과 -> 
'''

# def solution1(MAP, block_set, rest_item):
#     remove_block = 2
#     put_block = 1
#     visited = []

#     max_value = -1
#     min_time = math.inf
#     block_h = 0
    
#     for ref in block_set:
        
#         running_time = 0

#         # if visited:
#         #     continue
#         for i in range(N):
#             for j in range(M):
#                 # print(i, j, MAP[i][j])
#                 if MAP[i][j] < ref and rest_item >= 1:
#                     running_time += put_block
#                     rest_item -= ref
#                 elif MAP[i][j] > ref:
#                     running_time += remove_block
#                     rest_item += ref
#                 else:
#                     continue

#         # print(running_time, ref)
#         if running_time < min_time and running_time != 0:
#             min_time = running_time
#             block_h = ref
#         elif running_time == min_time and running_time != 0:
#             min_time = running_time
#             block_h = max(block_h, ref)

    
#     print(min_time, block_h)
    

# def solution2(MAP, block_set, rest_item):
#     remove_block = 2
#     put_block = 1

#     flag = 0

#     result_time = math.inf
#     result_height = 0

#     for ref in range(256):
#         running_time = 0
#         flag = 0

#         for i in range(N):
#             for j in range(M):
#                 if MAP[i][j] > ref:
#                     change_num = MAP[i][j] - ref
#                     running_time += remove_block * change_num
#                 elif MAP[i][j] < ref:
#                     change_num = ref - MAP[i][j]
#                     if rest_item >= change_num:
#                         running_time += remove_block * change_num
#                     else:
#                         flag = 1
                

#         if result_time > running_time and not flag:
#             result_time = running_time 
#             result_height = ref
#         elif result_time == running_time and not flag:
#             result_height = max(result_height, ref)
        

#     print(result_time, result_height)   

# def solution3(MAP, block_set, rest_item):
#     remove = 2
#     put = 1

#     flag = 0

#     result_time = math.inf
#     result_height = 0

#     for ref in range(256):
#         running_time = 0
#         flag = 0
#         put_block = 0
#         remove_block = 0

#         for i in range(N):
#             for j in range(M):
#                 if MAP[i][j] > ref:
#                     remove_block += MAP[i][j] - ref
#                 else:
#                     put_block += ref - MAP[i][j]
                
#         if put_block > remove_block + B:
#             continue

#         count = remove_block * remove + put_block * put

#         if count <= result_time:
#             result_time = count
#             result_height = ref

#     print(result_time, result_height)   



def solution(MAP, rest_item, first, last):
    result_time = math.inf
    result_height = 0

    for ref in range(first, last+1):
        if sum_block + rest_item >= ref * N * M:
            cur_time = 0
            for cur_block in MAP:
                if cur_block > ref: # remove
                    cur_time += (cur_block - ref) * MAP[cur_block] * 2
                elif cur_block < ref: # put
                    
                    print(ref, cur_block, MAP, MAP[cur_block])
                    cur_time += (ref - cur_block) * MAP[cur_block]
                    print(cur_time)

            if cur_time <= result_time:
                result_time = cur_time
                result_height = ref

    print(result_time, result_height)


N, M, B = map(int, input().split())

MAP = []

for _ in range(N): MAP += map(int, sys.stdin.readline().split())

min_height = min(MAP)
max_height = max(MAP)
sum_block = sum(MAP)
MAP = dict(Counter(MAP))

solution(MAP, B, min_height, max_height)