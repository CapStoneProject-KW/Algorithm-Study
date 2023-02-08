from itertools import combinations as C

def solution(houses: list[tuple], chickens: list[tuple], m: int) -> int:
    chicken_dists = {} # chicken_dists[house] = [((i, j), d), ...]
    for house in houses:
        chicken_dists[house] = []
        for chicken in chickens:
            chicken_dists[house].append((chicken, abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))) # ((i, j), d)
        chicken_dists[house].sort(key=lambda x: x[1]) # ascending order in distance
    # Find the chicken dist of each house excluding the closed chickens
    chicken_dist_of_city = float('inf')
    for closed_chickens in C(chickens, len(chickens)-m):
        tmp = 0
        for house, dists in chicken_dists.items():
            for chicken, dist in dists:
                if chicken in closed_chickens:
                    continue
                tmp += dist
                break
        chicken_dist_of_city = min(chicken_dist_of_city, tmp)
    return chicken_dist_of_city


if __name__ == '__main__':
    N, M = map(int, input().split())
    MAP = []
    houses, chickens = {}, {} # 1, 2
    for i in range(N):
        MAP.append(list(map(int, input().split())))
        for j in range(N):
            if MAP[i][j] == 1: houses[(i, j)] = True
            if MAP[i][j] == 2: chickens[(i, j)] = True
    print(solution(houses, chickens, M))