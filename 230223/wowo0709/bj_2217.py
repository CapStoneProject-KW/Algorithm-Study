# 주어진 로프들을 이용해서 들어올릴 수 있는 물체 하나의 최대 중량
import sys
input = sys.stdin.readline

def solution(ws: list[int]) -> int:
    ws.sort(reverse=True)
    ret = -1
    for i in range(len(ws)):
        ret = max(ret, ws[i]*(i+1))
    return ret


if __name__ == '__main__':
    N = int(input())
    ws = [int(input().rstrip()) for _ in range(N)]
    print(solution(ws))