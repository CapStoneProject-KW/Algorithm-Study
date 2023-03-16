from collections import Counter

def solution(n: int):
    cnts = Counter(str(n))
    cnts['69'] = (cnts['6'] + cnts['9'] + 1) // 2 
    del cnts['6'], cnts['9']
    return max(cnts.values())


if __name__ == '__main__':
    n = int(input())
    print(solution(n))