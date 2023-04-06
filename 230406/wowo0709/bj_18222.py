def solution(k: int) -> int:
    if k <= 1:
        return k
    if k%2 == 0:
        return solution(k//2)
    else:
        return 1 - solution(k//2)


if __name__ == '__main__':
    print(solution(int(input())-1))