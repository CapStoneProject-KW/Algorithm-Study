import sys
sys.stdin = open("bj_14501_in.txt", "r")
input = sys.stdin.readline

'''
DP
isposible: O
variable: price
점화식: 
f(1) = price_1 if T==1
f(2) = f(1) + price_2 if T(1) <= 2-1
memo: memo[day] = price
base case: 1일 -> T=1이면 가능
'''

def solution2():
    # _memo[0] = 0
    # if _time[0] == 1:
    # _memo[0] = _price[0]

    # for i in range(N):
    #     for j in range(i, N+1):
    #         if _time[i] <= j-i and _time[j] <= N - j:
    #             # print('hi', i, j)
    #             # print(_time[i], j-i)
    #             # print(_time[j], (N+1) - j)
    #             _memo[j] = max(_memo[i] + _price[j], _memo[j])
    #             # print(_memo)
    #             # break

    for i in range(N):
        for j in range(i+_time[i], N+1):
            _memo[j] = max(_memo[i] + _price[i], _memo[j])
            # if _memo[j] < _memo[i] + _price[i]:
            #     _memo[j] = _memo[i] + _price[i]

    return _memo[N]



def solution(memo, price, time):
    for i in range(N-1, -1, -1):
        if time[i]+i > N:
            memo[i] = memo[i+1]
        else:
            memo[i] = max(memo[i+1], price[i]+memo[i+time[i]])
    
    return memo[0]


N = int(input())

_memo = [0] * 1001
_price = []
_time = []

for i in range(N):
    T, P = map(int, input().split())
    _time.append(T)
    _price.append(P)


# print(solution(_memo, _price, _time))
print(solution2())