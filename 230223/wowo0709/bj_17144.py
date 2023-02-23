'''
1초 동안 일어나는 일
- 미세먼지의 확산
    - 인접한 4 방향으로 d//5 씩 확산, 자기 위치는 d - nx(d//5) 가 됨
    - 벽이거나, 공기청정기로는 확산 X
- 공기청정기 작동
    - 위쪽 바람은 반시계로, 아래쪽 바람은 시계로
    - 미세먼지가 바람에 닿으면 바람의 방향대로 1칸 이동
    - 바람에 의해 공기청정기 위치로 가면 사라짐
'''
def print_board(board):
    H, W = len(board), len(board[0])
    for i in range(H):
        for j in range(W):
            print(board[i][j], end=' ')
        print()

def spread_dusts(board: list[list], cleaner: list[tuple]) -> list[list]:
    didj = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    H, W = len(board), len(board[0])
    spreaded_dusts = [[0 for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if board[i][j] == 0 or board[i][j] == -1:
                continue
            cnt = 0
            for di, dj in didj:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and (ni, nj) not in cleaner:
                    spreaded_dusts[ni][nj] += board[i][j] // 5
                    cnt += 1
            board[i][j] -= cnt * (board[i][j] // 5)
    for i in range(H):
        for j in range(W):
            board[i][j] += spreaded_dusts[i][j]
    return board

def run_air_cleaner(board: list[list], cleaner: list[tuple]) -> dict:
    H, W = len(board), len(board[0])
    move_wind = {'up': [(0, 1), (-1, 0), (0, -1), (1, 0)], # counter-clockwise
                 'down': [(0, 1), (1, 0), (0, -1), (-1, 0)]} # clockwise
    # air cleaning process
    for e, side in enumerate(['up', 'down']):
        direction = 0
        wind = [cleaner[e], (cleaner[e][0], cleaner[e][1]+1)]
        previous = 0 # right next to cleaner
        while wind[1] != cleaner[e]:
            # move wind
            # 원래 방향대로 이동
            next_wind = [[0, 0], [0, 0]]
            for i in range(2): # wind location
                for j in range(2): # i, j
                    next_wind[i][j] = wind[i][j] + move_wind[side][direction][j]
            # 범위를 넘는지 확인하고, 넘었다면 방향전환
            if not (0 <= next_wind[1][0] < H and 0 <= next_wind[1][1] < W):
                next_wind = [(wind[0][0]+move_wind[side][direction][0], wind[0][1]+move_wind[side][direction][1]),
                        (wind[1][0]+move_wind[side][direction+1][0], wind[1][1]+move_wind[side][direction+1][1])]
                direction += 1
            wind = [tuple(next_wind[0]), tuple(next_wind[1])]
            # move dust
            board[wind[0][0]][wind[0][1]], previous = previous, board[wind[0][0]][wind[0][1]]
    return board

def solution(board: list[list], cleaner: list[tuple], time: int) -> int:
    for t in range(time):
        # spread dusts
        board = spread_dusts(board, cleaner)
        # print(f'Time: {t} (after spread)')
        # print_board(board)
        # run air cleaner
        board = run_air_cleaner(board, cleaner)
        # print(f'Time: {t} (after cleaning)')
        # print_board(board)
    return sum(map(sum, board)) + 2 # +2: cleaner


if __name__ == '__main__':
    R, C, T = map(int, input().split())
    board, cleaner = [], []
    for i in range(R):
        board.append(list(map(int, input().split())))
        for j in range(C):
            if board[i][j] == -1:
                cleaner.append((i, j))
    print(solution(board, cleaner, T))
    
    

### 시간초과
"""
def spread_dusts(size: tuple, air_cleaner: list[tuple], dusts: dict[tuple, int]) -> dict:
    didj = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    H, W = size
    spreaded_dusts = {}
    for (ci, cj), amount in dusts.items():
        cnt = 0
        for di, dj in didj:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < H and 0 <= nj < W and (ni, nj) not in air_cleaner:
                spreaded_dusts[(ni, nj)] = spreaded_dusts.get((ni, nj), 0) + amount // 5
                cnt += 1
        dusts[(ci, cj)] -= cnt * (amount // 5)
    for spreaded_loc, amount in spreaded_dusts.items():
        dusts[spreaded_loc] = dusts.get(spreaded_loc, 0) + amount
    return dusts

def run_air_cleaner(size: tuple, air_cleaner: list[tuple], dusts: dict[tuple, int]) -> dict:
    H, W = size
    moved_dusts = {} # moved_dusts[(original_loc)] = ((moved_loc), amount)
    move_wind = {'up': [(0, 1), (-1, 0), (0, -1), (1, 0)], # counter-clockwise
                 'down': [(0, 1), (1, 0), (0, -1), (-1, 0)]} # clockwise
    # air cleaning process
    for i, side in enumerate(['up', 'down']):
        direction = 0
        wind = [air_cleaner[i], (air_cleaner[i][0], air_cleaner[i][1]+1)]
        while wind[1] != air_cleaner[i]:
            # move wind
            # 원래 방향대로 이동
            next_wind = [[0, 0], [0, 0]]
            for i in range(2): # wind location
                for j in range(2): # i, j
                    next_wind[i][j] = wind[i][j] + move_wind[side][direction][j]
            # 범위를 넘는지 확인하고, 넘었다면 방향전환
            if not (0 <= next_wind[1][0] < H and 0 <= next_wind[1][1] < W):
                next_wind = [(wind[0][0]+move_wind[side][direction][0], wind[0][1]+move_wind[side][direction][1]),
                        (wind[1][0]+move_wind[side][direction+1][0], wind[1][1]+move_wind[side][direction+1][1])]
                direction += 1
            (ni1, nj1), (ni2, nj2) = next_wind
            wind = [(ni1, nj1), (ni2, nj2)]
            # move dust
            if wind[0] in dusts:
                moved_dusts[wind[0]] = (wind[1], dusts[wind[0]])
    # Apply air cleaning result
    for original_loc in moved_dusts.keys():
        dusts.pop(original_loc)
    for moved_loc, amount in moved_dusts.values():
        if moved_loc in air_cleaner:
            continue
        dusts[moved_loc] = amount
    return dusts

def solution(size: tuple, air_cleaner: list[tuple], dusts: dict[tuple, int], time: int) -> int:
    for t in range(time):
        # spread dusts
        dusts = spread_dusts(size, air_cleaner, dusts)
        print(f'Time: {t} (after spread)')
        print_board(size, air_cleaner, dusts)
        # run air cleaner
        dusts = run_air_cleaner(size, air_cleaner, dusts)
        print(f'Time: {t} (after cleaning)')
        print_board(size, air_cleaner, dusts)
    return sum(dusts.values())


if __name__ == '__main__':
    R, C, T = map(int, input().split())
    size = (R, C)
    air_cleaner = [] # (a, b), (a+1, b)
    dusts = {} # dusts = {row}
    for i in range(R):
        arr = list(map(int, input().split()))
        for j in range(C):
            if arr[j] == -1: air_cleaner.append((i, j))
            if arr[j] > 0: dusts[(i, j)] = arr[j]
    print(solution(size, air_cleaner, dusts, T))
"""

### 시간초과
"""
def spread_dusts(size: tuple, air_cleaner: list[tuple], dusts: dict[tuple, int]) -> dict:
    didj = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    H, W = size
    spreaded_dusts = {}
    for (ci, cj), amount in dusts.items():
        cnt = 0
        for di, dj in didj:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < H and 0 <= nj < W and (ni, nj) not in air_cleaner:
                spreaded_dusts[(ni, nj)] = spreaded_dusts.get((ni, nj), 0) + amount // 5
                cnt += 1
        dusts[(ci, cj)] -= cnt * (amount // 5)
    for spreaded_loc, amount in spreaded_dusts.items():
        dusts[spreaded_loc] = dusts.get(spreaded_loc, 0) + amount
    # print(f'Time: {t} (after spread)')
    # print_board(size, air_cleaner, dusts)
    return dusts

def run_air_cleaner(size: tuple, air_cleaner: list[tuple], dusts: dict[tuple, int]) -> dict:
    H, W = size
    moved_dusts = {} # moved_dusts[(original_loc)] = ((moved_loc), amount)
    # upward
    wind = [air_cleaner[0], (air_cleaner[0][0], air_cleaner[0][1]+1)]
    while wind[1] != air_cleaner[0]:
        # move dust
        if wind[0] in dusts:
            moved_dusts[wind[0]] = (wind[1], dusts[wind[0]])
        # move wind
        if (wind[1][1] - wind[0][1]) == 1: # right
            if wind[1][1] == W-1: wind = [wind[1], (wind[1][0]-1, wind[1][1])] # up
            else: wind = [wind[1], (wind[1][0], wind[1][1]+1)]
        elif (wind[1][0] - wind[0][0]) == -1: # up
            if wind[1][0] == 0: wind = [wind[1], (wind[1][0], wind[1][1]-1)] # left
            else: wind = [wind[1], (wind[1][0]-1, wind[1][1])] 
        elif (wind[1][1] - wind[0][1]) == -1: # left
            if wind[1][1] == 0: wind = [wind[1], (wind[1][0]+1, wind[1][1])] # down
            else: wind = [wind[1], (wind[1][0], wind[1][1]-1)] 
        elif (wind[1][0] - wind[0][0]) == 1: # down
            if wind[1] == air_cleaner[0]: wind = [wind[1], (wind[1][0], wind[1][1]+1)] # right
            else: wind = [wind[1], (wind[1][0]+1, wind[1][1])]
    # bottom
    wind = [air_cleaner[1], (air_cleaner[1][0], air_cleaner[1][1]+1)]
    while wind[1] != air_cleaner[1]:
        # move dust
        if wind[0] in dusts:
            moved_dusts[wind[0]] = (wind[1], dusts[wind[0]])
        # move wind
        if (wind[1][1] - wind[0][1]) == 1: # right
            if wind[1][1] == W-1: wind = [wind[1], (wind[1][0]+1, wind[1][1])] # down
            else: wind = [wind[1], (wind[1][0], wind[1][1]+1)]
        elif (wind[1][0] - wind[0][0]) == 1: # down
            if wind[1][0] == H-1: wind = [wind[1], (wind[1][0], wind[1][1]-1)] # left
            else: wind = [wind[1], (wind[1][0]+1, wind[1][1])]
        elif (wind[1][1] - wind[0][1]) == -1: # left
            if wind[1][1] == 0: wind = [wind[1], (wind[1][0]-1, wind[1][1])] # up
            else: wind = [wind[1], (wind[1][0], wind[1][1]-1)] 
        elif (wind[1][0] - wind[0][0]) == -1: # up
            if wind[1] == air_cleaner[1]: wind = [wind[1], (wind[1][0], wind[1][1]+1)] # right
            else: wind = [wind[1], (wind[1][0]-1, wind[1][1])] 
    # Apply air cleaning result
    for original_loc in moved_dusts.keys():
        dusts.pop(original_loc)
    for moved_loc, amount in moved_dusts.values():
        if moved_loc in air_cleaner:
            continue
        dusts[moved_loc] = amount
    # print(f'Time: {t} (after cleaning)')
    # print_board(size, air_cleaner, dusts)
    return dusts

def solution(size: tuple, air_cleaner: list[tuple], dusts: dict[tuple, int], time: int) -> int:
    for t in range(time):
        # spread dusts
        dusts = spread_dusts(size, air_cleaner, dusts)
        # run air cleaner
        dusts = run_air_cleaner(size, air_cleaner, dusts)
    return sum(dusts.values())


if __name__ == '__main__':
    R, C, T = map(int, input().split())
    size = (R, C)
    air_cleaner = [] # (a, b), (a+1, b)
    dusts = {} # dusts = {row}
    for i in range(R):
        arr = list(map(int, input().split()))
        for j in range(C):
            if arr[j] == -1: air_cleaner.append((i, j))
            if arr[j] > 0: dusts[(i, j)] = arr[j]
    print(solution(size, air_cleaner, dusts, T))
"""