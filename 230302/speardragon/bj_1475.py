import sys
from collections import Counter
from math import ceil
sys.stdin = open("bj_1475_in.txt", "r")
input = sys.stdin.readline
'''
6과 9만 따로 빼서 몇개 필요한지 갯수랑 다른 애들 중 max 갯수 중 더 큰 것
'''

N = int(input())
num_list = list(str(N))

num_dict = {'6/9': 0}
for num in num_list:
    if num == '9' or num == '6':
        num_dict['6/9'] = num_dict.get('6/9', 0) + 1
    else:
        num_dict[num] = num_dict.get(num, 0) + 1

max_value = -1
for k, v in num_dict.items():
    if k != '6/9':
        max_value = max(max_value, v)

result = max(max_value, ceil(num_dict['6/9']/2))
# print(max_value, ceil(num_dict['6/9']/2))
print(result)



# result = []
# cnt = 0
# for i in range(len(num_list)):
#     if i == 0:
#         result.append(num_list[i])
#         cnt += 1
#         continue
    
#     if (num_list[i] == '9' and '6' in result and '9' in result): 
#         cnt += 1
#         result.append(num_list[i])

#     elif (num_list[i] == '6' and '9' in result and '6' in result):
#         cnt += 1
#         result.append(num_list[i])

#     if num_list[i] in result:

#         cnt += 1
#     elif num_list[i] not in result:
#         result.append(num_list[i])
#     print(result)