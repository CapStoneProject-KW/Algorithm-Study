'''
[가로]: 오른쪽, 오른쪽 아래
[세로]: 아래, 오른쪽 아래
[오른쪽 아래]: 오른쪽, 오른쪽 아래, 아래
오른쪽/아래의 경우 이동할 칸만 비워져 있으면 됨
오른쪽 아래의 경우 오른쪽, 아래가 모두 비워져 있어야 됨
목적지로 이동시킬 수 있는 총 방법의 개수는? -> 백트래킹
+)
만약에 다음 위치에서 목적지로 갈 수 있는 경우가 n이면, 
현재 위치에서 목적지로 갈 수 있는 경우는 +n
단, '방향'까지 같아야 함
'''
### Python3: 48ms
global N, MAP, DEST, dp, visited
moves = {
    'hor': [(0, 1, 'hor'), (1, 1, 'diag')], # 오른쪽, 오른쪽아래
    'ver': [(1, 0, 'ver'), (1, 1, 'diag')], # 아래, 오른쪽아래
    'diag': [(0, 1, 'hor'), (1, 0, 'ver'), (1, 1, 'diag')] # 오른쪽, 아래, 오른쪽아래
}

# direction 방향으로 이동해서 cur 위치로 이동할 수 있는지 검사
def is_movable(cur: tuple[int, int], direction: str) -> bool:
    (cx, cy), cd = cur, direction
    # Out of boundary
    if not (cx < N and cy < N):
        return False
    # Check if it's empty space
    if cd == 'hor' and MAP[cx][cy] == 0:
        return True
    elif cd == 'ver' and MAP[cx][cy] == 0:
        return True
    elif cd == 'diag' and not (MAP[cx-1][cy] or MAP[cx][cy-1] or MAP[cx][cy]): # all 0
        return True
    return False

# 현재 위치 cur와 온 방향 direction이 주어졌을 때, 목적지 dest까지 이동하는 경우의 수
def solution(cur: tuple[int, int], direction: str) -> int:
    if cur == DEST:
        return 1
    (cx, cy), cd = cur, direction
    visited[cx][cy][cd] = 1
    for move in moves[cd]:
        nx, ny, nd = cx+move[0], cy+move[1], move[2]
        if is_movable((nx, ny), nd):
            if dp[nx][ny][nd] > 0:
                dp[cx][cy][cd] += dp[nx][ny][nd]
            elif not visited[nx][ny][nd]: # dp[nx][ny] == 0
                cnt = solution((nx, ny), nd)
                dp[cx][cy][cd] += cnt
            else: # dp[nx][ny] == 0, visited[nx][ny] == 1
                continue
    return dp[cx][cy][cd]
        

if __name__ == '__main__':
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    DEST = (N-1, N-1)
    dp = [[{'hor': 0, 'ver': 0, 'diag': 0} for _ in range(N)] for _ in range(N)]
    visited = [[{'hor': 0, 'ver': 0, 'diag': 0} for _ in range(N)] for _ in range(N)]
    print(solution(cur=(0, 1), direction='hor'))


### 시간초과
"""
global N, MAP, DEST
moves = {
    'hor': [(0, 1, 'hor'), (1, 1, 'diag')], # 오른쪽, 오른쪽아래
    'ver': [(1, 0, 'ver'), (1, 1, 'diag')], # 아래, 오른쪽아래
    'diag': [(0, 1, 'hor'), (1, 0, 'ver'), (1, 1, 'diag')] # 오른쪽, 아래, 오른쪽아래
}

# direction 방향으로 이동해서 cur 위치로 이동할 수 있는지 검사
def is_movable(cur: tuple[int, int], direction: str) -> bool:
    # Out of boundary
    if not (cur[0] < N and cur[1] < N):
        return False
    # Check if it's empty space
    if direction == 'hor' and MAP[cur[0]][cur[1]] == 0:
        return True
    elif direction == 'ver' and MAP[cur[0]][cur[1]] == 0:
        return True
    elif direction == 'diag' and MAP[cur[0]-1][cur[1]] == 0 \
                                and MAP[cur[0]][cur[1]-1] == 0 \
                                and MAP[cur[0]][cur[1]] == 0:
        return True
    return False

# 현재 위치 cur와 온 방향 direction이 주어졌을 때, 목적지 dest까지 이동하는 경우의 수
def solution(cur: tuple[int, int], direction: str, cnt: int) -> int:
    if cur == DEST:
        return cnt + 1
    for move in moves[direction]:
        next = (cur[0]+move[0], cur[1]+move[1])
        if is_movable(next, move[2]):
            cnt = solution(next, move[2], cnt)
    return cnt
        

if __name__ == '__main__':
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    DEST = (N-1, N-1)
    print(solution(cur=(0, 1), direction='hor', cnt=0))
"""