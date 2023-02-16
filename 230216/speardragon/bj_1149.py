import sys
sys.stdin = open("bj_1149_in.txt", "r")
input = sys.stdin.readline
'''
DP - top down

overlapping part : 

f(1) = min(arr)
f(2) = f(1) + 

1 100 2
1 100 4

'''


# def solution(idx):
#     print(idx, _memo)
#     if idx == 0:
#         print(house[idx], min(house[idx]))
#         return min(house[idx])

#     if _memo[idx] is None:
#         min_value = min(house[idx][flag+1], house[idx][flag+2]) + solution(idx-1)

        
#         min_value = min(house[idx]) + solution(idx-1)
#         print(min_value, _memo)
#         _memo[idx] = min_value
       
#     return _memo[idx]
    

# def solution():
#     result = []
#     for i in range(3):
#         _memo = [None] * (N)
#         _memo[0] = house[0][i]
#         flag = i

#         for j in range(1, len(house)):
#             # print(house[j][(flag+1)%3], house[j][(flag+2)%3])
#             # min_value = min(house[j][(flag+1)%3], house[j][(flag+2)%3])
#             if house[j][(flag+1)%3] <= house[j][(flag+2)%3]:
#                 min_value = house[j][(flag+1)%3]
#                 flag = (flag+1)%3
#             elif house[j][(flag+1)%3] > house[j][(flag+2)%3]:
#                 min_value = house[j][(flag+2)%3]
#                 flag = (flag+2)%3

#             _memo[j] = min_value
            
        
#         print(_memo)
#         print(sum(_memo))

#         result.append(_memo[N-1])


def solution():
    for i in range(1, N):
        house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
        house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
        house[i][2] = min(house[i-1][1], house[i-1][0]) + house[i][2]
        print(house)
    return min(house[N-1][0], house[N-1][1], house[N-1][2])



N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]

# print(solution(len(house) - 1))
print(solution())

