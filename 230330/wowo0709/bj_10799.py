def solution(brackets: str) -> int:
    s = []
    cnt = 0
    for b in brackets:
        if b == '(':
            s.append(b)
            laser = True
        else:
            s.pop()
            if laser: cnt += len(s)
            else: cnt += 1
            laser = False
    return cnt


if __name__ == '__main__':
    brackets = input()
    print(solution(brackets))