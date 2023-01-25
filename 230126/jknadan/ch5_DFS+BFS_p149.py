# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

# map 정보 입력 및 저장
tray = []

for i in range(N):
    tray.append(list(map(int, input())))

count = 0


def DFS(i, j):
    global tray

    # 현재 기준 우측이 0이고 이동 가능하면 현재를 = 1 처리하고 DFS 탐색
    if tray[i][j + 1] == 0:
        tray[i][j] = 1
        DFS(i, j + 1)

    # 현재 기준 아래측이 0이고 이동 가능하면 현재를 = 1 처리하고 DFS 탐색
    if tray[i + 1][j] == 0:
        tray[i][j] = 1
        DFS(i + 1, j)

    # Base case 혹시 몰라 예외처리 빡세게 : 그냥 return 0 해도 되나?
    elif (tray[i + 1][j] and tray[i - 1][j] and tray[i][j + 1] and tray[i][j - 1]) != 0:
        return 0


def searching(i, j):
    global tray, N, M
    if i <= -1 or i >= N or j <= -1 or j >= M:
        return False
    elif tray[i][j] == 0:
        DFS(i, j)
        # global 키워드 쓰고 그 다음에 값이든 뭐든 할당
        global count
        count += 1

    else:
        return 0


for i in range(N):
    for j in range(M):
        searching(i, j)

# 값 출력
print(count)

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

를 하게 되면 index Error가 뜬다. 왜 그러는 걸까?
'''
