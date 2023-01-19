# # N = 세로 || M = 가로
# N, M = map(int, input().split())
# ix, iy, dir = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(M)]  # 선언과 동시에 입력받기
#
# arrival = [(ix, iy)]  # 가장 초기 값을 도착 리스트에 넣기
# able = 0
# for i in range(M):
#     able += arr[i].count(0)
#
# while len(arrival) == able:
#
#     if dir == 4:
#         dir = 0
#
#     if dir == 0:
#         if (ix, iy - 1) in arrival:
#             dir += 1
#             continue
#         else:
#             ix += 0
#             iy -= 1
#             arrival.append((ix, iy))
#             dir += 1
#     if dir == 1:
#         if (ix + 1, iy) in arrival:
#             dir += 1
#             continue
#         else:
#             ix += 1
#             iy += 0
#             arrival.append((ix, iy))
#             dir += 1
#     if dir == 2:
#         if (ix, iy + 1) in arrival:
#             dir += 1
#             continue
#         else:
#             ix += 0
#             iy += 1
#             arrival.append((ix, iy))
#             dir += 1
#     if dir == 3:
#         if (ix - 1, iy) in arrival:
#             dir += 1
#             continue
#         else:
#             ix -= 1
#             iy += 1
#             arrival.append((ix, iy))
#             dir += 1
#     if ( (ix + 1, iy) and (ix - 1, iy) and (ix, iy + 1) and (ix, iy - 1) ) or (ix,iy) == (1,1) in arrival:
#         ix -= 1
#         iy
#
# print(len(arrival))


# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())

d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [1,0,1,0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    turn_left() # 왼쪽으로 회전
    nx = x+ dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
# 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
else:
    turn_time += 1

# 네 방향 모두 갈 수 없는 경우
if turn_time ==4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동하기
    if array[nx][ny] == 0:
        x= nX
        y= ny
        # 뒤가 바다로 막혀있는 경우
    else :
        break
    turn_time = 0

print (count)