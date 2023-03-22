import sys
sys.stdin = open("bj_10709_in.txt", "r")
input = sys.stdin.readline

def solution(info):
    answer = [[-1]*W for _ in range(H)]
    
    for i in range(H):
        if 'c' not in info[i]:
            answer[i] = [-1] * W
            continue
        for j in range(W):
            if info[i][j] == 'c':
                answer[i][j] = 0
            elif info[i][j] == '.':
                count = 1
                for k in range(j-1, -1, -1):
                    if info[i][k] == 'c':
                        answer[i][j] = count
                        break
                    count += 1
    
    for i in answer:
        print(*i)
                


H, W = map(int, input().split())

info = [list(input().strip()) for _ in range(H)]

solution(info)