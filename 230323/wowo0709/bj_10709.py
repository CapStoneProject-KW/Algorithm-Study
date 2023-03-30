def solution() -> list[list[int]]:
    ret = [[] for _ in range(H)]
    for i in range(H):
        arr = list(input())
        c = False
        for j in range(W):
            if c == False:
                if arr[j] == '.': 
                    ret[i].append(-1)
                elif arr[j] == 'c': 
                    ret[i].append(0)
                    c = True
            else:
                if arr[j] == '.': 
                    ret[i].append(ret[i][j-1]+1)
                elif arr[j] == 'c': 
                    ret[i].append(0)
    return ret


if __name__ == '__main__':
    H, W = map(int, input().split())
    ans = solution()
    for i in range(H):
        print(*ans[i])