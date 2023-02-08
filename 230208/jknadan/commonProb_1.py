N, L = map(int, input().split())  # 정수형으로 값 입력 받기, 스페이스바로 값 연속으로 받기
array = list(map(int, input().split()))

array.sort()
arrIndex = 0
count = 0

print(array)
def remainTape(index, L):
    global count, arrIndex

    if index + 1 >= len(array):
        count += 1
        return 0

    if (array[index + 1] - array[index]) == L - 1:
        count += 1
        arrIndex = index + 1
        # print(count)

    elif array[index + 1] - array[index] < L - 1:
        remainTape(index + 1, L - abs(array[index + 1] - array[index]))
        # print("재귀 조짐")

    elif array[index + 1] - array[index] > L - 1:
        count += 1
        arrIndex = index


while True:
    if arrIndex < len(array):
        remainTape(arrIndex, L)
        arrIndex += 1
    else:
        break


print(count)
