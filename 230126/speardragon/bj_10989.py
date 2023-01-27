import sys
from collections import Counter
sys.stdin = open("bj_10989_in.txt", "r")
input = sys.stdin.readline



# def solution(num_list):
    


N = int(input())

num_list = [0] * 10001

for i in range(N):
    num_list[int(input())] += 1


for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)




# print(*num_list, sep='\n')
