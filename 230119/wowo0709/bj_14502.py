from itertools import combinations as C
from collections import deque
from typing import Union

def solution(
    my_map: list[list[int]], 
    new_walls: Union[list, tuple], 
    information: dict[int, list]
    ) -> int:
    '''
    Args:
        my_map: 2d map consisted of 0, 1, and 2
        new_walls: Coordinates of the new walls (1)
        information: Coordinate information of 0, 1, and 2
    Ret:
        Size of the safety area
    '''
    
    H, W = len(my_map), len(my_map[0])
    q = deque([])
    propagated = dict()
    for virus_i, virus_j in information[2]:
        q.append((virus_i, virus_j))
        propagated[(virus_i, virus_j)] = True
        while q:
            cur_i, cur_j = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_i, next_j = cur_i + di, cur_j + dj
                if 0 <= next_i < H and 0 <= next_j < W \
                                and (next_i, next_j) not in new_walls \
                                and my_map[next_i][next_j] == 0 \
                                and not (next_i, next_j) in propagated:
                    propagated[(next_i, next_j)] = True
                    q.append((next_i, next_j))
    return H * W - (len(information[1]) + len(new_walls)) - (len(propagated))
    

if __name__ == '__main__':
    N, M = map(int, input().split())
    MAP = []
    information = {0: [], 1: [], 2: []} # 0: empty 1: wall 2: virus
    for i in range(N):
        MAP.append(list(map(int, input().split())))
        for j in range(M):
            information[MAP[i][j]].append((i, j))
    ans = -1
    for c in C(information[0], 3):
        ans = max(ans, solution(MAP, c, information))
    print(ans)