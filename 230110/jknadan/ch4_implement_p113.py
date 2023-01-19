# TODO : 내가 푼 방법

N = int(input())  # 정수 N 입력

arr = [3, 13, 23, 33, 43, 53]
case = 0

for hh in range(N+1):
    for mm in range(60):
        for ss in range(60):
            if (hh in arr) or (mm in arr) or (ss in arr):
                case += 1


print(case)

# TODO : 책의 방법

# N = int(input())  # 정수 N 입력
# case = 0
#
# for hh in range(N+1):
#     for mm in range(60):
#         for ss in range(60):
#             if '3' in str(hh) + str(mm) + str(ss):
#                 case += 1
#
# print(case)