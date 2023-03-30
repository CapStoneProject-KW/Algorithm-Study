import sys
sys.stdin = open("bj_10799_in.txt", "r")
input = sys.stdin.readline
'''
1. ()가 레이저
2. 막대 안에 레이저가 몇 개 존재하는지 counting
3. 막대 판별
하나씩 push하면서 
'''

def solution():
    s = []
    answer = 0
    for i in range(len(bracket)):
        if bracket[i] == '(':
            s.append(i)
        elif bracket[i] == ')':
            if s[-1] == i-1: # 레이저
                s.pop()
                answer += len(s)
            else: # 
                s.pop()
                answer += 1
    print(answer)

bracket = input().strip()

solution()
