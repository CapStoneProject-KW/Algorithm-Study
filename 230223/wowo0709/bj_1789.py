'''
S가 있다고 할 때, 
서로 다른 최대한의 숫자의 합으로 나타내려면,
작은 수부터 차례로 더해야 한다. 
만약 더하다가 S보다 커지면, 
그 전 수를 빼고 지금 수를 더한다. 
'''
def solution(s: int):
    stack = []
    _sum = 0
    for i in range(1, s+1):
        _sum += i
        if _sum > s:
            _sum -= stack[-1]
            stack.pop()
        stack.append(i)
        if _sum == s:
            break
    return len(stack)


if __name__ == '__main__':
    S = int(input())
    print(solution(S))