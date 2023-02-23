import sys
sys.stdin = open("bj_1924_in.txt", "r")
input = sys.stdin.readline

day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x, y = map(int, input().split())

yoil = 0
for mon in range(1, x+1):
    date = 28
    if mon in [1, 3, 5, 7, 8, 10, 12]:
        date = 31
    elif mon in [4, 6, 9, 11]:
        date = 30

    if mon == x:
        yoil += y
    else:
        yoil += date


print(day_list[yoil%7])
