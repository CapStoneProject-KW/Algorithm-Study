'''
1. 잔돈 500, 100, 50, 10, 5, 1
2. 거스름돈 갯수 제일 적게
3. 1000짜리 냄.
4. 그리디 알고리즘
sol) 큰 거 순서대로 
620 = 500 + 100 + 10 * 2
'''

price = 1000 - int(input())

count = 0
rest = price 

# if (rest >= 500):
#     count += price // 500
#     rest %= 500

# if (rest >= 100):
#     count += rest // 100
#     rest %= 100

# if (rest >= 50):
#     count += rest // 50
#     rest %= 50

# if (rest >= 10):
#     count += rest // 10
#     rest %= 10

# if (rest >= 5):
#     count += rest // 5
#     rest %= 5

# if (rest >= 1):
#     count += rest // 1
#     rest %= 1

for i in [500, 100, 50, 10, 5, 1]:
    count += rest // i
    rest %= i

print(count)
    

