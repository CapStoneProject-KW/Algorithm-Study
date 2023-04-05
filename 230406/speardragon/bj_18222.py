import sys
# sys.stdin = open("bj_18222_in.txt")
input = sys.stdin.readline
'''
k=4
0110

f(0) = 0 1
f(1) = 01 2
f(2) = 0110 3~4
f(3) = 0110 1001 5~8
f(4) = 0110100110 010110 9~16

해당 위치가 어느 level에 위치해 있는지
level-1 했을 때 절반을 기준으로

1 -> 0
2 -> 1
3 -> 2(1)
4 -> 1(0)

a0 = 0
a1 = 1
a2n = 1- solution(n//2)
a2n+1 = solution(n//2)


a1 = 0
a2 = 1
a3 = 1
a4 = 0

a5 = 1 그대로
a6 = 0 1-
a7 = 0 1-
a8 = 1 그대로

a9 = 1 1-
a10 = 0 1-
a11 = 0 1-
a12 = 1 1-
'''

def solution(x): # 6
    # base case
    if x == 0 or x == 1:
        if x == 0: return 0
        else: return 1
    elif x%2!=0:
        return 1-solution(x//2)
    else:
        return solution(x//2)
    
def solution2(x):
    print(x)
    if x==0 or x==1:
        return x
    elif x%2==0:
        return solution2(x//2)
    else:
        return 1-solution2(x//2)



k = int(input())

print(solution2(k-1))

